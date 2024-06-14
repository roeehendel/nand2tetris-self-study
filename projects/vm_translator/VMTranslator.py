import os.path
import sys
from pathlib import Path

from code_writer import CodeWriter
from command_type import CommandType
from vm_parser import VMParser


class VMTranslator:
    def __init__(self, input_path: str):
        if os.path.isdir(input_path):
            self.input_files_paths = [os.path.join(input_path, file_name) for file_name in os.listdir(input_path) if
                                      file_name.split('.')[1] == 'vm']
            output_file_path = f'{input_path}/{os.path.basename(input_path)}.asm'
        else:
            self.input_files_paths = [input_path]
            output_file_path = input_path.replace('vm', 'asm')

        self.code_writer = CodeWriter(output_file_path)

    def translate(self):
        self.code_writer.write_init()
        self.code_writer.write_empty_line()

        for input_file_path in self.input_files_paths:
            self._translate_single_file(input_file_path)

        self.code_writer.close()

    def _translate_single_file(self, input_file_path: str):
        vm_parser = VMParser(input_file_path)
        self.code_writer.set_current_file(Path(input_file_path).stem)

        while vm_parser.has_more_commands():
            vm_line = vm_parser.parse_next_command()

            self.code_writer.write_comment(vm_line)

            command_type = vm_parser.command_type()
            arg1 = vm_parser.arg1()
            arg2 = vm_parser.arg2()

            if command_type == CommandType.ARITHMETIC:
                self.code_writer.write_arithmetic(arg1)
            elif command_type in [CommandType.PUSH, CommandType.POP]:
                self.code_writer.write_push_pop(command_type, segment=arg1, index=arg2)
            elif command_type == CommandType.LABEL:
                self.code_writer.write_label(arg1)
            elif command_type == CommandType.GOTO:
                self.code_writer.write_goto(arg1)
            elif command_type == CommandType.IF_GOTO:
                self.code_writer.write_if_goto(arg1)
            elif command_type == CommandType.FUNCTION:
                self.code_writer.write_function(arg1, int(arg2))
            elif command_type == CommandType.RETURN:
                self.code_writer.write_return()
            elif command_type == CommandType.CALL:
                self.code_writer.write_call(arg1, arg2)

            self.code_writer.write_empty_line()


if __name__ == '__main__':
    file_path = sys.argv[1]
    vm_translator = VMTranslator(file_path)
    vm_translator.translate()
