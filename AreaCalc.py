#Area Calculator
import math
from time import sleep

print('===================\n'
      '  Area Calculator\n'
      '===================')
while True:

    shape = (int(input('\n''1) Triangle\n2) '
                'Rectangle\n3) '
                'Sqaure\n4) '
                'Circle\n5) '
                'Quit\n'
                '\n'
                'Which shape? ')))

    if shape == 1:
        base = float(input('Base: '))
        height = float(input('Height: '))
        A = (base * height)/2
        print(f"The area is {A}")
        sleep(2)

    if shape == 2:
        length = float(input('Length: '))
        width = float(input('Width: '))
        A = length * width
        print(f"The area is {A}")
        sleep(2)

    if shape == 3:
        side = float(input('Side length: '))
        A = side**2
        print(f"The area is {A}")
        sleep(2)

    if shape == 4:
        radius = float(input('Radius: '))
        A = (math.pi * (radius**2))
        print(A)
        sleep(2)

    if shape == 5:
        print('Thank you for using the area calculator')
        break
    