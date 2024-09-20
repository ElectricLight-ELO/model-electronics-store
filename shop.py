class _Product:
    def __init__(self, model, price):
        self.modelT = model
        self.priceT = price

    def getType(self):
        raise NotImplementedError("абстрактный метод")

    def getInfo(self):
        raise NotImplementedError("абстрактный метод")


class noteBook(_Product):
    def __init__(self, model, price, processor):
        super().__init__(model, price)
        self.processor = processor

    def getType(self):
        return "noteBook"

    def getInfo(self):
        print(f"Процессор: {self.processor}")


class TV(_Product):
    def __init__(self, model, price, resolution):
        super().__init__(model, price)
        self.resolution = resolution

    def getType(self):
        return "TV"

    def getInfo(self):
        print(f"Разрешение экрана: {self.resolution}")