
def p1():
    try:
        def remq(a, p):
            a.pop(p + 1)
            a.pop(p)
            a.pop(p - 1)
            return a

        def calculator(*args):
            a = []
            k = 0
            for i in range(len(s)):
                if not s[i].isnumeric():
                    a.append(str(s[k:i]))
                    a.append(str(s[i]))
                    k = i + 1
                if i == len(s) - 1:
                    a.append(str(s[k:]))

            while "*" in a:
                p = a.index("*")
                res = float(a[p - 1]) * float(a[p + 1])
                a = remq(a, p)
                a.insert(p - 1, res)
            while "/" in a:
                p = a.index("/")
                res = float(a[p - 1]) / float(a[p + 1])
                a = remq(a, p)
                a.insert(p - 1, res)
            res = float(a[0])
            for i in range(len(a)):
                if a[i] == "+":
                    res += float(a[i + 1])
                if a[i] == "-":
                    res -= float(a[i + 1])
            return res

        s = input("Enter Operation Format With [+,*,-,/] Only\n")
        b=calculator(s)
    except:
        print("Enter Valid in Format Example:  1+2*3/4\n")
        p1()

    else:
        print(s, end=" = ")
        print(b)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
p1()