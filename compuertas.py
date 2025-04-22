import utilidades

def compuerta_AND(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (AND) solamente retorna 1 en caso de que ambos valores ingresados sean 1
    if utilidades.es_binario(primer_valor) and utilidades.es_binario(segundo_valor):
        return primer_valor and segundo_valor

def compuerta_NOT(valor):
    # Esta compuerta logica (NOT) retorna el valor contrario al ingresado (0 si se ingresa 1 y 1 si se ingresa 0)
    if utilidades.es_binario(valor):
        return 0 if valor == 1 else 1

def compuerta_OR(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (OR) retorna 1 si al menos uno de los valores ingresados es 1
    if utilidades.es_binario(primer_valor) and utilidades.es_binario(segundo_valor):
        return primer_valor or segundo_valor

def compuerta_NOR(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (NOR) retorna 1 siempre que los dos valores ingresados sean 0, caso contrario retorna 0
    if utilidades.es_binario(primer_valor) and utilidades.es_binario(segundo_valor):
        return compuerta_NOT(compuerta_OR(primer_valor, segundo_valor))

def compuerta_NAND(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (NAND) retorna 0 en caso que los dos valores ingresados sean 1, caso contrario retorna 1
    if utilidades.es_binario(primer_valor) and utilidades.es_binario(segundo_valor):
        return compuerta_NOT(compuerta_AND(primer_valor, segundo_valor))

def compuerta_XOR(primer_valor=0, segundo_valor=0):
    # Esta compuerta lógica (XOR) retorna 1 cuando los valores ingresados son diferentes, y 0 cuando son iguales.
    if utilidades.es_binario(primer_valor) and utilidades.es_binario(segundo_valor):
        return 1 if primer_valor != segundo_valor else 0