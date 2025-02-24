if __name__ == "__main__":
    class Animal:
        """Базовый класс для животных."""

        def __init__(self, species: str, name: str, age: int):
            """Конструктор класса Animal.

            Args:
            species (str): Вид животного.
            name (str): Имя животного.
            age (int): Возраст животного в годах.
            """
            self.species = species
            self.name = name
            self.age = age

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"{self.species} по имени {self.name}, возраст: {self.age} лет"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление объекта."""
            return f"Animal(species={self.species}, name={self.name}, age={self.age})"

        def make_sound(self) -> None:
            """Метод для воспроизведения звука, который издает животное.

            Обоснование: Разные животные издают разные звуки.
            """
            print(f"{self.name} издает звук.")


    class Cat(Animal):
        """Дочерний класс для кошек."""

        def __init__(self, name: str, age: int, color: str):
            """Расширяет конструктор класса Animal, добавляя цвет шерсти.

            Args:
            name (str): Имя кошки.
            age (int): Возраст кошки в годах.
            color (str): Цвет шерсти.
            """
            super().__init__("Кошка", name, age)
            self.color = color

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"{super().__str__()} с шерстью цвета {self.color}"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление объекта."""
            return f"Cat(name={self.name}, age={self.age}, color={self.color})"

        def make_sound(self) -> None:
            """Перегруженный метод воспроизведения звука.

            Обоснование: Кошки мяукают.
            """
            print(f"{self.name} мяукает.")


    class Dog(Animal):
        """Дочерний класс для собак."""

        def __init__(self, name: str, age: int, breed: str):
            """Расширяет конструктор класса Animal, добавляя породу.

            Args:
            name (str): Имя собаки.
            age (int): Возраст собаки в годах.
            breed (str): Порода собаки.
            """
            super().__init__("Собака", name, age)
            self.breed = breed

        def __str__(self) -> str:
            """Возвращает строковое представление объекта."""
            return f"{super().__str__()} породы {self.breed}"

        def __repr__(self) -> str:
            """Возвращает официальное строковое представление объекта."""
            return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

        def make_sound(self) -> None:
            """Перегруженный метод воспроизведения звука.

            Обоснование: Собаки лают.
            """
            print(f"{self.name} лает.")


    # Пример использования
    cat = Cat("Мурка", 3, "Серая")
    print(cat)
    print(repr(cat))
    cat.make_sound()

    dog = Dog("Бобик", 5, "Дворняга")
    print(dog)
    print(repr(dog))
    dog.make_sound()
