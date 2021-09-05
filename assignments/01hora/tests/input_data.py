# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["60", "S", "S"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "60"],
            "Revisa el caso cuando la unidad de origen y destino sean la misma",
        ),
        # Test case 2
        (
            ["61", "S", "M"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "2"],
            "Revisa el redondeo y tu conversión de segundos a minutos",
        ),
        # Test case 3
        (
            ["3601", "S", "H"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "2"],
            "Revisa el redondeo y tu conversión de segundos a minutos",
        ),
        # Test case 4
        (
            ["61", "M", "H"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "2"],
            "Revisa el redondeo y tu conversión de minutos a horas",
        ),
        # Test case 5
        (
            ["2", "M", "S"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "120"],
            "Revisa el redondeo y tu conversión de segundos a minutos",
        ),
        # Test case 6
        (
            ["2", "H", "S"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "7200"],
            "Revisa el redondeo y tu conversión de segundos a minutos",
        ),
        # Test case 7
        (
            ["10", "H", "M"],
            ["Ingresa el tiempo que deseas convertir: ", "Ingresa la unidad base: ", "Ingresa la unidad a la cual se va a convertir: ", "600"],
            "Revisa el redondeo y tu conversión de segundos a minutos",
        )
    ]
