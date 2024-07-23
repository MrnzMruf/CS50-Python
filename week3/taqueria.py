dict_taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

##print(dict_taqueria)

total_cost = 0.0  

print("Welcome to the Taqueria! Please enter your orders (Press Ctrl+D to finish):")  

try:  
    while True:  
        item = input().strip()  
        item = item.title()  # تبدیل به حروف بزرگ و کوچک مناسب  

        if item in dict_taqueria:  
            total_cost += dict_taqueria[item]  
            print(f"Total: ${total_cost:.2f}")  
        else:  
            print(f"{item} is not on the menu. Please try again.")  
except EOFError:  
    print("Thank you for your order!")
