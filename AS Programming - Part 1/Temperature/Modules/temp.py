def CelsiusToF(celsius):
    #declare fahrenheit : REAL
    fahrenheit = celsius * 9/5 + 32
    print(celsius,"C =",fahrenheit,"F")

def FahrenheitToC(fahrenheit):
    #declare celsius : REAL
    celsius = (fahrenheit - 32)* 5/9
    print(celsius,"C =",fahrenheit,"F")