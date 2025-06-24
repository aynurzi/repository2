class Plate:
    """
    Класс, описывающий тарелку с характеристиками материала, диаметра и состояния.

    Атрибуты:
        material (str): Материал тарелки (стекло, керамика и т.д.)
        diameter (float): Диаметр тарелки в сантиметрах (должен быть > 0)
        is_clean (bool): Чистая ли тарелка (по умолчанию True)
    """

    def __init__(self, material: str, diameter: float, is_clean: bool = True):
        """
        Инициализация тарелки.

        Args:
            material: Материал изготовления
            diameter: Диаметр в см (должен быть > 0)
            is_clean: Состояние чистоты (по умолчанию True)

        Raises:
            ValueError: Если диаметр <= 0

        Пример:
            >>> plate = Plate("ceramic", 20.5)
            >>> plate.material
            'ceramic'
        """
        if diameter <= 0:
            raise ValueError("Диаметр должен быть положительным числом")

        self.material = material
        self.diameter = diameter
        self.is_clean = is_clean

    def wash(self) -> str:
        """
        Моет тарелку, устанавливает статус is_clean в True.

        Returns:
            str: Сообщение о результате мытья

        Пример:
            >>> plate = Plate("glass", 15.0, False)
            >>> plate.wash()
            'Тарелка вымыта'
        """
        self.is_clean = True
        return "Тарелка вымыта"

    def use(self, food_amount: float = 1.0) -> str:
        """
        Использование тарелки (сервировка еды).

        Args:
            food_amount: Количество еды (должно быть > 0)

        Returns:
            str: Сообщение о результате использования

        Raises:
            ValueError: Если food_amount <= 0

        Пример:
            >>> plate = Plate("porcelain", 18.0)
            >>> plate.use(0.5)
            'Тарелка использована для 0.5 еды'
        """
        if food_amount <= 0:
            raise ValueError("Количество еды должно быть положительным")
        self.is_clean = False
        return f"Тарелка использована для {food_amount} еды"


class Glasses:
    """
    Класс, описывающий очки с характеристиками типа, диоптрий и состояния.

    Атрибуты:
        type (str): Тип очков (sunglasses, reading и т.д.)
        diopters (float): Оптическая сила линз
        is_broken (bool): Сломаны ли очки (по умолчанию False)
    """

    def __init__(self, type: str, diopters: float = 0.0, is_broken: bool = False):
        """
        Инициализация очков.

        Args:
            type: Тип очков
            diopters: Оптическая сила (по умолчанию 0.0)
            is_broken: Состояние (по умолчанию False)

        Пример:
            >>> glasses = Glasses("sunglasses")
            >>> glasses.type
            'sunglasses'
        """
        self.type = type
        self.diopters = diopters
        self.is_broken = is_broken

    def wear(self, hours: float = 1.0) -> str:
        """
        Носить очки определенное количество часов.

        Args:
            hours: Количество часов (должно быть > 0)

        Returns:
            str: Сообщение о результате ношения

        Raises:
            ValueError: Если hours <= 0

        Пример:
            >>> glasses = Glasses("reading", 2.5)
            >>> glasses.wear(3)
            'Очки носили 3.0 часов'
        """
        if hours <= 0:
            raise ValueError("Количество часов должно быть положительным")
        return f"Очки носили {hours} часов"

    def adjust_diopters(self, new_diopters: float) -> str:
        """
        Изменить оптическую силу линз.

        Args:
            new_diopters: Новое значение диоптрий

        Returns:
            str: Сообщение об изменении

        Пример:
            >>> glasses = Glasses("progressive", 1.5)
            >>> glasses.adjust_diopters(2.0)
            'Оптическая сила изменена на 2.0'
        """
        self.diopters = new_diopters
        return f"Оптическая сила изменена на {new_diopters}"


class TShirt:
    """
    Класс, описывающий футболку с характеристиками размера, цвета и состояния.

    Атрибуты:
        size (str): Размер футболки (S, M, L, XL)
        color (str): Основной цвет
        is_clean (bool): Чистая ли футболка (по умолчанию True)
    """

    def __init__(self, size: str, color: str, is_clean: bool = True):
        """
        Инициализация футболки.

        Args:
            size: Размер (должен быть S, M, L или XL)
            color: Цвет
            is_clean: Состояние (по умолчанию True)

        Raises:
            ValueError: Если размер недопустим

        Пример:
            >>> tshirt = TShirt("M", "blue")
            >>> tshirt.color
            'blue'
        """
        if size.upper() not in {"S", "M", "L", "XL"}:
            raise ValueError("Недопустимый размер")
        self.size = size.upper()
        self.color = color
        self.is_clean = is_clean

    def wear(self, days: int = 1) -> str:
        """
        Носить футболку определенное количество дней.

        Args:
            days: Количество дней (должно быть > 0)

        Returns:
            str: Сообщение о результате ношения

        Raises:
            ValueError: Если days <= 0

        Пример:
            >>> tshirt = TShirt("L", "black")
            >>> tshirt.wear(2)
            'Футболка носилась 2 дней'
        """
        if days <= 0:
            raise ValueError("Количество дней должно быть положительным")
        self.is_clean = False
        return f"Футболка носилась {days} дней"

    def wash(self, temperature: float = 30.0) -> str:
        """
        Постирать футболку.

        Args:
            temperature: Температура стирки (должна быть между 20 и 60)

        Returns:
            str: Сообщение о результате стирки

        Raises:
            ValueError: Если температура вне допустимого диапазона

        Пример:
            >>> tshirt = TShirt("XL", "white")
            >>> tshirt.wash(40.0)
            'Футболка постирана при 40.0°C'
        """
        if temperature < 20 or temperature > 60:
            raise ValueError("Температура должна быть между 20 и 60 градусами")
        self.is_clean = True
        return f"Футболка постирана при {temperature}°C"
