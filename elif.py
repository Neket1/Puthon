first = int(input())
second = int(input())
third = int(input())

if first == second and first == third:
    print( 'вывод всех трех чисел', first, second, third)
elif first == second :
    print( 'вывод всех трех чисел', first, second)
else:
    print('никакое число не совпало')