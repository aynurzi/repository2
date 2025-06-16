class Car:
    """Класс, представляющий автомобиль."""

    def __init__(self, brand: str, model: str, year: int, color: str = "black"):
        """
        Конструктор автомобиля.
        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска (целое число >= 1900).
        :param color: Цвет автомобиля (по умолчанию черный).
        :raises TypeError: Если год выпуска указан строкой.
        :raises ValueError: Если год выпуска меньше 1900.
        """
        try:
            # Пытаемся преобразовать значение года к типу int
            year = int(year)
        except ValueError:
            # Если значение года не может быть преобразовано к числу, выбрасываем ошибку
            raise TypeError("Год выпуска должен быть числовым значением.")

        if year < 1900:
            # Если год меньше 1900, выбрасываем ошибку
            raise ValueError("Год выпуска автомобиля должен быть больше или равен 1900.")

        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет автомобиля.
        :param new_color: Новый цвет автомобиля.
        """
        self.color = new_color

    def get_info(self) -> str:
        """
        Возвращает информацию об автомобиле в формате 'Бренд Модель, Год выпуска, Цвет'.
        :return: Строку с информацией об автомобиле.
        """
        return f"{self.brand} {self.model}, {self.year}, {self.color}"


class Tree:
    """Класс, представляющий дерево."""

    def __init__(self, height: float, species: str, age: int = 0):
        """
        Конструктор дерева.
        :param height: Высота дерева (в метрах, положительное число).
        :param species: Вид дерева.
        :param age: Возраст дерева (по умолчанию 0 лет).
        :raises TypeError: Если высота дерева отрицательная.
        """
        # Проверка типа высоты
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числовым значением.")

        # Проверка значения высоты
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")

        self.height = height
        self.species = species
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на указанное количество лет.
        :param years: Количество лет, на которое увеличивается возраст (целое число >= 0).
        :raises TypeError: Если количество лет отрицательное.
        """
        # Проверка типа количества лет
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом.")

        # Проверка значения количества лет
        if years < 0:
            raise ValueError("Количество лет должно быть неотрицательным числом.")

        self.age += years

    def get_height_and_age(self) -> tuple[float, int]:
        """
        Возвращает высоту и возраст дерева.
        :return: Кортеж (высота, возраст).
        """
        return self.height, self.age


class SocialNetwork:
    """Представляет социальную сеть с названием и количеством пользователей."""

    def __init__(self, name: str, num_users: int):
        """Инициализирует объект социальной сети."""
        self.name = name
        if not isinstance(num_users, int):
            raise TypeError("Количество пользователей должно быть целым числом.")
        if num_users < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным целым числом.")
        self.num_users = num_users

    def add_users(self, num_new_users: int) -> int:
        """Добавляет новых пользователей в социальную сеть.
        Аргументы:
            num_new_users (int): Количество новых пользователей для добавления. Должно быть неотрицательным.
        Возвращает:
            int: Обновленное количество пользователей.
        Исключения:
            TypeError: если num_new_users не целое число.
            ValueError: если num_new_users отрицательно.
        >>> sn = SocialNetwork("ПримернаяСеть", 1000)
        >>> sn.add_users(500)
        1500
        """
        if not isinstance(num_new_users, int):
            raise TypeError("Количество новых пользователей должно быть целым числом.")
        if num_new_users < 0:
            raise ValueError("Количество новых пользователей не может быть отрицательным.")
        self.num_users += num_new_users
        return self.num_users

    def get_user_count(self) -> int:
        """Возвращает текущее количество пользователей."""
        return self.num_users
