grammar MatrizProducto;

programa
    : sentencias EOF
    ;

sentencias
    : sentencia sentencias
    | sentencia
    ;

sentencia
    : MATRIZ_LITERAL declaracionMatriz
    | identificador sentenciaId
    ;

sentenciaId
    : IGUAL valorAsig
    ;

valorAsig
    : identificador productoOpc
    | matriz productoOpc
    | numero
    ;

productoOpc
    : ASTERISCO operandoDer
    |
    ;

operandoDer
    : identificador
    | matriz
    ;

declaracionMatriz
    : identificador IGUAL matriz
    ;

matriz
    : LCORCHETE filas RCORCHETE
    ;

filas
    : fila (COMA fila)*
    ;

fila
    : LCORCHETE elementos RCORCHETE
    ;

elementos
    : numero (COMA numero)*
    ;

identificador
    : IDENTIFICADOR
    ;

numero
    : ENTERO
    | DECIMAL
    ;

// Tokens
MATRIZ_LITERAL : 'matriz' ;
IGUAL      : '=' ;
ASTERISCO  : '*' ;
LCORCHETE  : '[' ;
RCORCHETE  : ']' ;
COMA       : ',' ;

IDENTIFICADOR
    : LETRA (LETRA | DIGITO | '_')*
    ;

DECIMAL
    : '-'? DIGITO+ '.' DIGITO+
    ;

ENTERO
    : '-'? DIGITO+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

// Fragmentos (no generan tokens, solo se usan en definiciones)
fragment LETRA
    : [a-zA-Z]
    ;

fragment DIGITO
    : [0-9]
    ;
