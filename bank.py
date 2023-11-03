def main():
    greeting = input("Приветствие: ")
    if greeting.startswith("здравствуйте"):
        print("$0")
    elif greeting.startswith("з"):
        print("$20")
    else:
        print("$100")
main()