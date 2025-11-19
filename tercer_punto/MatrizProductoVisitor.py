# Generated from MatrizProducto.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MatrizProductoParser import MatrizProductoParser
else:
    from MatrizProductoParser import MatrizProductoParser

# This class defines a complete generic visitor for a parse tree produced by MatrizProductoParser.

class MatrizProductoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatrizProductoParser#programa.
    def visitPrograma(self, ctx:MatrizProductoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#sentencias.
    def visitSentencias(self, ctx:MatrizProductoParser.SentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#sentencia.
    def visitSentencia(self, ctx:MatrizProductoParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#sentenciaId.
    def visitSentenciaId(self, ctx:MatrizProductoParser.SentenciaIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#valorAsig.
    def visitValorAsig(self, ctx:MatrizProductoParser.ValorAsigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#productoOpc.
    def visitProductoOpc(self, ctx:MatrizProductoParser.ProductoOpcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#operandoDer.
    def visitOperandoDer(self, ctx:MatrizProductoParser.OperandoDerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#declaracionMatriz.
    def visitDeclaracionMatriz(self, ctx:MatrizProductoParser.DeclaracionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#matriz.
    def visitMatriz(self, ctx:MatrizProductoParser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#filas.
    def visitFilas(self, ctx:MatrizProductoParser.FilasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#fila.
    def visitFila(self, ctx:MatrizProductoParser.FilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#elementos.
    def visitElementos(self, ctx:MatrizProductoParser.ElementosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#identificador.
    def visitIdentificador(self, ctx:MatrizProductoParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrizProductoParser#numero.
    def visitNumero(self, ctx:MatrizProductoParser.NumeroContext):
        return self.visitChildren(ctx)



del MatrizProductoParser