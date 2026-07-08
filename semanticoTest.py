from parser import *
from visitorSemantico import VisitorSemanticoFirst, VisitorSemanticoSecond


def main():
    if len(sys.argv) < 2:
        print("Use: python semanticoTest.py <arquivo.rs>")
        exit(1)

    with open(sys.argv[1], 'r') as f:
        source_code = f.read()
    the_lexer = create_lexer()
    the_parser = create_parser()

    result = the_parser.parse(source_code, lexer=the_lexer)

    visitor = VisitorSemanticoFirst()
    result.accept(visitor)

    visitor2 = VisitorSemanticoSecond(visitor.tabela)
    result.accept(visitor2)


if __name__ == '__main__':
    main()
