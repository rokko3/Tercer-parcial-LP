# Gramatica para un lenguaje CRUD
```
S -> SELECT_STMT 
S -> INSERT_STMT
S -> UPDATE_STMT
S -> DELETE_STMT
#SELECT columnas FROM tabla 

SELECT_STMT -> SELECT COLS FROM ID WHERE_CLAUSE

COLS -> ASTERISCO
COLS -> COL_LIST

COL_LIST -> ID COL_LIST_PRIMA

COL_LIST_PRIMA -> COMA ID COL_LIST_PRIMA
COL_LIST_PRIMA -> ε

WHERE_CLAUSE -> WHERE CONDICION
WHERE_CLAUSE -> ε

#INSERT INTO tabla VALUES 
INSERT_STMT -> INSERT INTO ID VALUES PAREN_IZQ VAL_LIST PAREN_DER

VAL_LIST -> VALOR VAL_LIST_PRIMA

VAL_LIST_PRIMA -> COMA VALOR VAL_LIST_PRIMA
VAL_LIST_PRIMA -> ε

VALOR -> NUMERO
VALOR -> CADENA 
VALOR -> ID

# UPDATE tabla SET asignaciones 
UPDATE_STMT -> UPDATE ID SET ASIG_LIST WHERE_CLAUSE

ASIG_LIST -> ASIGNACION ASIG_LIST_PRIMA

ASIG_LIST_PRIMA -> COMA ASIGNACION ASIG_LIST_PRIMA
ASIG_LIST_PRIMA -> ε

ASIGNACION -> ID IGUAL VALOR

#DELETE FROM tabla 
DELETE_STMT -> DELETE FROM ID WHERE_CLAUSE

CONDICION -> COMPARACION COND_PRIMA

COND_PRIMA -> AND COMPARACION COND_PRIMA
COND_PRIMA -> OR COMPARACION COND_PRIMA
COND_PRIMA -> ε

COMPARACION -> ID IGUAL VALOR

```

# Gramatica de atributos
<table>
  <tr>
    <th>Produccion</th>
    <th>Atributo</th>
  </tr>
  <tr>
    <td>S → SELECT_STMT</td>
    <td>funcion regla_S_SELECT(SELECT_STMT):
    S.tipo = "SELECT"
    S.tabla = SELECT_STMT.tabla
    S.valido = SELECT_STMT.codigo != null
    S.codigo = SELECT_STMT.codigo
    retornar S
