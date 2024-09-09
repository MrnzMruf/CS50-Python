def energy(m):
    c = 300000000
    E = m * (c ** 2)
    return E
def main():
    user_input = int(input("Please Enter mass in kilograms: "))
    E = energy(user_input)
    print(f"The Energy Measured in Joules will be: {E}")

main()
