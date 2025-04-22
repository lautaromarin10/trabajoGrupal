import compuertas

def es_binario(valor):
    # Comprueba que el valor ingresado es un binaro (0 o 1)
    return valor in [0, 1]

def seleccionar_compuerta():
    compuerta_seleccionada = int(input("Ingrese la compuerta logica que quieres utilizar \n 1: AND\n 2: OR\n 3: NOT\n 4: NAND\n 5: XOR\n 6: NOR\n"))
    return compuerta_seleccionada

def compuertas_basicas(compuerta_elegida, primer_valor, segundo_valor):
    
    if compuerta_elegida == 1:
        #Compuerta AND
        print(f"El resultado de aplicar la compuerta AND entre {primer_valor} y {segundo_valor} es {compuertas.compuerta_AND(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 2:
        #Compuerta OR
        print(f"El resultado de aplicar la compuerta OR entre {primer_valor} y {segundo_valor} es {compuertas.compuerta_OR(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 3:
        #Compuerta NOT
        valor_elegido = int(input(f"Que valor quieres utilizar en la compuerta NOT? {primer_valor} o {segundo_valor}"))
        if valor_elegido not in [primer_valor, segundo_valor]:
            print("El valor elegido no es un valor valido")
        else:
            print(f"El resultado de aplicar la compuerta NOT a {valor_elegido} es {compuertas.compuerta_NOT(valor_elegido)}")

def compuertas_avanzadas(compuerta_elegida, primer_valor, segundo_valor):
    
    if compuerta_elegida == 4:
        #Compuerta NAND
        print(f"El resultado de aplicar la compuerta NAND entre {primer_valor} y {segundo_valor} es {compuertas.compuerta_NAND(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 5:
        #Compuerta XOR
        print(f"El resultado de aplicar la compuerta XOR entre {primer_valor} y {segundo_valor} es {compuertas.compuerta_XOR(primer_valor, segundo_valor)}")
    elif compuerta_elegida == 6:
        #Compuerta NOR
        print(f"El resultado de aplicar la compuerta NOR entre {primer_valor} y {segundo_valor} es {compuertas.compuerta_NOR(primer_valor, segundo_valor)}")

def elegir_compuerta(primer_valor, segundo_valor):

    compuerta = seleccionar_compuerta()

    if compuerta in [1,2,3]:
        compuertas_basicas(compuerta, primer_valor, segundo_valor)
    elif compuerta in [4,5,6]:
        compuertas_avanzadas(compuerta, primer_valor, segundo_valor)
    else:
        print("El numero ingresado no corresponde a una opcion valida, por favor intentalo nuevamente")
        elegir_compuerta(primer_valor, segundo_valor)