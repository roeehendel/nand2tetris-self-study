import multiprocessing
import os
import subprocess
import sys
from pathlib import Path

EXTENSIONS = ('.tst')
SUCCESS_MESSAGE = b'End of script - Comparison ended successfully\r\n'


def test_file(file):
    # tester_program = 'HardwareSimulator.bat'
    tester_program = 'CPUEmulator.bat'
    results = subprocess.run([tester_program, file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    message = results.stdout
    error_message = results.stderr

    success = (results.stdout == SUCCESS_MESSAGE)

    if success:
        message = 'success'
    else:
        message = error_message

    return file, message


if __name__ == "__main__":
    project = sys.argv[1]

    root_dir = os.path.join(os.getcwd(), project)
    os.chdir(root_dir)

    relevant_files = []

    for subdir, dirs, files in os.walk(root_dir):
        relevant_files += [
            os.path.join(subdir, file)
            for file in files
            if os.path.splitext(file)[-1].lower() in EXTENSIONS
        ]

    # relevant_files = [file for file in relevant_files if 'Memory' not in file]
    relevant_files = [file for file in relevant_files if 'VME' not in file]

    print('Starting tests')

    with multiprocessing.Pool(16) as pool:
        results = pool.map(test_file, relevant_files)

    successful = [Path(file).stem for file, message in results if message == 'success']
    failed = [(Path(file).stem, message) for file, message in results if message != 'success']

    print()
    print(f'Successful ({len(successful)}):', ', '.join(successful))
    print('-' * 10)
    print(f'Failed ({len(failed)}):')
    for file, error_message in failed:
        print(file, error_message)
