answer =  input("the Great Question of Life, the Universe and Everything? ").lower()
answer = answer.replace(" ","")
if answer == "42" or answer == "forty-two" or answer == "fortytwo":
    print("Yes")
else:
    print("No")
