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
