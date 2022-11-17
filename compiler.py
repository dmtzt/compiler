import argparse
from pathlib import Path

from compiler.files import FileReader
from compiler.files import FilePrinter
from compiler.parser import Parser
from compiler.quadruples import QuadrupleList

def main():
    FILE_EXTENSION = '.epo'

    parser = Parser()
    file_reader = FileReader()
    file_printer = FilePrinter()
    arg_parser = argparse.ArgumentParser(description='Esperanto compiler')

    arg_parser.add_argument('infile', type=str, help='Input file name')
    arg_parser.add_argument('-n',
                            '--names',
                            action='store_true',
                            help='Generate additional named representation file')

    args = arg_parser.parse_args()

    fname = args.infile
    fpath = file_reader.generate_file_path(fname)
    fstem = file_reader.get_file_stem(fpath)
    fsuffix = file_reader.get_file_suffix(fpath)

    if fsuffix != FILE_EXTENSION:
        raise IncorrectFileExtensionError()

    fdata = file_reader.read_file(fpath)
    quadruple_list = parser.parse(fdata)

    if args.names:
        print('Names')
        named_repr_fpath = file_printer.generate_named_representation_file_path(fstem)
        file_printer.generate_named_representation_file(named_repr_fpath, quadruple_list)

    print('Code')
    code_repr_fpath = file_printer.generate_intermediate_code_representation_file_path(fstem)
    file_printer.generate_intermediate_code_representation_file(code_repr_fpath, quadruple_list)
    # print(fpath)
    # print(fstem)
    # print(fsuffix)


class IncorrectFileExtensionError(RuntimeError):
    pass


if __name__ == '__main__':
    main()
