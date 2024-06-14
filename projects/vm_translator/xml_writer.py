from typing import IO
from xml.sax.saxutils import escape


def write_xml(tag_name):
    def decorator(f):
        def wrapper(self, *args, **kwargs):
            self.xml_writer.open_tag(tag_name)
            f(self, *args, **kwargs)
            self.xml_writer.close_tag(tag_name)

        return wrapper

    return decorator


class XMLWriter:
    def __init__(self, output_file: IO):
        self._output_file = output_file
        self._indentation = 0

    def open_tag(self, tag_name: str):
        self._output_file.write(' ' * self._indentation)
        self._output_file.write(f'<{tag_name}>\n')
        self._indentation += 4

    def close_tag(self, tag_name: str):
        self._indentation -= 4
        self._output_file.write(' ' * self._indentation)
        self._output_file.write(f'</{tag_name}>\n')

    def write_terminal(self, tag_name: str, terminal_value: str):
        self._output_file.write(' ' * self._indentation)
        self._output_file.write(f'<{tag_name}>')
        self._output_file.write(f'{escape(terminal_value)}')
        self._output_file.write(f'</{tag_name}>\n')
