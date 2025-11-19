from antlr4 import *
import sys
from MatrizProductoLexer import MatrizProductoLexer
from MatrizProductoParser import MatrizProductoParser
from EvaluadorMatricesVisitor import EvaluadorMatricesVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Leer desde archivo
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
    else:
        print("Uso: python main.py <archivo>")
        print("O ingrese la cadena directamente:")
        input_text = input("> ")
        input_stream = InputStream(input_text)
    
    # Análisis léxico
    lexer = MatrizProductoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Análisis sintáctico
    parser = MatrizProductoParser(stream)
    tree = parser.programa()
    
    # Verificar errores sintácticos
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\n✗ Se encontraron {parser.getNumberOfSyntaxErrors()} errores sintácticos")
        sys.exit(1)
    else:
        print("✓ Análisis sintáctico exitoso\n")
    
    # Mostrar árbol de parseo (opcional)
    print("--- ÁRBOL DE PARSEO ---")
    print(tree.toStringTree(recog=parser))
    print()
    
    # Evaluación semántica con el Visitor
    try:
        evaluador = EvaluadorMatricesVisitor()
        evaluador.visit(tree)
        
        # Mostrar tabla de símbolos final
        evaluador.mostrar_tabla_simbolos()
        
    except Exception as e:
        print(f"\n✗ Error de evaluación: {e}")
        sys.exit(1)