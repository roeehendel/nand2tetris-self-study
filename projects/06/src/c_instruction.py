class CInstruction:
    def __init__(self, line: str):
        dest, comp, jump = CInstruction._parse(line)
        self.dest = dest
        self.comp = comp
        self.jump = jump

    def hack_line(self):
        return '111' + self.comp_hack() + self.dest_hack() + self.jump_hack()

    def dest_hack(self):
        if self.dest is None:
            return '000'

        d1 = '1' if 'A' in self.dest else '0'
        d2 = '1' if 'D' in self.dest else '0'
        d3 = '1' if 'M' in self.dest else '0'

        return d1 + d2 + d3

    def comp_hack(self):
        a = '1' if 'M' in self.comp else '0'
        comp_canonized = self.comp.replace('M', 'A')
        c = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101'
        }[comp_canonized]

        return a + c

    def jump_hack(self):
        return {
            None: '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }[self.jump]

    @staticmethod
    def _parse(line):
        if '=' in line:
            dest = line.split('=')[0]
            line = line.split('=')[1]
        else:
            dest = None

        if ';' in line:
            comp = line.split(';')[0]
            line = line.split(';')[1]
            jump = line
        else:
            comp = line
            jump = None

        return dest, comp, jump
