import sys
from typing import List

from c_instruction import CInstruction
from src.clean_white_spaces import clean_white_spaces

A_COMMAND_ASM_SYMBOL = '@'
A_COMMAND_BIN_PREFIX = '0'
C_COMMAND_BIN_PREFIX = '111'


class Assembler:
    def __init__(self):
        self.hack_lines = []
        self.symbol_table = {
            **{f'R{i}': i for i in range(16)},
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }
        self.next_variable_address = 16

    def assemble(self, file_name: str):
        with open(file_name, 'r') as f:
            file_lines = f.read().split('\n')

        clean_file_lines = clean_white_spaces(file_lines)

        non_label_lines = self.first_pass(clean_file_lines)
        self.second_pass(non_label_lines)

        # print(clean_file_lines)
        # print(self.hack_lines)

        hack_file_name = file_name.replace('asm', 'hack')

        with open(hack_file_name, 'w') as f:
            for hack_line in self.hack_lines:
                f.write(hack_line + '\n')

    def first_pass(self, lines: List[str]) -> List[str]:
        non_label_lines = []

        line_number = 0

        for line in lines:
            if line.startswith('('):
                label = line[1:-1]
                self.symbol_table[label] = line_number
            else:
                non_label_lines.append(line)
                line_number += 1

        return non_label_lines

    def second_pass(self, lines: List[str]):
        for line in lines:
            if self.is_a_command(line):
                hack_line = self.a_instruction_binary(line)
            else:
                hack_line = self.c_instruction_binary(line)
            self.hack_lines.append(hack_line)

    def a_instruction_binary(self, line: str):
        value = line[1:]

        if line[1:].isnumeric():
            numeric_value = int(value)
        else:
            if value not in self.symbol_table:
                self.symbol_table[value] = self.next_variable_address
                self.next_variable_address += 1
            numeric_value = self.symbol_table[value]

        return A_COMMAND_BIN_PREFIX + format(numeric_value, "015b")

    @staticmethod
    def is_a_command(line: str):
        return line.startswith(A_COMMAND_ASM_SYMBOL)

    @staticmethod
    def c_instruction_binary(line: str):
        return CInstruction(line).hack_line()


if __name__ == '__main__':
    assembler = Assembler()

    assembler.assemble(sys.argv[1])
