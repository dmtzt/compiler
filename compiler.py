import argparse
from pathlib import Path

from compiler.files import SourceCodeFileReader
from compiler.files import IntermediateCodeFilePrinter
from compiler.parser import Parser
from compiler.intermediate_code import IntermediateCodeContainer

class InvalidFileExtensionError(RuntimeError):
    pass


def main():
    FILE_EXTENSION = '.epo'

    parser = Parser()
    file_reader = SourceCodeFileReader()
    file_printer = IntermediateCodeFilePrinter()
    arg_parser = argparse.ArgumentParser(description='Esperanto compiler')

    arg_parser.add_argument('infile', type=str, help='Input file name')
    arg_parser.add_argument('-d',
                            '--debug',
                            action='store_true',
                            help='Generate additional debug file')
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
    intermediate_code_container = parser.parse(fdata)

    if args.debug:
        named_repr_fpath = file_printer.generate_debug_file_path(fstem)
        file_printer.generate_debug_file(named_repr_fpath, intermediate_code_container)

    code_repr_fpath = file_printer.generate_intermediate_code_representation_file_path(fstem)
    file_printer.generate_intermediate_code_representation_file(code_repr_fpath, intermediate_code_container)


if __name__ == '__main__':
    main()