</td>
  </tr>
  <tr>
    <td>S → INSERT_STMT/td>
    <td>funcion regla_S_INSERT(INSERT_STMT):
    S.tipo = "INSERT"
    S.tabla = INSERT_STMT.tabla
    S.valido = INSERT_STMT.codigo != null
    S.codigo = INSERT_STMT.codigo
    retornar S</td>
  </tr>
  <tr>
    <td>S → UPDATE_STMT</td>
    <td>funcion regla_S_UPDATE(UPDATE_STMT):
    S.tipo = "UPDATE"
    S.tabla = UPDATE_STMT.tabla
    S.valido = UPDATE_STMT.codigo != null
    S.codigo = UPDATE_STMT.codigo
    retornar S</td>
  </tr>
  <tr>
    <td>S → DELETE_STMT</td>
    <td>funcion regla_S_DELETE(DELETE_STMT):
    S.tipo = "DELETE"
    S.tabla = DELETE_STMT.tabla
    S.valido = DELETE_STMT.codigo != null
    S.codigo = DELETE_STMT.codigo
    retornar S</td>
  </tr>
  <tr>
    <td>SELECT_STMT → SELECT COLS FROM ID WHERE_CLAUSE</td>
    <td>funcion regla_SELECT_STMT(COLS, ID, WHERE_CLAUSE):
    SELECT_STMT.columnas = COLS.lista
    SELECT_STMT.tabla = ID.lexema
    SELECT_STMT.where = WHERE_CLAUSE.condicion
    
    codigo = crear_nodo_AST()
    codigo.tipo = "SELECT"
    codigo.columnas = COLS.lista
    codigo.todos = COLS.todos
    codigo.tabla = ID.lexema
    codigo.where = WHERE_CLAUSE.existe ? WHERE_CLAUSE.condicion : null
    
    SELECT_STMT.codigo = codigo
    retornar SELECT_STMT</td>
  </tr>
  <tr>
    <td>COLS → ASTERISCO</td>
    <td>funcion regla_COLS_ASTERISCO():
    COLS.lista = []
    COLS.todos = true
    retornar COLS</td>
  </tr>
  <tr>
    <td>COLS → COL_LIST/td>
    <td>funcion regla_COLS_COL_LIST(COL_LIST):
    COLS.lista = COL_LIST.lista
    COLS.todos = false
    retornar COLS/td>
  </tr>
  <tr>
    <td>COL_LIST → ID COL_LIST_PRIMA</td>
    <td>funcion regla_COL_LIST(ID, COL_LIST_PRIMA):
    COL_LIST.lista = [ID.lexema] + COL_LIST_PRIMA.lista
    retornar COL_LIST/td>
  </tr>
  <tr>
    <td>COL_LIST_PRIMA → COMA ID COL_LIST_PRIMA</td>
    <td>funcion regla_COL_LIST_PRIMA_recursiva(ID, COL_LIST_PRIMA_siguiente):
    COL_LIST_PRIMA.lista = [ID.lexema] + COL_LIST_PRIMA_siguiente.lista
    retornar COL_LIST_PRIMA</td>
  </tr>
  <tr>
    <td>COL_LIST_PRIMA → ε</td>
    <td>funcion regla_COL_LIST_PRIMA_epsilon():
    COL_LIST_PRIMA.lista = []
    retornar COL_LIST_PRIMA</td>
  </tr>
  <tr>
    <td>WHERE_CLAUSE → WHERE CONDICION</td>
    <td>funcion regla_WHERE_CLAUSE_con_condicion(CONDICION):
    WHERE_CLAUSE.condicion = CONDICION.ast
    WHERE_CLAUSE.existe = true
    retornar WHERE_CLAUSE</td>
  </tr>
  <tr>
    <td>WHERE_CLAUSE → ε</td>
    <td>funcion regla_WHERE_CLAUSE_epsilon():
    WHERE_CLAUSE.condicion = null
    WHERE_CLAUSE.existe = false
    retornar WHERE_CLAUSE</td>
  </tr>
  <tr>
    <td>INSERT_STMT → INSERT INTO ID VALUES PAREN_IZQ VAL_LIST PAREN_DER
