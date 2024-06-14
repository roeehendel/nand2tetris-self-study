from enums.keyword import Keyword
from enums.token_type import TokenType

SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static',
            'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this',
            'let', 'do', 'if', 'else', 'while', 'return']


class JackTokenizer:
    def __init__(self, input_file_path: str):
        with open(input_file_path, 'r') as input_file:
            raw_input_string = input_file.read()
        self._input_chars = list(self._clean_comments_and_whitespaces(raw_input_string))
        self._token_type = None
        self._token_value = None

    @staticmethod
    def _clean_comments_and_whitespaces(raw_input_string: str):
        lines = raw_input_string.split('\n')
        lines = [line.split('//')[0].strip() for line in lines]
        lines = [line for line in lines if line != '']

        # TODO: replace with better code for removing multiline comments
        raw_string = ' '.join(lines).strip()
        clean_string = ''
        i = 0
        while i < len(raw_string):
            if raw_string[i:].startswith('/*'):
                i += raw_string[i:].find('*/') + 2
            else:
                clean_string += raw_string[i]
                i = i + 1

        return clean_string

    def _remove_whitespace(self):
        self._input_chars = list(''.join(self._input_chars).strip())

    def has_more_tokens(self) -> bool:
        self._remove_whitespace()
        if len(self._input_chars) == 0:
            return False
        return True

    def advance(self):
        self._remove_whitespace()

        if self._input_chars[0].isnumeric():
            integer_constant = ''
            while self._input_chars[0].isnumeric():
                integer_constant += self._input_chars.pop(0)

            self._token_type = TokenType.INT_CONST
            self._token_value = integer_constant
        elif self._input_chars[0] == '"':
            self._input_chars.pop(0)
            string_constant = ''
            while self._input_chars[0] != '"':
                string_constant += self._input_chars.pop(0)
            self._input_chars.pop(0)

            self._token_type = TokenType.STRING_CONST
            self._token_value = string_constant
        elif self._input_chars[0] in SYMBOLS:
            self._token_type = TokenType.SYMBOL
            self._token_value = self._input_chars.pop(0)
        else:
            value = ''
            while self._input_chars[0] not in SYMBOLS + [' ']:
                value += self._input_chars.pop(0)
            if value in KEYWORDS:
                self._token_type = TokenType.KEYWORD
            else:
                self._token_type = TokenType.IDENTIFIER
            self._token_value = value

    def token_type(self) -> TokenType:
        return self._token_type

    def token_value(self) -> str:
        return self._token_value

    def keyword(self) -> Keyword:
        pass

    def symbol(self) -> str:
        pass

    def identifier(self) -> str:
        pass

    def int_value(self) -> int:
        pass

    def string_value(self) -> int:
        pass


if __name__ == '__main__':
    input_file_path = r'C:\projects\nand2tetris\projects\10\ExpressionLessSquare\SquareGame.jack'

    output_file_path = input_file_path.replace('.jack', 'TT.xml')

    tokenizer = JackTokenizer(input_file_path)

    with open(output_file_path, 'w') as output_file:
        output_file.write('<tokens>\n')

        while tokenizer.has_more_tokens():
            tokenizer.advance()
            output_file.write(
                '<{token_type}> {token_value} </{token_type}>\n'.format(
                    token_type=tokenizer.token_type().value,
                    token_value=tokenizer._token_value
                )
            )

        output_file.write('</tokens>\n')
