
def calculate_change():
    ad = 50  # Amount Due
    ic = 0   # Inserted Coin
    co = 0   # Change Owned

    while ic < ad:
        amount_due = ad - ic
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin [5, 10, 25]: "))

        if coin == 5 or coin == 10 or coin == 25:
            ic += coin

            if ic == co:
                print(f"Change Owed: {co}")

            if ic > ad:
                co = ic - ad
               # print(f"Changed owned: {co}")

   # if ad < ic:
    #    co = ic - ad
    print(f"Change Owed: {co}")
    #if change_owend > 0:


if __name__ == "__main__":
    calculate_change()
