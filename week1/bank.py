#str_input = input("Greeting: ").lower().strip()
def main():
    str_input = input("Greeting: ").lower().strip()
    if str_input.startswith("hello",0,6):
        print("$0")
    elif str_input.startswith("h",0,1):
        print("$20")
    else:
        print("$100")

main()
