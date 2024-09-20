import shop
import controller

def message():
    print("1 Добавить товар")
    print("2 Удалить товар по имени")
    print("3 Вывести все товары")
    print("0 Выход")

def main():
    control = controller.Controller()
    control.loadData()

    while True:
        message()
        digital = input("Введите номер функции: ")

        if digital == "1":
            type = int(input("1 TV / 2 NoteBook: "))
            nameTov = input("Введите имя: ")
            control.addNewTovar(nameTov, type)
        elif digital == "2":
            nameProd = input("Введите имя товара для удаления: ")
            control.removeByName(nameProd)
            pass

        elif digital == "3":
            control.showAllProduct()
            pass
        elif digital == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()
