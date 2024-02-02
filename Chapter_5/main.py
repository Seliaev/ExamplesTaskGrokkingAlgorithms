class Somebody:
    """Пример хэширования и сравнения значений обьекта класса"""
    def __init__(self, age, name):
        self.age: int = age
        self.name: str = name

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

    def __hash__(self) -> hash:
        """хэширует tuple из данных"""
        return hash((self.age, self.name))



