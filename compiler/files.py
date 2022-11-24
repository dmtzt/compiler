import json

from pathlib import Path
from .quadruples import QuadrupleList
from .intermediate_code import IntermediateCodeContainer

class SourceCodeFileReader:
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


class IntermediateCodeFilePrinter:
    def generate_debug_file(self, fpath: Path, intermediate_code_container: IntermediateCodeContainer) -> None:
        quadruple_list = intermediate_code_container.get_quadruple_list()
        quadruples = quadruple_list.get_quadruples()

        with open(fpath,'w',encoding = 'utf-8') as f:
            for count, quadruple in enumerate(quadruples):
                f.write(f'{count : < 5}{quadruple.get_debug_representation()}')
                f.write('\n')


    def generate_intermediate_code_representation_file(self, fpath: Path, intermediate_code_container: IntermediateCodeContainer) -> None:
        intermediate_code_representation = intermediate_code_container.get_json_obj()

        with open(fpath,'w',encoding = 'utf-8') as f:
            f.write(intermediate_code_representation)
            f.write('\n')

    
    def generate_debug_file_path(self, fstem: str) -> Path:
        fname = f'{fstem}.debug'
        return Path().absolute() / fname


    def generate_intermediate_code_representation_file_path(self, fstem: str) -> Path:
        fname = f'{fstem}.obj'
        return Path().absolute() / fname


class IntermediateCodeFileReader:
    def read_file(self, fpath: Path) -> str:
        if not fpath.is_file():
            raise FileNotFoundError()

        with open(fpath) as f:
            data = json.load(f)
            return obj
        
    
    def generate_file_path(self, fname: str) -> Path:
        return Path().absolute() / fname


    def get_file_suffix(self, fpath: Path) -> str:
        return fpath.suffix


class FileNotFoundError(RuntimeError):
    pass