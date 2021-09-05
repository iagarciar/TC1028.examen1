#Importa una libreria si lo requieres

def convertidor_tiempo(numero, unidad_base, unidad_conversion): 
    #Escribe tu código abajo de esta línea
    pass

def main():
    numero = int(input("Ingresa el tiempo que deseas convertir: "))
    unidad_base = input("Ingresa la unidad base: ")
    unidad_conversion = input("Ingresa la unidad a la cual se va a convertir: ")
    resultado = convertidor_tiempo(numero, unidad_base, unidad_conversion)
    print(resultado)
  
if __name__ == '__main__':
    main()