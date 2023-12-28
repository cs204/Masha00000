def camel_to_snake():
    camel_case = input("Верблюжий стиль: ")
    snake_case = ""

    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    print(snake_case)

camel_to_snake()