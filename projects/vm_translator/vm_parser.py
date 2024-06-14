from command_type import CommandType


class VMParser:
    def __init__(self, input_file_path: str):
        with open(input_file_path, 'r') as f:
            self.lines = f.read().split('\n')
        self.clean_lines()

        self._command_type = None
        self._arg1 = None
        self._arg2 = None

    def clean_lines(self):
        clean_lines = map(self.clean_line, self.lines)
        self.lines = [line for line in clean_lines if line != '']

    @staticmethod
    def clean_line(line: str):
        if '//' in line:
            line = line.split('//')[0]
        return line.strip()

    def has_more_commands(self):
        return len(self.lines) > 0

    def parse_next_command(self) -> str:
        line = self.lines.pop(0)

        self._command_type = None
        self._arg1 = None
        self._arg2 = None

        command_parts = line.split(' ')

        command_type_string = command_parts[0]
        self._command_type = CommandType.from_string(command_type_string)

        if self._command_type == CommandType.ARITHMETIC:
            self._arg1 = command_type_string
        else:
            if len(command_parts) > 1:
                self._arg1 = command_parts[1]
            if len(command_parts) > 2:
                self._arg2 = command_parts[2]

        return line

    def command_type(self) -> CommandType:
        return self._command_type

    def arg1(self) -> str:
        return self._arg1

    def arg2(self) -> int:
        return self._arg2
