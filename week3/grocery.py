grocery_dict = {} 

print("Please enter grocery items (one per line). Press Ctrl+D (or Ctrl+Z on Windows) to finish:")  

while True:     
    try:
        item = input()
        item_upper = item.strip().upper()  # Normalize case and remove whitespace   

        if item_upper:   # Only process non-empty strings 
            if item_upper in grocery_dict:
                grocery_dict[item_upper] += 1
            else:
                grocery_dict[item_upper] = 1
    except EOFError:
        break

# Sort items alphabetically and prepare the output  
sorted_items = sorted(grocery_dict.keys())

print("\nYour Grocery List:")
for item in sorted_items:
    count = grocery_dict[item]
    print(f"{count}.{item}")
