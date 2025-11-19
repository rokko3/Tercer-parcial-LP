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
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>
  <tr>
    <td>Valor 1</td>
    <td>Valor 2</td>
  </tr>
  <tr>
    <td>Valor 3</td>
    <td>Valor 4</td>
  </tr>

</table>