</td>
    <td>funcion regla_INSERT_STMT(ID, VAL_LIST):
    INSERT_STMT.tabla = ID.lexema
    INSERT_STMT.valores = VAL_LIST.valores
    
    // Generar código
    codigo = crear_nodo_AST()
    codigo.tipo = "INSERT"
    codigo.tabla = ID.lexema
    codigo.valores = VAL_LIST.valores
    
    INSERT_STMT.codigo = codigo
    retornar INSERT_STMT</td>
  </tr>
  <tr>
    <td>VAL_LIST → VALOR VAL_LIST_PRIMA</td>
    <td>funcion regla_VAL_LIST(VALOR, VAL_LIST_PRIMA):
    VAL_LIST.valores = [VALOR.valor] + VAL_LIST_PRIMA.valores
    retornar VAL_LIST</td>
  </tr>
  <tr>
    <td>VAL_LIST_PRIMA → COMA VALOR VAL_LIST_PRIMA/td>
    <td>funcion regla_VAL_LIST_PRIMA_recursiva(VALOR, VAL_LIST_PRIMA_siguiente):
    VAL_LIST_PRIMA.valores = [VALOR.valor] + VAL_LIST_PRIMA_siguiente.valores
    retornar VAL_LIST_PRIMA</td>
  </tr>
  <tr>
    <td>VAL_LIST_PRIMA → ε</td>
    <td>funcion regla_VAL_LIST_PRIMA_epsilon():
    VAL_LIST_PRIMA.valores = []
    retornar VAL_LIST_PRIMA</td>
  </tr>
  <tr>
    <td>VALOR → NUMERO</td>
    <td>funcion regla_VALOR_numero(NUMERO):
    VALOR.valor = convertir_a_numero(NUMERO.lexema)
    VALOR.tipo = "numero"
    retornar VALOR</td>
  </tr>
  <tr>
    <td>VALOR → CADENA</td>
    <td>funcion regla_VALOR_cadena(CADENA):
    VALOR.valor = CADENA.lexema
    VALOR.tipo = "cadena"
    retornar VALOR</td>
  </tr>
  <tr>
    <td>VALOR → ID</td>
    <td>funcion regla_VALOR_identificador(ID):
    VALOR.valor = ID.lexema
    VALOR.tipo = "identificador"
    retornar VALOR</td>
  </tr>
  <tr>
    <td>UPDATE_STMT → UPDATE ID SET ASIG_LIST WHERE_CLAUSE</td>
    <td>funcion regla_UPDATE_STMT(ID, ASIG_LIST, WHERE_CLAUSE):
    UPDATE_STMT.tabla = ID.lexema
    UPDATE_STMT.asignaciones = ASIG_LIST.asignaciones
    UPDATE_STMT.where = WHERE_CLAUSE.condicion
    
    codigo = crear_nodo_AST()
    codigo.tipo = "UPDATE"
    codigo.tabla = ID.lexema
    codigo.asignaciones = ASIG_LIST.asignaciones
    codigo.where = WHERE_CLAUSE.existe ? WHERE_CLAUSE.condicion : null
    
    UPDATE_STMT.codigo = codigo
    retornar UPDATE_STMT</td>
  </tr>
  <tr>
    <td>ASIG_LIST → ASIGNACION ASIG_LIST_PRIMA</td>
    <td>funcion regla_ASIG_LIST(ASIGNACION, ASIG_LIST_PRIMA):
    ASIG_LIST.asignaciones = [ASIGNACION.ast] + ASIG_LIST_PRIMA.asignaciones
    retornar ASIG_LIST</td>
  </tr>
  <tr>
    <td>ASIG_LIST_PRIMA → COMA ASIGNACION ASIG_LIST_PRIMA</td>
    <td>funcion regla_ASIG_LIST_PRIMA_recursiva(ASIGNACION, ASIG_LIST_PRIMA_siguiente):
    ASIG_LIST_PRIMA.asignaciones = [ASIGNACION.ast] + ASIG_LIST_PRIMA_siguiente.asignaciones
    retornar ASIG_LIST_PRIMA</td>
  </tr>
  <tr>
    <td>ASIG_LIST_PRIMA → ε</td>
    <td>funcion regla_ASIG_LIST_PRIMA_epsilon():
    ASIG_LIST_PRIMA.asignaciones = []
    retornar ASIG_LIST_PRIMA</td>
  </tr>
  <tr>
    <td>ASIGNACION → ID IGUAL VALOR</td>
    <td>funcion regla_ASIGNACION(ID, VALOR):
    ASIGNACION.columna = ID.lexema
    ASIGNACION.valor = VALOR.valor
    
    ast.tipo = "asignacion"
    ast.columna = ID.lexema
    ast.valor = VALOR.valor
    ast.tipo_valor = VALOR.tipo
    
    ASIGNACION.ast = ast
    retornar ASIGNACION</td>
  </tr>
  <tr>
    <td>DELETE_STMT → DELETE FROM ID WHERE_CLAUSE/td>
    <td>funcion regla_DELETE_STMT(ID, WHERE_CLAUSE):
    DELETE_STMT.tabla = ID.lexema
    DELETE_STMT.where = WHERE_CLAUSE.condicion
    
    // Generar código
    codigo = crear_nodo_AST()
    codigo.tipo = "DELETE"
    codigo.tabla = ID.lexema
    codigo.where = WHERE_CLAUSE.existe ? WHERE_CLAUSE.condicion : null
    
    DELETE_STMT.codigo = codigo
    retornar DELETE_STMT</td>
  </tr>
  <tr>
    <td>CONDICION → COMPARACION COND_PRIMA</td>
    <td>funcion regla_CONDICION(COMPARACION, COND_PRIMA):
    si COND_PRIMA.ast == null entonces
        CONDICION.ast = COMPARACION.ast
    sino
        CONDICION.ast = COND_PRIMA.ast
    fin_si
    
    CONDICION.valida = COMPARACION.ast != null
    retornar CONDICION</td>
  </tr>


</table>