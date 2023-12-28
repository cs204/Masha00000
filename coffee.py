def main():
    amount_due = 50
    change_owed = 0

    print(f"Нужная сумма: {amount_due}")

    while change_owed < amount_due:
        coin = int(input('Вставьте монету: '))
        change_owed += coin
        remaining_due = amount_due - change_owed
        if change_owed - amount_due == 0:
            break
        print(f"Ваша сдача: {remaining_due} рублей")

    if change_owed >= amount_due:
        change = change_owed - amount_due
        print(f"Ваша сдача: {change}")

main()
