from pathlib import Path
from .quadruples import QuadrupleList

class FileReader:
    def __init__(self) -> None:
        pass


    def generate_file_path(self, fname: str) -> str:
        return Path(fname)


    def get_file_stem(self, fpath: Path) -> str:
        return fpath.stem

    
    def get_file_suffix(self, fpath: Path) -> str:
        return fpath.suffix


    def read_file(self, fpath: Path) -> str:
        if not fpath.is_file():
            raise FileNotFoundError()

        with open(fpath) as f:
            return '\n'.join(line.rstrip() for line in f)


class FilePrinter:
    def __init__(self) -> None:
        pass


    def generate_named_representation_file(self, fpath: Path, quadruple_list: QuadrupleList) -> None:
        quadruples = quadruple_list.get_quadruples()

        with open(fpath,'w',encoding = 'utf-8') as f:
            for count, quadruple in enumerate(quadruples):
                f.write(f'{count : < 5}{quadruple.get_named_representation()}\n')

    
    def generate_intermediate_code_representation_file(self, fpath: Path, quadruple_list: QuadrupleList) -> None:
        quadruples = quadruple_list.get_quadruples()

        with open(fpath,'w',encoding = 'utf-8') as f:
            for quadruple in quadruples:
                f.write(quadruple.get_intermediate_code_representation())
                f.write('\n')

    
    def generate_named_representation_file_path(self, fstem: str) -> Path:
        fname = f'{fstem}.names'
        return Path().absolute() / fname


    def generate_intermediate_code_representation_file_path(self, fstem: str) -> Path:
        fname = f'{fstem}.obj'
        return Path().absolute() / fname


class FileNotFoundError(RuntimeError):
    pass