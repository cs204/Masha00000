def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    v = v.replace("ft", "") # Удаляем "ft" из строки
    v = float(v) # Преобразуем строку в число типа float
    v = v * 0.3048 # Выполняем конвертацию из футов в метры
    return v
main()