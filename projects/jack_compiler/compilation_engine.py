from pathlib import Path
from typing import IO, List, Union, Callable, Optional

from enums.variable_type import SymbolKind
from jack_tokenizer import JackTokenizer
from projects.vm_translator.vm_writer import VMWriter, MemorySegment, ArithmeticCommand
from symbol_table import SymbolTable


class CompilationEngine:
    def __init__(self, tokenizer: JackTokenizer, output_file: IO):
        self._tokenizer = tokenizer
        self._output_file = output_file
        self._reached_end_of_file = False
        self._tokenizer.advance()
        self._symbol_table = SymbolTable()
        self._vm_writer = VMWriter(output_file)
        self._class_name = None
        self._label_index = 0

    def compile_class(self):
        self._eat_token('class')
        self._class_name = self._eat_token()

        self._eat_token('{')

        while self._current_token() in ['static', 'field']:
            self.compile_class_var_dec()

        while self._current_token() in ['constructor', 'function', 'method']:
            self.compile_subroutine_dec()

        self._eat_token('}')

    def compile_class_var_dec(self):
        vars_kind = self._eat_token()
        vars_type = self._eat_token()
        var_names = self._compile_comma_seperated_list(self._compile_var_dec_item)

        for var_name in var_names:
            self._symbol_table.define(var_name, vars_type, SymbolKind.from_string(vars_kind))

        self._eat_token(';')

    def _compile_var_dec_item(self):
        return self._eat_token()

    def compile_subroutine_dec(self):
        self._symbol_table.start_subroutine()

        subroutine_type = self._eat_token()
        return_type = self._eat_token()
        subroutine_name = self._eat_token()

        if subroutine_type == 'method':
            self._symbol_table.define('this', self._class_name, SymbolKind.ARG)

        self._eat_token('(')
        self.compile_parameter_list()
        self._eat_token(')')

        self._eat_token('{')

        while self._current_token() == 'var':
            self.compile_var_dec()

        n_locals = self._symbol_table.variable_count(SymbolKind.VAR)
        self._vm_writer.write_function(f'{self._class_name}.{subroutine_name}', n_locals)

        if subroutine_type == 'constructor':
            n_fields = self._symbol_table.variable_count(SymbolKind.FIELD)
            self._vm_writer.write_push(MemorySegment.CONST, n_fields)
            self._vm_writer.write_call('Memory.alloc', 1)
            self._vm_writer.write_pop(MemorySegment.POINTER, 0)

            # TODO: make sure this code is ok
            # self._symbol_table.define('this', '', SymbolKind.VAR)
            # index = self._symbol_table.index_of('this')
            # self._vm_writer.write_push(MemorySegment.POINTER, 0)
            # self._vm_writer.write_pop(MemorySegment.LOCAL, index)

        elif subroutine_type == 'method':
            self._vm_writer.write_push(MemorySegment.ARG, 0)
            self._vm_writer.write_pop(MemorySegment.POINTER, 0)

        self.compile_statements()

        self._eat_token('}')

    def compile_parameter_list(self):
        if self._current_token() != ')':
            parameters = self._compile_comma_seperated_list(self._compile_parameter_list_item)
            for parameter_type, parameter_name in parameters:
                self._symbol_table.define(parameter_name, parameter_type, SymbolKind.ARG)

    def _compile_parameter_list_item(self):
        parameter_type = self._eat_token()
        parameter_name = self._eat_token()
        return parameter_type, parameter_name

    def compile_var_dec(self):
        self._eat_token('var')
        vars_type = self._eat_token()
        vars_names = self._compile_comma_seperated_list(self._compile_var_dec_item)
        self._eat_token(';')

        for var_name in vars_names:
            self._symbol_table.define(var_name, vars_type, SymbolKind.VAR)

    def compile_statements(self):
        while self._current_token() in ['let', 'if', 'while', 'do', 'return']:
            if self._current_token() == 'let':
                self.compile_let_statement()
            elif self._current_token() == 'if':
                self.compile_if_statement()
            elif self._current_token() == 'while':
                self.compile_while_statement()
            elif self._current_token() == 'do':
                self.compile_do_statement()
            elif self._current_token() == 'return':
                self.compile_return_statement()

    def compile_let_statement(self):
        self._eat_token('let')
        var_name = self._eat_token()

        array_assignment = False

        if self._current_token() == '[':
            array_assignment = True
            array_name = var_name

            self._push_variable(array_name)

            self._eat_token('[')
            self.compile_expression()
            self._eat_token(']')

            self._vm_writer.write_arithmetic(ArithmeticCommand.ADD)
            self._vm_writer.write_pop(MemorySegment.TEMP, 1)

        self._eat_token('=')

        self.compile_expression()
        self._eat_token(';')

        if array_assignment:
            self._vm_writer.write_push(MemorySegment.TEMP, 1)
            self._vm_writer.write_pop(MemorySegment.POINTER, 1)
            self._vm_writer.write_pop(MemorySegment.THAT, 0)
        else:
            self._pop_variable(var_name)

    def compile_if_statement(self):
        self._label_index += 1
        else_label = f'ELSE_{self._label_index}'
        end_label = f'END_IF_{self._label_index}'

        self._eat_token('if')
        self._eat_token('(')
        self.compile_expression()
        self._eat_token(')')

        self._vm_writer.write_arithmetic(ArithmeticCommand.NOT)
        self._vm_writer.write_if(else_label)

        self._eat_token('{')
        self.compile_statements()
        self._eat_token('}')

        self._vm_writer.write_goto(end_label)

        self._vm_writer.write_label(else_label)
        if self._current_token() == 'else':
            self._eat_token('else')
            self._eat_token('{')
            self.compile_statements()
            self._eat_token('}')

        self._vm_writer.write_label(end_label)

    def compile_while_statement(self):
        self._label_index += 1
        loop_label = f'WHILE_{self._label_index}'
        end_label = f'END_WHILE_{self._label_index}'

        self._vm_writer.write_label(loop_label)

        self._eat_token('while')
        self._eat_token('(')
        self.compile_expression()
        self._eat_token(')')

        self._vm_writer.write_arithmetic(ArithmeticCommand.NOT)
        self._vm_writer.write_if(end_label)

        self._eat_token('{')
        self.compile_statements()
        self._eat_token('}')

        self._vm_writer.write_goto(loop_label)

        self._vm_writer.write_label(end_label)

    def compile_do_statement(self):
        self._eat_token('do')
        self.compile_subroutine_call()
        self._vm_writer.write_pop(MemorySegment.TEMP, 0)  # discard void return value
        self._eat_token(';')

    def compile_subroutine_call(self):
        first_token = self._eat_token()
        self._compile_subroutine_call_without_first_token(first_token)

    def _compile_subroutine_call_without_first_token(self, first_token):
        n_arguments = 0

        if self._current_token() == '.':
            self._eat_token('.')
            if self._symbol_table.exists(first_token):
                object_name = first_token
                object_type = self._symbol_table.type_of(first_token)

                self._push_variable(object_name)

                n_arguments = 1
            else:
                object_type = first_token

            method_name = f'{object_type}.{self._eat_token()}'
        else:
            n_arguments = 1
            self._vm_writer.write_push(MemorySegment.POINTER, 0)
            method_name = f'{self._class_name}.{first_token}'

        self._eat_token('(')
        n_arguments += self.compile_expression_list()
        self._eat_token(')')

        self._vm_writer.write_call(method_name, n_arguments)

    def compile_expression_list(self):
        if self._current_token() != ')':
            return len(self._compile_comma_seperated_list(self.compile_expression))
        return 0

    def compile_return_statement(self):
        self._eat_token('return')
        if self._current_token() != ';':
            if self._current_token() == 'this':
                self._eat_token()
                self._vm_writer.write_push(MemorySegment.POINTER, 0)
            else:
                self.compile_expression()
        else:
            self._vm_writer.write_push(MemorySegment.CONST, 0)  # void return value
        self._eat_token(';')

        self._vm_writer.write_return()

    def _compile_comma_seperated_list(self, compile_list_item: Callable):
        items = []

        items.append(compile_list_item())

        while self._current_token() == ',':
            self._eat_token(',')
            items.append(compile_list_item())

        return items

    def compile_expression(self):
        self.compile_term()
        if self._current_token() in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
            operator = self._eat_token()
            self.compile_term()
            self._vm_writer.write_arithmetic(ArithmeticCommand.from_string(operator))

        return 'expression'

    def compile_term(self):
        if self._current_token() in ['-', '~']:
            unary_operator = self._eat_token()
            self.compile_term()
            self._vm_writer.write_arithmetic(ArithmeticCommand.from_string_unary(unary_operator))
        elif self._current_token() == '(':
            self._eat_token('(')
            self.compile_expression()
            self._eat_token(')')
        else:
            first_token = self._eat_token()

            if self._current_token() == '[':
                array_name = first_token
                self._push_variable(array_name)

                self._eat_token('[')
                self.compile_expression()
                self._eat_token(']')

                self._vm_writer.write_arithmetic(ArithmeticCommand.ADD)
                self._vm_writer.write_pop(MemorySegment.POINTER, 1)

                self._vm_writer.write_push(MemorySegment.THAT, 0)
            elif self._current_token() in ['(', '.']:
                self._compile_subroutine_call_without_first_token(first_token)
            elif first_token.isnumeric():
                self._vm_writer.write_push(MemorySegment.CONST, int(first_token))
            elif first_token in ['true', 'false', 'null']:
                if first_token == 'true':
                    self._vm_writer.write_push(MemorySegment.CONST, 1)
                    self._vm_writer.write_arithmetic(ArithmeticCommand.NEG)
                else:
                    self._vm_writer.write_push(MemorySegment.CONST, 0)
            elif self._symbol_table.exists(first_token):
                var_kind = self._symbol_table.kind_of(first_token)
                var_index = self._symbol_table.index_of(first_token)
                self._vm_writer.write_push(var_kind.memory_segment(), var_index)
            else:
                string_constant = first_token

                self._vm_writer.write_push(MemorySegment.CONST, len(string_constant))
                self._vm_writer.write_call('String.new', 1)
                self._vm_writer.write_pop(MemorySegment.TEMP, 0)

                for c in string_constant:
                    self._vm_writer.write_push(MemorySegment.TEMP, 0)
                    self._vm_writer.write_push(MemorySegment.CONST, ord(c))
                    self._vm_writer.write_call('String.appendChar', 2)

                self._vm_writer.write_push(MemorySegment.TEMP, 0)

    def _push_variable(self, var_name: str):
        var_kind = self._symbol_table.kind_of(var_name)
        var_index = self._symbol_table.index_of(var_name)
        self._vm_writer.write_push(var_kind.memory_segment(), var_index)

    def _pop_variable(self, var_name: str):
        var_kind = self._symbol_table.kind_of(var_name)
        var_index = self._symbol_table.index_of(var_name)
        self._vm_writer.write_pop(var_kind.memory_segment(), var_index)

    def _current_token(self):
        self._verify_not_eof()
        return self._tokenizer.token_value()

    def _eat_token(self, expected_token: Optional[str] = None):
        token_value = self._current_token()
        token_type = self._tokenizer.token_type()

        if expected_token is not None and token_value != expected_token:
            self._raise_unexpected_token(token_value, expected_token)

        if self._tokenizer.has_more_tokens():
            self._tokenizer.advance()
        else:
            self._reached_end_of_file = True

        return token_value

    def _verify_not_eof(self):
        if self._reached_end_of_file:
            raise Exception(f'Unexpected EOF')

    def _raise_unexpected_token(self, token: str, expected_tokens: Union[str, List[str]]):
        print(self._tokenizer._input_chars)
        raise Exception(
            f'Unexpected token in file {Path(self._output_file.name).stem}. Got: {token}, expected: {expected_tokens}'
        )
