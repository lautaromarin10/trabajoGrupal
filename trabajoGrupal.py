def es_binario(valor):
    return valor in [0,1]

def compuerta_AND(primerValor = 0, segundoValor = 0):

    if es_binario(primerValor) and es_binario(segundoValor):
        return primerValor and segundoValor
