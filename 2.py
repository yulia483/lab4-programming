"""
Максимум из трех чисел 
"""

#ввод чисел 
a=int(input("введите первое число: "))
b=int(input("введите второе число: "))
c=int(input("введите третье число: "))
#сравниваем числа 
if a>=b and a>=c:
    maximum=a
elif b>=a and b>=c:
    maximum=b
else:
    maximum=c
print(f"максимум: {maximum}")


