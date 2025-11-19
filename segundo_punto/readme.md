## Gramatica para Producto punto de matrices

Esta gramatica permite la instancia de matrices de diferentes formas y la operacion producto punto entre matrices.
```bash
PROGRAMA -> SENTENCIAS

SENTENCIAS -> SENTENCIA SENTENCIAS'

SENTENCIAS' -> SENTENCIA SENTENCIAS'
SENTENCIAS' -> ε

SENTENCIA -> 'matriz' DECLARACION_MATRIZ
SENTENCIA -> IDENTIFICADOR SENTENCIA_ID

SENTENCIA_ID -> '=' VALOR_ASIG 

VALOR_ASIG -> IDENTIFICADOR PRODUCTO_OPC
VALOR_ASIG -> MATRIZ PRODUCTO_OPC
VALOR_ASIG -> NUMERO


PRODUCTO_OPC -> '*' OPERANDO_DER
PRODUCTO_OPC -> ε

OPERANDO_DER -> IDENTIFICADOR
OPERANDO_DER -> MATRIZ

DECLARACION_MATRIZ -> IDENTIFICADOR '=' MATRIZ 

MATRIZ -> '[' FILAS ']'

FILAS -> FILA FILAS'

FILAS' -> ',' FILA FILAS'
FILAS' -> ε

FILA -> '[' ELEMENTOS ']'

ELEMENTOS -> NUMERO ELEMENTOS'DIGITO

ELEMENTOS' -> ',' NUMERO ELEMENTOS'
ELEMENTOS -> ε

IDENTIFICADOR -> letra RESTO_ID'

RESTO_ID' -> letra RESTO_ID'
RESTO_ID' -> entero RESTO_ID'
RESTO_ID' -> '_' RESTO_ID'
RESTO_ID' -> ε

NUMERO -> entero
NUMERO -> decimal


```

# Notas
Definimos los terminales como tokens tales como entero, decimal y letra.

# Ejemplos de cadenas aceptadas
```bash
resultado = A * B
matriz M = [[1, 2], [3, 4]]
C = [[1, 0], [0, 1]] * [[5, 6], [7, 8]]
x = 42
matriz v = [[1, 2, 3]]
resultado = M * v
```