

#1
import json
with open("test1.json","r", encoding="utf-8*") as file:
    a = json.load(file)
    for key in a:
        d= a[key]['city']
        if d == "Moscow":
            print(a[key]['name'])
            print(a[key]['age'],'лет')
            print(d,)

#2
import json
фамилия = input("Ваша фамилия: ")
имя = input("Имя: ")
отчество = input("отчество: ")
телефон = input("номер телефона или данные карты: ")
год_рождения = input("год рождения: ")
город_рождения = input("Введите ваш город рождения или где проживаете: ")
место_учебы = input("Введите ваше место учёбы: ")
Оценка = input("Как вам наш анонимный тест напишите отзыв: ")
данные = {
    "Фамилия":фамилия,
    "Имя":имя,
    "Отчество":отчество,
    "Телефон":телефон,
    "Год_рождения":год_рождения,
    "Город_рождения":город_рождения,
    "Место_учёбы":место_учебы,
    "Оценка":Оценка
}
with open('данные.json', 'w', encoding='utf-8') as json_file:
    json.dump(данные, json_file, ensure_ascii=False, indent=4)

print("Всё теперь ты в казахстане 'данные.json'.")

#3
import json

with open('данные.json', 'r', encoding='utf-8') as json_file:
    dan = json.load(json_file)
print("Текущие данные:")
for ключ, значение in dan.items():
    print(f"{ключ}: {значение}")

ключ_для_изменения = input("Введите Имя ключ, чтобы его изменить: ")
if ключ_для_изменения in dan:

    новое_значение = input(f"Новые данные '{ключ_для_изменения}': ")

    dan[ключ_для_изменения] = новое_значение

    with open('данные.json', 'w', encoding='utf-8') as json_file:
        json.dump(dan, json_file, ensure_ascii=False, indent=4)

    print(f"Данные внутри '{ключ_для_изменения}' сохр.")
