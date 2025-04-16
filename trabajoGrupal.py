def es_binario(valor):
    # Comprueba que el valor ingresado es un binaro (0 o 1)
    return valor in [0,1]

def compuerta_AND(primerValor = 0, segundoValor = 0):
    #Esta compuerta logica (AND) solamente retorna 1 en caso de que ambos valores ingresados sean 1
    if es_binario(primerValor) and es_binario(segundoValor):
        return primerValor and segundoValor

def compuerta_NOT(valor):
    #Esta compuerta logica (NOT) retorna el valor contrario al ingresado (0 si se ingresa 1 y 1 si se ingresa 0)
    if(es_binario(valor)):
        return 0 if valor == 1 else 1
    
def compuerta_OR(primerValor = 0, segundoValor = 0):
    #Esta compuerta logica (OR) retorna 1 si al menos uno de los valores ingresados es 1
    if es_binario(primerValor) and es_binario(segundoValor):
        return primerValor or segundoValor

def compuerta_NOR(primerValor = 0, segundoValor = 0):
    #Esta compuerta logica (NOR) retorna 1 siempre que los dos valores ingresados sean 0, caso contrario retorna 0
    if es_binario(primerValor) and es_binario(segundoValor):
        return compuerta_NOT(compuerta_OR(primerValor, segundoValor))

def compuerta_NAND(primerValor = 0, segundoValor = 0):
    #Esta compuerta logica (NAND) retorna 0 en caso que los dos valores ingresados sean 1, caso contrario retorna 1
    if es_binario(primerValor) and es_binario(segundoValor):
        return compuerta_NOT(compuerta_AND(primerValor, segundoValor))
