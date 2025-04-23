import utilidades

def main():

    primer_valor = int(input("Ingrese el primer valor binario\n"))
    segundo_valor = int(input("Ingrese el segundo valor binario\n"))

    if not (utilidades.es_binario(primer_valor)) or not (utilidades.es_binario(segundo_valor)):
        print("Uno de los dos valores ingresados no es un valor binario, intentalo nuevamente\n")
        main()
    else:
        utilidades.elegir_compuerta(primer_valor, segundo_valor)

main()
