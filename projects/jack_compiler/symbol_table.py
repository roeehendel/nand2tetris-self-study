from typing import NamedTuple

from enums.variable_type import SymbolKind


class Symbol(NamedTuple):
    symbol_type: str
    symbol_kind: SymbolKind
    index: int


class SymbolTable:
    def __init__(self):
        self._class_table = dict()
        self._subroutine_table = dict()

    def start_subroutine(self):
        self._subroutine_table = dict()

    def define(self, name: str, symbol_type: str, symbol_kind: SymbolKind):
        symbol = Symbol(symbol_type, symbol_kind, self.variable_count(symbol_kind))

        if symbol_kind in [SymbolKind.STATIC, SymbolKind.FIELD]:
            self._class_table[name] = symbol
        else:
            self._subroutine_table[name] = symbol

    def variable_count(self, symbol_kind: SymbolKind):
        if symbol_kind in [SymbolKind.STATIC, SymbolKind.FIELD]:
            table = self._class_table
        else:
            table = self._subroutine_table

        return sum([symbol.symbol_kind == symbol_kind for symbol in table.values()])

    def kind_of(self, name: str):
        return self._get_symbol(name).symbol_kind

    def type_of(self, name: str):
        return self._get_symbol(name).symbol_type

    def index_of(self, name: str):
        return self._get_symbol(name).index

    def exists(self, name: str):
        try:
            self._get_symbol(name)
        except Exception as e:
            return False
        return True

    def _get_symbol(self, name: str) -> Symbol:
        if name in self._subroutine_table:
            table = self._subroutine_table
        elif name in self._class_table:
            table = self._class_table
        else:
            raise Exception(f'Unresolved symbol: {name}')

        return table[name]
