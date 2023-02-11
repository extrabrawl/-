def del_space(vir0s):
    x = "" 
    for i in range(len(vir0s)):

        if vir0s[i] != " ":
            x = x+vir0s[i]
    return x


def calculating():
    v = input("Введите выражение: ")
    v = del_space(v)
    print(v)
    num = []
    sign = []
    i = 0
    buf = ""
    while i < len(v):
        while i<len(v) and v[i] >= "0" and v[i] <= "9":
            buf = buf+v[i] 
            i = i+1
        bufi = int(buf)
        num.append(bufi)
        buf = ""
        if i<len(v):
            sign.append(v[i])
        i = i+1
    i = len(sign)-1
    while i >= 0:
        if sign[i] == "^":
            c = num[i] ** num[i+1]
            num.pop(i)
            sign.pop(i)
            num[i] = c
        i = i-1
    
    i = 0
    while i<len(sign):
        if sign[i] == "*":
            c = num[i] * num[i+1]
            num.pop(i)
            num[i] = c
            sign.pop(i)
        else:
            if sign[i] == "/" or sign[i] == ":":
                c = num[i] // num[i+1]
                num.pop(i)
                num[i] = c
                sign.pop(i)
            else:
                i = i+1

    while len(sign) != 0:
        if sign[0] == "+":
            c = num[0] + num[1]
            num.pop(0)
            num[0] = c
        else:
            if sign[0] == "-":
                c = num[0] - num[1]
                num.pop(0)
                num[0] = c
        
        sign.pop(0)
    print("Ответ:", num[0])

print("Добро пожаловать в калькулятор!")
while True:
    d = input("Введите 1, если хотите продолжить или 2, если выйти: ")
    if d == "1":
        calculating()
    elif d == "2":
        break
    else:
        print("Некорректный ввод. Попробуйте еще раз.")   
    