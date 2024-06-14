import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from os import PathLike
from typing import Union

EXTENSIONS = ('.hdl')

def zip_dir(zip_name: str, source_dir: Union[str, PathLike]):
    src_path = Path(source_dir).expanduser().resolve(strict=True)
    with ZipFile(zip_name, 'w', ZIP_DEFLATED) as zf:
        for file in src_path.rglob('*.hdl'):
            zf.write(file, file.relative_to(src_path))

if __name__ == "__main__":
	project = sys.argv[1]

	rootdir = os.getcwd()

	rootdir = os.path.join(os.getcwd(), project)
	os.chdir(rootdir)

	zip_dir('project1.zip', rootdir)
