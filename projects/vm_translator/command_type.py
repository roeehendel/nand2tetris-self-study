from enum import Enum, auto

ARITHMETIC_COMMANDS_STRINGS = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']


class CommandType(Enum):
    ARITHMETIC = auto()
    PUSH = auto()
    POP = auto()
    LABEL = auto()
    GOTO = auto()
    IF_GOTO = auto()
    FUNCTION = auto()
    RETURN = auto()
    CALL = auto()

    @staticmethod
    def from_string(command_type_string: str):
        if command_type_string in ARITHMETIC_COMMANDS_STRINGS:
            return CommandType.ARITHMETIC

        return {
            'push': CommandType.PUSH,
            'pop': CommandType.POP,
            'label': CommandType.LABEL,
            'goto': CommandType.GOTO,
            'if-goto': CommandType.IF_GOTO,
            'function': CommandType.FUNCTION,
            'return': CommandType.RETURN,
            'call': CommandType.CALL
        }[command_type_string]
