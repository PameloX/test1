print("0 в качестве знака операции"
      "\nзавершит работу программы\n")

while True:
    s = input("Знак (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("Введите первое число a = "))
        b = float(input("Введите первое число b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")