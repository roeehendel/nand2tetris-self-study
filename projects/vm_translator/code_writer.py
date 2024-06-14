import random
import string
from pathlib import Path

from command_type import CommandType

SIMPLE_SEGMENTS = ['local', 'argument', 'this', 'that']
SEGMENTS_BASES = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT',
    'pointer': '3',
    'temp': '5'
}
GLOBAL_SEGMENTS = ['pointer', 'temp']


class CodeWriter:
    def __init__(self, output_file_path: str):
        self._output_file = open(output_file_path, 'w')
        self._current_file_name = Path(output_file_path).stem
        self._current_function_name = None
        self._call_index = 0

    def set_current_file(self, file_name: str):
        self._current_file_name = file_name

    def write_comment(self, comment: str):
        self._write(f'// {comment}')

    def write_empty_line(self):
        self._output_file.write('\n')

    def write_init(self):
        self._write("""
            // INIT CODE
            // SP=256
            @256
            D=A
            @SP
            M=D
        """)

        self.write_call('Sys.init', 0)

        #             @Sys.init
        #             0;JMP

    def write_arithmetic(self, arithmetic_command: str):
        simple_two_operand_commands = ['add', 'sub', 'and', 'or']
        comparison_two_operand_commands = ['eq', 'gt', 'lt']

        TWO_OPERANDS_COMMAND_BASE = """
            @SP
            M=M-1
            A=M
            D=M
            @SP
            A=M-1
        """

        if arithmetic_command in simple_two_operand_commands:
            self._write(TWO_OPERANDS_COMMAND_BASE)
            if arithmetic_command == 'add':
                self._write('M=D+M')
            elif arithmetic_command == 'sub':
                self._write('M=M-D')
            elif arithmetic_command == 'and':
                self._write('M=D&M')
            elif arithmetic_command == 'or':
                self._write('M=D|M')
        elif arithmetic_command in comparison_two_operand_commands:
            random_string = ''.join(random.choices(string.digits, k=10))

            # Compute x-y
            self._write(TWO_OPERANDS_COMMAND_BASE)
            self._write('D=M-D')

            # Compare and jump
            self._write(f'@TRUE_{random_string}')

            if arithmetic_command == 'eq':
                self._write('D;JEQ')
            elif arithmetic_command == 'gt':
                self._write('D;JGT')
            elif arithmetic_command == 'lt':
                self._write('D;JLT')

            self._write("""
                @SP
                A=M-1
                M=0
                @END_{random}
                0;JMP
            (TRUE_{random})
                @SP
                A=M-1
                M=-1
            (END_{random})
            """.format(random=random_string))

        else:
            self._write("""
                @SP
                A=M-1
            """)
            if arithmetic_command == 'neg':
                self._write('M=-M')
            elif arithmetic_command == 'not':
                self._write('M=!M')
            else:
                raise Exception('Unsupported arithmetic command')

    def write_push_pop(self, command_type: CommandType, segment: str, index: int):
        if command_type == CommandType.PUSH:
            self._write_push(segment, index)
        elif command_type == CommandType.POP:
            self._write_pop(segment, index)

    def write_label(self, label: str):
        self._write(f'({self._full_label(label)})')

    def write_goto(self, label: str):
        self._write(f"""
            @{self._full_label(label)}
            0;JMP
        """)

    def write_if_goto(self, label: str):
        self._write_decrement_stack_pointer()

        self._write(f"""
            @SP
            A=M
            D=M
            @{self._full_label(label)}
            D;JNE
       """)

    def write_function(self, function_name: str, num_vars: int):
        self._current_function_name = function_name
        self._write(f'({function_name})')
        for i in range(num_vars):
            self._write_push('constant', 0)

    def write_return(self):
        self._write("""
            // FRAME := R13 = LCL
            @LCL
            D=M
            @R13 
            M=D
            
            // RET := R14 = *(FRAME - 5)
            @R13
            D=M
            @5
            A=D-A
            D=M
            @R14
            M=D
            
            // *ARG = pop()
            @SP
            M=M-1 // SP--
            A=M
            D=M // D = *SP
            @ARG
            A=M
            M=D // *ARG = D
            
            // SP = ARG + 1
            @ARG
            D=M+1
            @SP
            M=D    
        
            // THAT = *(FRAME - 1)
            @R13
            D=M
            @1
            A=D-A
            D=M
            @THAT
            M=D
            
            // THIS = *(FRAME - 2)
            @R13
            D=M
            @2
            A=D-A
            D=M
            @THIS
            M=D
            
            // ARG = *(FRAME - 3)
            @R13
            D=M
            @3
            A=D-A
            D=M
            @ARG
            M=D
            
            // LCL = *(FRAME - 4)
            @R13
            D=M
            @4
            A=D-A
            D=M
            @LCL
            M=D
            
            // goto RET
            @R14
            A=M
            0;JMP
        """)

    def write_call(self, function_name: str, n_args: int):
        return_label = f'{self._current_function_name}$ret{self._call_index}'

        self._write(f"""
            // push return-address
            @{return_label}
            D=A
        """)
        self._write_push_d()

        for memory_location in ['LCL', 'ARG', 'THIS', 'THAT']:
            self._write(f"""
                // push {memory_location}
                @{memory_location}
                D=M
            """)
            self._write_push_d()

        self._write(f"""
            // ARG = SP-n-5
            @SP
            D=M
            @{n_args}
            D=D-A
            @5
            D=D-A
            @ARG
            M=D
        """)

        self._write("""
            @SP
            D=M
            @LCL
            M=D
        """)

        self._write(f"""
            @{function_name}
            0;JMP
        """)

        self._write(f'({return_label})')
        self._call_index += 1

    def _full_label(self, label: str):
        return f'{self._current_function_name}:{label}'

    def _write_push(self, segment: str, index: int):
        # Load the value to push into the D register
        if segment == 'constant':
            self._write(f"""
                @{index}
                D=A
            """)
        elif segment in SIMPLE_SEGMENTS + GLOBAL_SEGMENTS:
            self._write_calculate_address(segment, index)

            self._write(f"""
                A=D
                D=M
            """)
        elif segment == 'static':
            self._write(f"""
                @{self._current_file_name}.{index}
                D=M
            """)

        self._write_push_d()

    def _write_push_d(self):
        self._write("""
            @SP
            A=M
            M=D
        """)

        self._write_increment_stack_pointer()

    def _write_pop(self, segment: str, index: int):
        self._write_decrement_stack_pointer()

        if segment in SIMPLE_SEGMENTS + GLOBAL_SEGMENTS:
            self._write_calculate_address(segment, index)

            # Store the address
            self._write("""
                @R13
                M=D
            """)

            # Write value from stack to address
            self._write("""
                @SP
                A=M
                D=M
                @R13
                A=M
                M=D
            """)
        elif segment == 'static':
            self._write(f"""
                @SP
                A=M
                D=M
                @{self._current_file_name}.{index}
                M=D
            """)

    def _write_calculate_address(self, segment: str, index: int):
        self._write(f'@{SEGMENTS_BASES[segment]}')

        if segment in SIMPLE_SEGMENTS:
            self._write('D=M')
        elif segment in GLOBAL_SEGMENTS:
            self._write('D=A')
        self._write(f"""
            @{index}
            D=D+A
        """)

    def _write_decrement_stack_pointer(self):
        self._write("""
            @SP
            M=M-1
        """)

    def _write_increment_stack_pointer(self):
        self._write("""
            @SP
            M=M+1
        """)

    def _write(self, code: str):
        lines = [line.strip() for line in code.split('\n')]
        lines = [line for line in lines if line != '']

        for line in lines:
            self._output_file.write(f'{line}\n')

    def close(self):
        self._output_file.close()
