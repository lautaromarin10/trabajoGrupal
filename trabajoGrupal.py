def es_binario(valor):
    # Comprueba que el valor ingresado es un binaro (0 o 1)
    return valor in [0, 1]

def compuerta_AND(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (AND) solamente retorna 1 en caso de que ambos valores ingresados sean 1
    if es_binario(primer_valor) and es_binario(segundo_valor):
        return primer_valor and segundo_valor

def compuerta_NOT(valor):
    # Esta compuerta logica (NOT) retorna el valor contrario al ingresado (0 si se ingresa 1 y 1 si se ingresa 0)
    if es_binario(valor):
        return 0 if valor == 1 else 1

def compuerta_OR(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (OR) retorna 1 si al menos uno de los valores ingresados es 1
    if es_binario(primer_valor) and es_binario(segundo_valor):
        return primer_valor or segundo_valor

def compuerta_NOR(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (NOR) retorna 1 siempre que los dos valores ingresados sean 0, caso contrario retorna 0
    if es_binario(primer_valor) and es_binario(segundo_valor):
        return compuerta_NOT(compuerta_OR(primer_valor, segundo_valor))

def compuerta_NAND(primer_valor=0, segundo_valor=0):
    # Esta compuerta logica (NAND) retorna 0 en caso que los dos valores ingresados sean 1, caso contrario retorna 1
    if es_binario(primer_valor) and es_binario(segundo_valor):
        return compuerta_NOT(compuerta_AND(primer_valor, segundo_valor))

def compuerta_XOR(primer_valor=0, segundo_valor=0):
    # Esta compuerta lógica (XOR) retorna 1 cuando los valores ingresados son diferentes, y 0 cuando son iguales.
    if es_binario(primer_valor) and es_binario(segundo_valor):
        return 1 if primer_valor != segundo_valor else 0

def seleccionar_compuerta():
    compuerta_seleccionada = int(input("Ingrese la compuerta logica que quieres utilizar \n 1: AND\n 2: OR\n 3: NOT\n 4: NAND\n 5: XOR\n 6: NOR\n"))
    return compuerta_seleccionada

def compuertas_basicas(compuerta_elegida, primer_valor, segundo_valor):
    
    if compuerta_elegida == 1:
        #Compuerta AND
        print(f"El resultado de aplicar la compuerta AND entre {primer_valor} y {segundo_valor} es {compuerta_AND(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 2:
        #Compuerta OR
        print(f"El resultado de aplicar la compuerta OR entre {primer_valor} y {segundo_valor} es {compuerta_OR(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 3:
        #Compuerta NOT
        valor_elegido = int(input(f"Que valor quieres utilizar en la compuerta NOT? {primer_valor} o {segundo_valor}"))
        if valor_elegido not in [primer_valor, segundo_valor]:
            print("El valor elegido no es un valor valido")
        else:
            print(f"El resultado de aplicar la compuerta NOT a {valor_elegido} es {compuerta_NOT(valor_elegido)}")

def compuertas_avanzadas(compuerta_elegida, primer_valor, segundo_valor):
    
    if compuerta_elegida == 4:
        #Compuerta NAND
        print(f"El resultado de aplicar la compuerta NAND entre {primer_valor} y {segundo_valor} es {compuerta_NAND(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 5:
        #Compuerta XOR
        print(f"El resultado de aplicar la compuerta XOR entre {primer_valor} y {segundo_valor} es {compuerta_XOR(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 6:
        #Compuerta NOR
        print(f"El resultado de aplicar la compuerta NOR entre {primer_valor} y {segundo_valor} es {compuerta_NOR(primer_valor, segundo_valor)}")

def elegir_compuerta(primer_valor, segundo_valor):

    compuerta = seleccionar_compuerta()

    if compuerta in [1,2,3]:
        compuertas_basicas(compuerta, primer_valor, segundo_valor)
    elif compuerta in [4,5,6]:
        compuertas_avanzadas(compuerta, primer_valor, segundo_valor)
    else:
        print("El numero ingresado no corresponde a una opcion valida, por favor intentalo nuevamente")
        elegir_compuerta(primer_valor, segundo_valor)

def main():

    primer_valor = int(input("Ingrese el primer valor binario\n"))
    segundo_valor = int(input("Ingrese el primer valor binario\n"))

    if not (es_binario(primer_valor)) or not (es_binario(segundo_valor)):
        print("Uno de los dos valores ingresados no es un valor binario, intentalo nuevamente\n")
        main()
    else:
        elegir_compuerta(primer_valor, segundo_valor)
