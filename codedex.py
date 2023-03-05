print("En este archivo agregare todos los retos realizados por mi de la web codedex\n")


print("Reto 3: Generar cadena de caracteres en un orden especifico utilizando la funcion print\n")
print("metodo 1:saltos de linea\n       1\n     2 3\n   4 5 6\n7 8 9 10")
print("\nmetodo 2: concatenear en una sola linea varios elementos\n", "       1\n", "     2 3\n", "   4 5 6\n", "7 8 9 10")
print("""\nmetodo 3:comillas triples
       1
     2 3
   4 5 6
7 8 9 10 """)
print("\nmetodo 4: varios prints")
print("       1")
print("     2 3")
print("   4 5 6")
print("7 8 9 10")

print("\nReto 4: Create an initials.py program that displays your initials in block letters.First, start your program with a comment that says a fun fact about yourself.Then, create your block letters with your initials.\n")
print("method 1: Multiples prints\n") #mi comentario divertido es que voy a utilizar el spanglish para programar :)
print("N      N  I")
print("NN     N  I")
print("N N    N  I")
print("N  N   N  I")
print("N   N  N  I")
print("N    N N  I")
print("N     NN  I")
print("\n method 2: triple comillas")
print("""
N      N  I
NN     N  I
N N    N  I
N  N   N  I
N   N  N  I
N    N N  I
N     NN  I
 """)

print("\n challenge 5: In this task, you are going to write a letter to your future self... in Python.")
print("""
Today's date: 05/03/2023

How you are feeling right now: me siento ambicioso por el futuro
What you want to accomplish during this course: En 3 meses voy a dominar el lenguage python en un 50%
A little message to your older, wiser, and programmer self: Valio la pena, cada dia valio la pena
Your favorite emoji to spice things up!: ;) """)

print("\nchallenge 7:Create a temperature.py program that converts a temperature from Fahrenheit (°F) to Celsius (°C).Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.")
farenheit = 53
Celcius = (farenheit-32)/1.8
temperature_celcius = round(Celcius)
print("la temperatura de brooklyn es de " + str(temperature_celcius) + "º Grados Celcius")

print("\nchallenge 8:It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.Create a bmi.py program that calculates your own BMI.")

weight_kg = 58
Height_M = 1.83
BMI=  weight_kg/ (Height_M**2)
print("Mi indice de masa corporal es: " + str(round(BMI)))

print("\n challenge 9: Create a hypotenuse.py program that asks the user for two numbers, a and b, and calculates the hypotenuse using the Pythagorean equation\n")

cateto = int(input("Ingrese el valor numerico del primer catateto: "))
cateto_2 = int(input("Ingrese el valor numerico del segundo catateto: "))
import math
hipotenusa = round(math.sqrt((cateto**2) + (cateto_2**2)), 1)
print("La hipotenusa tiene un valor de: " + str(hipotenusa))

print("\n challenge 10: Create a currency.py program that asks the user for the amount they have in yuan, yen, and won and calculates the total in USD.")

Yuan = int(input("\nIngresa la cantidad de Yuanes chinos que tienes: "))
Yen = int(input("Ingresa la cantidad de Yenes japoneses que tienes: "))
Won = int(input("Ingresa la cantidad de Wones coreanos que tienes: "))
Total_usd = Yuan * 0.14 + Yen * 0.0074 + Won * 0.00077

print("la cantidad total de USD que tienes entre todas las divisas es de: " + str(Total_usd) + "$ a el cambio de el 5 de marzo de 2023")