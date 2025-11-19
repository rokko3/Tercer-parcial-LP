from MatrizProductoVisitor import MatrizProductoVisitor
from MatrizProductoParser import MatrizProductoParser
import numpy as np

class EvaluadorMatricesVisitor(MatrizProductoVisitor):

    def __init__(self):
        self.variables = {}  
        self.nivel_indentacion = 0
    
    def _print(self, mensaje, nivel=None):
        if nivel is None:
            nivel = self.nivel_indentacion
        print("  " * nivel + mensaje)
    
    def visitPrograma(self, ctx: MatrizProductoParser.ProgramaContext):

        resultado = self.visit(ctx.sentencias())
        return resultado
    
    def visitSentencias(self, ctx: MatrizProductoParser.SentenciasContext):

        # Visitar la primera sentencia
        if ctx.sentencia():
            resultado_sentencia = self.visit(ctx.sentencia())
            
        if ctx.sentencias():
            resultado_siguiente = self.visit(ctx.sentencias())
            
        return None
    
    def visitSentencia(self, ctx: MatrizProductoParser.SentenciaContext):

        if ctx.MATRIZ_LITERAL():
            return self.visit(ctx.declaracionMatriz())
        else:
            # Asignación: B = A * A
            identificador = ctx.identificador().getText()
            self._print(f"Asignacion: {identificador}", 0)
            self.nivel_indentacion += 1
            valor = self.visit(ctx.sentenciaId())
            self.nivel_indentacion -= 1
            self.variables[identificador] = valor
            

            self._print(f"{identificador} = ", 0)
            self._imprimir_matriz(valor, 1)
            print()
            return valor
    
    def visitDeclaracionMatriz(self, ctx: MatrizProductoParser.DeclaracionMatrizContext):
        nombre = ctx.identificador().getText()
        self._print(f"Declaracion de matriz: {nombre}", 0)
        self.nivel_indentacion += 1
        matriz = self.visit(ctx.matriz())
        self.nivel_indentacion -= 1
        self.variables[nombre] = matriz
        
        self._print(f"matriz {nombre} = ", 0)
        self._imprimir_matriz(matriz, 1)
        print()
        return matriz
    
    def visitSentenciaId(self, ctx: MatrizProductoParser.SentenciaIdContext):
        return self.visit(ctx.valorAsig())
    
    def visitValorAsig(self, ctx: MatrizProductoParser.ValorAsigContext):
        if ctx.identificador():
            # Variable
            nombre = ctx.identificador().getText()
            if nombre not in self.variables:
                raise Exception(f" Variable '{nombre}' no definida")
            valor = self.variables[nombre]
            
            # Verificar producto
            if ctx.productoOpc() and ctx.productoOpc().ASTERISCO():
                operando_der = self.visit(ctx.productoOpc())
                return self._producto_matrices(valor, operando_der)
            return valor
            
        elif ctx.matriz():
            # Matriz literal
            matriz = self.visit(ctx.matriz())
            
            # Verificar producto
            if ctx.productoOpc() and ctx.productoOpc().ASTERISCO():
                operando_der = self.visit(ctx.productoOpc())
                return self._producto_matrices(matriz, operando_der)
            return matriz
            
        elif ctx.numero():
            # Número escalar
            return self.visit(ctx.numero())
    
    def visitProductoOpc(self, ctx: MatrizProductoParser.ProductoOpcContext):
        if ctx.ASTERISCO():
            self._print("Operador: *")
            return self.visit(ctx.operandoDer())
        return None
    
    def visitOperandoDer(self, ctx: MatrizProductoParser.OperandoDerContext):
      
        if ctx.identificador():
            nombre = ctx.identificador().getText()
            if nombre not in self.variables:
                raise Exception(f"Variable '{nombre}' no definida")
            valor = self.variables[nombre]
            self._print(f"Operando derecho: '{nombre}' ({valor.shape[0]}x{valor.shape[1]})")
            return valor
        elif ctx.matriz():
            self._print("Operando derecho: matriz literal")
            return self.visit(ctx.matriz())
    
    def visitMatriz(self, ctx: MatrizProductoParser.MatrizContext):
        filas = self.visit(ctx.filas())
        matriz = np.array(filas)
        self._print(f"Matriz creada: {matriz.shape[0]}x{matriz.shape[1]}")
        return matriz
    
    def visitFilas(self, ctx: MatrizProductoParser.FilasContext):

        filas = []
        for fila_ctx in ctx.fila():
            fila = self.visit(fila_ctx)
            filas.append(fila)
        return filas
    
    def visitFila(self, ctx: MatrizProductoParser.FilaContext):
        return self.visit(ctx.elementos())
    
    def visitElementos(self, ctx: MatrizProductoParser.ElementosContext):
        elementos = []
        for numero_ctx in ctx.numero():
            numero = self.visit(numero_ctx)
            elementos.append(numero)
        return elementos
    
    def visitIdentificador(self, ctx: MatrizProductoParser.IdentificadorContext):
        return ctx.getText()
    
    def visitNumero(self, ctx: MatrizProductoParser.NumeroContext):
        if ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        elif ctx.ENTERO():
            return float(ctx.ENTERO().getText())
    
    def _producto_matrices(self, A, B):
        try:

            
            self._print(f"Matriz A: dimension {A.shape[0]}x{A.shape[1]}")
            self._imprimir_matriz(A, self.nivel_indentacion + 1)
            
            self._print(f"Matriz B: dimension {B.shape[0]}x{B.shape[1]}")
            self._imprimir_matriz(B, self.nivel_indentacion + 1)
            
            # Calcular producto
            resultado = np.dot(A, B)

            self._print(f"RESULTADO {resultado.shape[0]}x{resultado.shape[1]}")
            self._imprimir_matriz(resultado, self.nivel_indentacion + 1)
            
            return resultado
        except ValueError as e:
            raise Exception(f"\nDimensiones incompatibles: {A.shape} × {B.shape}")
    
    def _imprimir_matriz(self, matriz, nivel=0):
        if isinstance(matriz, np.ndarray):
            self._print("[", nivel)
            for i, fila in enumerate(matriz):
                # Formatear elementos
                elementos_str = []
                for x in fila:
                    if x == int(x):  # Si es entero
                        elementos_str.append(f"{int(x):6d}")
                    else:  # Si es decimal
                        elementos_str.append(f"{x:6.2f}")
                
                contenido = ", ".join(elementos_str)
                if i < len(matriz) - 1:
                    self._print(f"  [{contenido}],", nivel)
                else:
                    self._print(f"  [{contenido}]", nivel)
            self._print("]", nivel)
        else:
            self._print(str(matriz), nivel)
    
    def mostrar_tabla_simbolos(self):
        print("SIMBOLOS")
        
        if not self.variables:
            self._print("(vacía)", 1)
        else:
            for i, (nombre, matriz) in enumerate(self.variables.items(), 1):
                shape = matriz.shape if isinstance(matriz, np.ndarray) else "escalar"
                self._print(f"[{i}] {nombre}: matriz {shape}", 0)
                self._imprimir_matriz(matriz, 1)
                if i < len(self.variables):
                    print()
