from pathlib import Path
from .quadruples import QuadrupleList

class FileReader:
    def __init__(self) -> None:
        pass

    def read_file(file_path: Path) -> str:
        with open(file_path) as f:
            return '\n'.join(line.rstrip() for line in f)


class FilePrinter:
    def __init__(self) -> None:
        pass

    def generate_named_representation_file(self, quadruple_list: QuadrupleList, fname: str) -> None:
        quadruples = quadruple_list.get_quadruples()

        with open(fname,'w',encoding = 'utf-8') as f:
            for count, quadruple in enumerate(quadruples):
                f.write(f'{count : < 5}{quadruple.get_named_representation()}\n')

    
    def generate_intermediate_code_representation_file(self, quadruple_list: QuadrupleList, fname: str) -> None:
        quadruples = quadruple_list.get_quadruples()

        with open(fname,'w',encoding = 'utf-8') as f:
            for quadruple in quadruples:
                f.write(quadruple.get_intermediate_code_representation())
                f.write('\n')