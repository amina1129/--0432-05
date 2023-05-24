print ('Введите произвольную строку:')
stroka = input()
lenght = len(stroka)
stroka_bez_3 = ""
print ('Строка без 3-го символа (через срез): ', stroka [:2] + stroka [3:])
for i in range (0, lenght):
    if i != 2:
        stroka_bez_3 = stroka_bez_3 + stroka[i]
    if stroka[i] == "с":
     print('Найден символ (FOR)')
print ('Строка без 3-го символа (через цикл): ', stroka_bez_3)
simvol = stroka.find("с")
if simvol != -1:
    print('Найден символ (FIND)')
print ('Длина строки: ', lenght)
print ('Cтрока без последнего символа (через срез): ', stroka [0:lenght-1])
