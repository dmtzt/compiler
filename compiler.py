import argparse

from compiler.files import FileReader
from compiler.files import FilePrinter
from compiler.parser import Parser

def main():
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

    if args.names:
        print('Names')

    print('Code')


if __name__ == '__main__':
    main()
