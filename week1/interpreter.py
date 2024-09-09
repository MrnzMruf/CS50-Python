import re

input_user = input("Expression: ").strip()
input_user = re.findall(r'[+\-*/]|\d+(?:\.\d+)?', input_user)
input_user = " ".join(input_user)
input_user = input_user.split(" ")
x = float(input_user[0])
y = input_user[1]
z = float(input_user[2])

match y:
    case "+":
        #if y == "+":
        print("{:.1f}".format(x+z))
    case "-":
        #if y == "-":
        print("{:.1f}".format(x-z))
    case "*":
        #if y == "*":
        print("{:.1f}".format(x*z))
    case "/":
        #if y == "/":
        if z != 0:
            print("{:.1f}".format(x/z))
        else:
            print("no way")





