from enum import Enum, auto

from projects.vm_translator.vm_writer import MemorySegment


class SymbolKind(Enum):
    STATIC = auto()
    FIELD = auto()
    ARG = auto()
    VAR = auto()

    @staticmethod
    def from_string(s: str):
        return {
            'static': SymbolKind.STATIC,
            'field': SymbolKind.FIELD
        }[s]

    def memory_segment(self):
        return {
            SymbolKind.STATIC: MemorySegment.STATIC,
            SymbolKind.FIELD: MemorySegment.THIS,
            SymbolKind.ARG: MemorySegment.ARG,
            SymbolKind.VAR: MemorySegment.LOCAL,
        }[self]
