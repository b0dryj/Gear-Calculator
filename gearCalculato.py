#Gear calculator
#by b0dryj

from colorama import Fore, Back, Style #Добавление плагина "colorama"
from colorama import init #Добавление инцивилизации
init () #Инцивилизация




#спрашиваем что хочет вычислить пользователь
print(Fore.WHITE)
print("Вот что мы можем вычеслить (Вводить обозначение без ковычек):")
print('"da" - диаметр вершин зубьев')
print('"df" - диаметр впадин зубьев')
print('"d" - делительный диаметр')
print('"Pt" - окружной шаг')
print('"h" - высота зуба')
print('"hf"- высота ножки зуба')
print('"ha"- высота головки зуба')
print('"St"- окружная толцина зуба')

print(Fore.BLACK)
print(Back.BLUE)
what = str (input("Введите что хотите найти:"))

print(Fore.BLACK)
print(Back.MAGENTA)
if what == "da":
    print("Формула: da=m*(z+2)")
    m = float (input("Введите модуль шестерни(m):"))
    z = float (input("Введите количество зубцов у шестерни(z):"))
    da = m*(z+2)
    print ("Диаметр вершин зубьев = " + str(da) + "mm")

elif what == "df":
    print("Формула: df=m*(z-2,5)")
    m = float(input("Введите модуль шестерни(m):"))
    z = float(input("Введите количество зубцов у шестерни(z):"))
    df = m*(z-2.5)
    print("Диаметр впадин зубьев = " + str(df) + "mm")

elif what == "d":
    print("Формула: d=m*z")
    m = float(input("Введите модуль шестерни(m):"))
    z = float(input("Введите количество зубцов у шестерни(z):"))
    d = m * z
    print("Делительный диаметр = " + str(d) + "mm")

elif what == "Pt":
    print("Формула: Pt=п*m")
    m = float(input("Введите модуль шестерни(m):"))
    Pt = 3.14 * m
    print ("Окружной шаг = " + str(Pt) + "mm")

elif what == "h":
    print("Формула: h = hf + ha")
    hf = float(input("Введите высоту ножки зуба(hf): "))
    ha = float (input("Введите высоту головки зуба(ha): "))
    h = hf * ha
    print("Высота зуба= " + str(h) + "mm")

elif what == "hf":
    print ("Формуда: hf = 1,25mm")
    print ("hf всегда равно 1,25mm")

elif what == "ha":
    print("Формула: ha = m")
    m = float (input("Введите модуль шестерни(m): "))
    hf = m
    print("Высота головки зуба = " + str(hf) + "mm")

elif what == "St":
    print("Формула: St = Pt/2")
    Pt = float (input("Введите окружной шаг(Pt): "))
    St = Pt / 2
    print("Окружная толщина зуба = " + str(St) + "mm" )

else:
    print(Fore.BLACK)
    print(Back.RED)
    print("Введено неверное обозначение!")

print(Fore.BLACK)
print(Back.RED)
input("Нажмите на любую клавишу чтобы выйти из программы.")
Style.RESET_ALL

