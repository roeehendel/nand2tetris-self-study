from typing import List

COMMENT_START = '//'


def is_empty_line(line: str):
    if line == '':
        return True
    if line.startswith(COMMENT_START):
        return True
    return False


def clean_line(line: str):
    return line.split(COMMENT_START)[0].strip()


def clean_white_spaces(file_lines: List[str]):
    lines_stripped = [line.strip() for line in file_lines]
    lines_without_empty_lines = [line for line in lines_stripped if not is_empty_line(line)]
    lines_cleaned = [clean_line(line) for line in lines_without_empty_lines]
    
    return lines_cleaned
