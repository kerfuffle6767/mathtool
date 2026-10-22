import sys
import math

max_value=10000

def spravka():
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0 \n" \
    "Использование:    \n" \
    "python mathtool.py                          вывод справки    \n\
    python mathtool.py --help                  вывод справки    \n\
    python mathtool.py solve                   ввод коэффициентов с клавиатуры    \n\
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами\n\
    Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")

def main():
    if len(sys.argv)<=1 or sys.argv[1]=="--help":
        spravka()
        sys.exit(0)
    if sys.argv[1]!="solve":
        print("неизвестная команда",file=sys.stderr)
        sys.exit(1)
    if sys.argv[1]=="solve" and len(sys.argv)==2:
        A=int(input("Введите А: ")) 
        B=int(input("Введите B: "))
        C=int(input("Введите C: ")) 
    elif len(sys.argv)==8:
        if sys.argv[2]!="-a" and sys.argv[4]!="-b" and sys.argv[6]!="-c":
            print("неизвестный параметр",file=sys.stderr)
            sys.exit(1)
        A=sys.argv[3]
        B=sys.argv[5]
        C=sys.argv[7]
    else:
        print("неверный набор параметров",file=sys.stderr)
        sys.exit(1)

    try:
        a1=int(A)
        b1=int(B)
        c1=int(C)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом",file=sys.stderr)
        sys.exit(1)

    if abs(a1)>max_value or abs(b1)>max_value or abs(c1)>max_value:
        print("ОШИБКА:значение вне допустимого диапазона",file=sys.stderr)
        sys.exit(1)
    if a1 == 0:
        if b1!=0:
            print("Уравнение линейное")
            X = -c1/b1
            print (f"X= {X:.3f}")
            sys.exit(0)
        else:
            print("ОШИБКА:это не уравнение, неизвестное отсутствует",file=sys.stderr)
            sys.exit(1)
            
    print("Уравнение квадратное")
    D = b1*b1 - 4*a1*c1
    print ("D= " + str(D))

    if D>0:
        x1= (-b1 + D**(1/2))/(2*a1)
        x2= (-b1 - D**(1/2))/(2*a1)
        print (f"{x1:.3f}, {x2:.3f}")
    elif D==0:
        x = -b1/(2*a1)
        print (f"{x:.3f}")
    else:
        print ("Действительных корней нет")

main()
