import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count_pass = int(input("Введите количество паролей: "))
length_pass = int(input('Введите длину пароля: '))
include_digits = input("Включать ли цифры в пароль? да / нет: ").lower() == "да"
include_lowercase_letters = input("Включать ли строчные буквы? да / нет: ").lower() == "да"
include_uppercase_letters = input("Включать ли прописные буквы? да / нет: ").lower() == "да"
include_punctuation = input("Включать ли неоднозначные символы? да / нет: ").lower() == "да"

if include_digits:
    chars += digits
if include_lowercase_letters:
    chars += lowercase_letters
if include_punctuation:
    chars += punctuation
if include_uppercase_letters:
    chars += uppercase_letters

def generate_password(length, chars):
    if not chars:
        print("Ошибка. Не выбран ни один диапазон символов")
        exit
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password 

def save_passwords_to_file(passwords, file_path):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            for item in passwords:
                file.write(f"Сервис: {item['service']}\nПароль: {item['password']}\n\n")
        print(f"\nПароли сохранены в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

passwords_list = []
for i in range(1, count_pass + 1):
    pwd = generate_password(length_pass, chars) 
    print(f'Пароль {i}: {pwd}')
    service = input(f"Для чего этот пароль? (Enter чтобы пропустить): ").strip()
    if service:
        passwords_list.append({"service": service, "password": pwd})

if passwords_list:
    if input("\nСохранить пароли в файл? (да/нет): ").lower() == "да":
        file_path = input("Введите путь к файлу (например: C:/passwords.txt): ").strip()
        save_passwords_to_file(passwords_list, file_path)