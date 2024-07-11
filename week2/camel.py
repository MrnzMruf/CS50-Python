def camel_to_snake(variable_name):
    snake_case = ""
    for char in variable_name:
        # Check if character is uppercase
        if char.isupper():
            # If it's the first character, convert to lowercase
            if snake_case == "":
                snake_case += char.lower()
            else:
                snake_case += "_" + char.lower()
        else:
            snake_case += char

    return snake_case


def main():
    # Prompt user for input
    variable_name = input("camelCase: ")

    # Convert camel case to snake case
    snake_case_name = camel_to_snake(variable_name)

    # Output the snake case variable name
    print("snake_case:", snake_case_name)


if __name__ == "__main__":
    main()
