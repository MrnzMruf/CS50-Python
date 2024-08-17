import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    # CheckError
    if len(sys.argv) == 1:
        # ItMeansRandom:
        list_font = figlet.getFonts()
        selected_font = random.choice(list_font)
        figlet.setFont(font=selected_font)
    elif len(sys.argv) == 3:
        # correct format check
        if sys.argv[1] in ("-f", "--font"):
            font_name = sys.argv[2]
            list_font = figlet.getFonts()
            if font_name in list_font:
                figlet.setFont(font=font_name)
            else:
                print("Invalid usage")
                sys.exit(1)
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

    inp_str = input("Input: ")

    out_str = figlet.renderText(inp_str)
    print(out_str)


if __name__ == "__main__":
    main()
