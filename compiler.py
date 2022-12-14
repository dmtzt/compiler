import argparse
from pathlib import Path

from compiler.files import SourceCodeFileReader
from compiler.files import IntermediateCodeFilePrinter
from compiler.parser import Parser

class InvalidFileExtensionError(RuntimeError):
    pass


def main():
    FILE_EXTENSION = '.epo'

    parser = Parser()
    file_reader = SourceCodeFileReader()
    file_printer = IntermediateCodeFilePrinter()
    arg_parser = argparse.ArgumentParser(description='Esperanto compiler')

    arg_parser.add_argument('infile', type=str, help='Input file name')
    arg_parser.add_argument('-n',
                            '--names',
                            action='store_true',
                            help='Generate additional named representation file')
    arg_parser.add_argument('-o',
                            metavar='outfile',
                            action='store',
                            help='Output file name')

    args = arg_parser.parse_args()

    fname = args.infile

    fpath = file_reader.generate_file_path(fname)
    fsuffix = file_reader.get_file_suffix(fpath)
    fstem = file_reader.get_file_stem(fpath) if not args.o else args.o

    if fsuffix != FILE_EXTENSION:
        raise InvalidFileExtensionError()

    fdata = file_reader.read_file(fpath)
    quadruple_list = parser.parse(fdata)

    if args.names:
        named_repr_fpath = file_printer.generate_named_representation_file_path(fstem)
        file_printer.generate_named_representation_file(named_repr_fpath, quadruple_list)

    code_repr_fpath = file_printer.generate_intermediate_code_representation_file_path(fstem)
    file_printer.generate_intermediate_code_representation_file(code_repr_fpath, quadruple_list)


if __name__ == '__main__':
    main()
