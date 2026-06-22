from parser import *
from prettyPrinter import *

def main():
    if len(sys.argv) < 2:
        print("Use: python lexer.py <arquivo_rust.rs>")
        exit(1)
    
    with open(sys.argv[1], 'r') as f:
        source_code = f.read()
    the_lexer = create_lexer()
    the_parser = create_parser()

    result = the_parser.parse(source_code, lexer=the_lexer)

    pretty_printer = PrettyPrinter()
    pretty_printer.visit(result)

if __name__ == '__main__':
    main()