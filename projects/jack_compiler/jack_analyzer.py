import os.path
import sys

from compilation_engine import CompilationEngine
from jack_tokenizer import JackTokenizer


class JackAnalyzer:
    def __init__(self, source: str):
        if os.path.isdir(source):
            self._input_file_paths = [
                os.path.join(source, file_name)
                for file_name in os.listdir(source)
                if file_name.endswith('.jack')
            ]
        else:
            self._input_file_paths = [source]

    def run(self):
        for input_file_path in self._input_file_paths:
            tokenizer = JackTokenizer(input_file_path)

            output_file_path = input_file_path.replace('.jack', '.vm')
            with open(output_file_path, 'w') as output_file:
                compilation_engine = CompilationEngine(tokenizer, output_file)
                compilation_engine.compile_class()


if __name__ == '__main__':
    jack_analyzer = JackAnalyzer(sys.argv[1])
    jack_analyzer.run()
