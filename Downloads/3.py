numbers = [] 
number = int(input("Введите целое число (для выхода введите 0): ")) 
 
while number != 0: 
    numbers.append(number) 
    number = int(input("Введите целое число (для выхода введите 0): ")) 
 
if len(numbers) > 0: 
    maximum = max(numbers) 
    minimum = min(numbers) 
    average = sum(numbers) / len(numbers) 
 
    print("Максимальное значение:", maximum) 
    print("Минимальное значение:", minimum) 
    print("Среднее арифметическое:", average) 
else: 
    print("Вы не ввели ни одного числа.")