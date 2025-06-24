class Outerwear:
    """Базовый класс для верхней одежды."""

    def __init__(self, name: str, size: str, material: str, insulation: bool):
        """
        Инициализация верхней одежды.
        :param name: Название изделия
        :param size: Размер (XS, S, M, L, XL, XXL)
        :param material: Основной материал
        :param insulation: Наличие утеплителя
        """
        self._name = name
        self._size = size.upper()
        self._material = material
        self._insulation = insulation
        self._is_clean = True  # Инкапсулированный атрибут - состояние чистоты

        # Валидация размера
        if self._size not in {"XS", "S", "M", "L", "XL", "XXL"}:
            raise ValueError("Недопустимый размер одежды")

    @property
    def name(self) -> str:
        """Название изделия."""
        return self._name

    @property
    def size(self) -> str:
        """Размер одежды."""
        return self._size

    @property
    def material(self) -> str:
        """Материал изделия."""
        return self._material

    @property
    def insulation(self) -> bool:
        """Наличие утеплителя."""
        return self._insulation

    def wear(self, hours: float = 1.0) -> str:
        """
        Носить одежду определенное количество часов.
        :param hours: Количество часов ношения (должно быть > 0)
        :return: Сообщение о результате ношения
        :raises ValueError: Если hours <= 0
        """
        if hours <= 0:
            raise ValueError("Время ношения должно быть положительным")
        self._is_clean = False
        return f"Одежда носилась {hours} часов"

    def clean(self) -> str:
        """Почистить одежду."""
        self._is_clean = True
        return "Одежда почищена"

    def __str__(self) -> str:
        """Строковое представление одежды."""
        insulated = "утепленная" if self.insulation else "неутепленная"
        return f"{self.name}, размер {self.size}, {self.material}, {insulated}"

    def __repr__(self) -> str:
        """Официальное строковое представление одежды."""
        return (f"{self.__class__.__name__}(name={self.name!r}, size={self.size!r}, "
                f"material={self.material!r}, insulation={self.insulation!r})")


class Coat(Outerwear):
    """Класс для пальто, наследующий от Outerwear."""

    def __init__(self, name: str, size: str, material: str, insulation: bool, length: str, style: str):
        """
        Инициализация пальто.
        :param name: Название
        :param size: Размер
        :param material: Материал
        :param insulation: Наличие утеплителя
        :param length: Длина (short, medium, long)
        :param style: Стиль (classic, modern, casual)
        """
        super().__init__(name, size, material, insulation)
        self._length = length.lower()
        self._style = style.lower()

        # Валидация длины
        if self._length not in {"short", "medium", "long"}:
            raise ValueError("Недопустимая длина пальто")

    @property
    def length(self) -> str:
        """Длина пальто."""
        return self._length

    @property
    def style(self) -> str:
        """Стиль пальто."""
        return self._style

    def wear(self, hours: float = 1.0, occasion: str = "casual") -> str:
        """
        Носить пальто с учетом мероприятия.
        Перегрузка метода wear для добавления специфики ношения пальто.
        :param hours: Количество часов ношения
        :param occasion: Тип мероприятия (casual, business, formal)
        :return: Сообщение о ношении
        """
        super().wear(hours)  # Используем родительский метод для базовой функциональности
        occasion = occasion.lower()
        if occasion not in {"casual", "business", "formal"}:
            raise ValueError("Недопустимый тип мероприятия")
        return f"Пальто носилось {hours} часов на {occasion} мероприятии"

    def button_up(self) -> str:
        """
        Застегнуть пальто.
        :return: Сообщение о результате
        """
        return "Пальто застегнуто"

    def __str__(self) -> str:
        """Строковое представление пальто."""
        base_str = super().__str__()
        return f"{base_str}, длина: {self.length}, стиль: {self.style}"

    def __repr__(self) -> str:
        """Официальное строковое представление пальто."""
        return (f"{self.__class__.__name__}(name={self.name!r}, size={self.size!r}, "
                f"material={self.material!r}, insulation={self.insulation!r}, "
                f"length={self.length!r}, style={self.style!r})")
