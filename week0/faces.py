def convert(str1):
    str1 = str1.replace(":)","🙂")
    str1 = str1.replace(":(","🙁")
    return str1

def main():
    user_input = input("Say Sth with Emoticons to convert it: ")
    result = convert(user_input)
    print(result)

main()
