from shop import TV, noteBook
import json
import xml.etree.ElementTree as ET

tovar_list = []
filename = "product_list.json"

class Controller:
    def loadData(self):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    model = item["model"]
                    price = item["price"]
                    if item["type"] == "TV":
                        tovar = TV(model, price, item["resolution"])
                    elif item["type"] == "noteBook":
                        tovar = noteBook(model, price, item["processor"])
                    tovar_list.append(tovar)
            print("Данные успешно загружены")
        except FileNotFoundError:
            print("Файл не найден, будет создан при сохранении")
        except json.JSONDecodeError:
            print("Ошибка чтения JSON файла")

    def saveDataToXML(self):
        root = ET.Element("products")

        for product in tovar_list:
            product_elem = ET.Element("product")
            model_elem = ET.SubElement(product_elem, "model")
            model_elem.text = product.modelT

            price_elem = ET.SubElement(product_elem, "price")
            price_elem.text = str(product.priceT)

            type_elem = ET.SubElement(product_elem, "type")
            if isinstance(product, TV):
                type_elem.text = "TV"
                resolution_elem = ET.SubElement(product_elem, "resolution")
                resolution_elem.text = product.resolution
            elif isinstance(product, noteBook):
                type_elem.text = "noteBook"
                processor_elem = ET.SubElement(product_elem, "processor")
                processor_elem.text = product.processor

            root.append(product_elem)

        tree = ET.ElementTree(root)
        with open("product_list.xml", "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)

    def saveData(self):
        data = []
        for product in tovar_list:
            if isinstance(product, TV):
                product_data = {
                    "model": product.modelT,
                    "price": product.priceT,
                    "type": "TV",
                    "resolution": product.resolution
                }
            elif isinstance(product, noteBook):
                product_data = {
                    "model": product.modelT,
                    "price": product.priceT,
                    "type": "noteBook",
                    "processor": product.processor
                }
            data.append(product_data)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def addNewTovar(self, name, type):
        price = int(input("Введите цену: "))
        if type == 1:
            resolution = input("Введите разрешение экрана: ")
            tovar_list.append(TV(name, price, resolution))
        elif type == 2:
            processor = input("Введите процессор: ")
            tovar_list.append(noteBook(name, price, processor))
        else:
            print("Неверный тип товара")
            return
        print("Товар добавлен успешно")
        self.saveData()
        self.saveDataToXML()

    def showAllProduct(self):
        for i, product in enumerate(tovar_list, 1):
            print(f"Товар {i}:")
            print(f"Модель: {product.modelT}")
            print(f"Цена: {product.priceT}")
            product_type = product.getType()
            print(f"Тип: {product_type}")
            product.getInfo()
            print("\n")

    def removeByName(self, name):
        for i, product in enumerate(tovar_list):
            if product.modelT.lower() == name.lower():
                removed_product = tovar_list.pop(i)
                print(f"Товар '{removed_product.modelT}' успешно удален")
                self.saveData()
                self.saveDataToXML()
                return
        print(f"Товар с названием '{name}' не найден")
