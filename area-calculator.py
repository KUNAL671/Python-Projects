print('----------------------------')
print('       Area Calculator      ')
print('----------------------------')
print('''1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit''')
shape = int(input('Enter your shape number: '))
if shape == 1:
    base = int(input('Enter your base number: '))
    height = int(input('Enter your height: '))
    print('The area of the triangle is', base * height / 2)
elif shape == 2:
    length = int(input('Enter your length: '))
    width = int(input('Enter your width: '))
    print('The area of the rectangle is', length * width )
elif shape == 3:
    side = int(input('Enter your side length: '))
    print('The area of the square is', side * side )
elif shape == 4:
    radius = int(input('Enter your radius: '))
    pi = 3.14159
    print('The area of the circle is', pi * radius ** 2)
else:
    print('Stopped')
