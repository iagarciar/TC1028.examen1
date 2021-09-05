![Tec de Monterrey](../../images/logotecmty.png)
# Convertidor de tiempo
**Examen 1**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
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
```
La línea `#Escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Este programa consiste en elaborar una función que sirva como convertidor de unidades de tiempo, el cual nos permitirá cambiar entre las unidades de: 
Segundos (S),
Minutos (M),
Horas (H).

Si la salida resultará en un número con decimales, dicho número se deberá redondear hacia arriba y convertir a entero.
Para este ejercicio se puede emplear la libería math

**Entradas**
Número a convertir (Número entero positivo),
Unidad base (S, M o H).
Unidad de tiempo a la cual se va convertir (S, M o H).

**Salida**
La salida consiste de un número entero positivo

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Ingresa el tiempo que deseas convertir: 1010
Ingresa la unidad base: S
Ingresa la unidad a la cual se va a convertir: M
17

Ingresa el tiempo que deseas convertir: 2
Ingresa la unidad base: H
Ingresa la unidad a la cual se va a convertir: S
7200

Ingresa el tiempo que deseas convertir: 60
Ingresa la unidad base: M
Ingresa la unidad a la cual se va a convertir: M
60
```

Una vez que termines tu actividad y la hayas probado con `pytest`,
súbela a tu repositorio en GitHub, con el proceso de `commit + push`.