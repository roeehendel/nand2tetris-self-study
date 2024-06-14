from enum import Enum
from typing import IO


class MemorySegment(Enum):
    CONST = 'constant'
    ARG = 'argument'
    LOCAL = 'local'
    STATIC = 'static'
    THIS = 'this'
    THAT = 'that'
    POINTER = 'pointer'
    TEMP = 'temp'


class ArithmeticCommand(Enum):
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ = 'eq'
    GT = 'gt'
    LT = 'lt'
    AND = 'and'
    OR = 'or'
    NOT = 'not'
    MULTIPLY = 'call Math.multiply 2'
    DIVIDE = 'call Math.divide 2'

    @staticmethod
    def from_string(s: str):
        return {
            '+': ArithmeticCommand.ADD,
            '-': ArithmeticCommand.SUB,
            '=': ArithmeticCommand.EQ,
            '>': ArithmeticCommand.GT,
            '<': ArithmeticCommand.LT,
            '&': ArithmeticCommand.AND,
            '|': ArithmeticCommand.OR,
            '*': ArithmeticCommand.MULTIPLY,
            '/': ArithmeticCommand.DIVIDE,
        }[s]

    @staticmethod
    def from_string_unary(s: str):
        return {
            '-': ArithmeticCommand.NEG,
            '~': ArithmeticCommand.NOT,
        }[s]


class VMWriter:
    def __init__(self, output_file: IO):
        self._output_file = output_file

    def write_push(self, segment: MemorySegment, index: int):
        self._write(f'push {segment.value} {index}')

    def write_pop(self, segment: MemorySegment, index: int):
        self._write(f'pop {segment.value} {index}')

    def write_arithmetic(self, arithmetic_command: ArithmeticCommand):
        self._write(arithmetic_command.value)

    def write_label(self, label: str):
        self._write(f'label {label}')

    def write_goto(self, label: str):
        self._write(f'goto {label}')

    def write_if(self, label: str):
        self._write(f'if-goto {label}')

    def write_call(self, name: str, n_argument: int):
        self._write(f'call {name} {n_argument}')

    def write_function(self, name: str, n_locals: int):
        self._write(f'function {name} {n_locals}')

    def write_return(self):
        self._write(f'return')

    def _write(self, line: str):
        self._output_file.write(f'{line}\n')
