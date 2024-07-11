def twttr():
    inp = input("Input: ")
    inp_list = [char for char in inp]
    #print(inp_list)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    inp_new = []
    for char in inp:
        if char not in vowels:
            inp_new.append(char)

    #print(f"Output: {inp_new}")
    out = ''.join(inp_new)
    print(f"Output: {out}")




if __name__ == "__main__":
    twttr()
