from antlr4 import *
import sys
from MatrizProductoLexer import MatrizProductoLexer
from MatrizProductoParser import MatrizProductoParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Leer desde archivo
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
    else:
        print("Uso: python main.py <archivo>")
        print("O ingrese la cadena directamente:")
        input_text = input("> ")
        input_stream = InputStream(input_text)
    
    lexer = MatrizProductoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    parser = MatrizProductoParser(stream)
    tree = parser.programa()
    
    
    print(tree.toStringTree(recog=parser))

    # mostrar errores sintacticos
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\n Se encontraron {parser.getNumberOfSyntaxErrors()} errores sintacticos")
    else:
        print("\n Analisis sintactico exitoso")