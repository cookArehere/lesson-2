"""
Task 4

доп задания (под звездочкой)

вариант задания осваивать форматирование строк. Заполните прочерк чтобы получить вот такую строку на выходе.
обратите внимание что 110110 это двоичное представление числа. То есть в строке выведен int, str, int, float но второй инт выведен в виде битовом

"000012 Василий 110110 32.10"



print("____________________".format(12, "Василий", 54, 32.1))



Попробуйте взять какое то одно слово в переменную и "собрать" из него другие слова. Выведите по разному, капсом, маленькими, с отступами.

Например взяли слово "Корован"

s1 = "Корован"

подумайте как вы из него можете вывести слово "ворона"


"""
task4 = '{:^65}'.format('Task 4')
print(task4)
print()

# print("____________________".format(12, "Василий", 54, 32.1))
print('{0:0>6} {1:s} {2:b} {3:g}'.format(12, "Василий", 54, 32.1))

# 1 variant
vorona = '{4}{3}{2}{1}{6}{5}'.format(*'Корован')
print(vorona)
print(vorona.capitalize())
print(vorona.upper())

#2 varint
s1 = 'Корован'
print(s1[4:0:-1] + s1[-1:-3:-1])
