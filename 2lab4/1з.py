class Disk:
    """
    Базовый класс для дисков.

    Атрибуты:
        title (str): Название диска.
        capacity (float): Вместимость диска в гигабайтах.
        used_space (float): Используемое пространство на диске в гигабайтах.
    """

    def __init__(self, title: str, capacity: float):
        """
        Инициализация диска.

        Аргументы:
            title (str): Название диска.
            capacity (float): Вместимость диска в гигабайтах.
        """
        self.title = title
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной")
        self.capacity = capacity
        self.used_space = 0.0  # Изначально использованное пространство равно 0

    def __str__(self) -> str:
        """
        Возвращает строковое представление диска.

        Возвращаемое значение:
            str: Строковое представление диска.
        """
        return f"Диск '{self.title}', вместимость: {self.capacity}GB, использовано: {self.used_space}GB"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление диска.

        Возвращаемое значение:
            str: Официальное строковое представление диска.
        """
        return f"{self.__class__.__name__}(title={self.title!r}, capacity={self.capacity!r}, used_space={self.used_space!r})"

    def add_data(self, size: float) -> None:
        """
        Добавление данных на диск.

        Аргументы:
            size (float): Размер добавляемых данных в гигабайтах.

        Исключения:
            ValueError: Если добавляемые данные превышают доступное пространство.
        """
        if self.used_space + size > self.capacity:
            raise ValueError("Недостаточно места на диске.")
        self.used_space += size

    def display_info(self) -> str:
        """
        Возвращает информацию о диске.

        Возвращаемое значение:
            str: Информация о диске.
        """
        return f"Название: {self.title}, Вместимость: {self.capacity}GB, Использовано: {self.used_space}GB"

class CDDisk(Disk):
    """
    Класс для CD-дисков, наследующий от класса Disk.

    Атрибуты:
        title (str): Название CD-диска.
        capacity (float): Вместимость CD-диска в гигабайтах (обычно 0.7GB).
        used_space (float): Используемое пространство на CD-диске в гигабайтах.
        audio_quality (str): Качество аудио на CD-диске.
    """
    def __init__(self, title: str, audio_quality: str):
        """
        Инициализация CD-диска.

        Аргументы:
            title (str): Название CD-диска.
            audio_quality (str): Качество аудио на CD-диске.
        """
        super().__init__(title, 0.7)  # Устанавливаем стандартную вместимость CD-диска
        self.audio_quality = audio_quality

    def __str__(self) -> str:
        """
        Возвращает строковое представление CD-диска.

        Возвращаемое значение:
            str: Строковое представление CD-диска.
        """
        return (f"CD-диск '{self.title}', вместимость: {self.capacity}GB, "
                f"использовано: {self.used_space}GB, качество аудио: {self.audio_quality}")

    def display_info(self) -> str:
        """
        Возвращает информацию о CD-диске.

        Возвращаемое значение:
            str: Информация о CD-диске.

        Причина перегрузки:
            Добавление информации о качестве аудио.
        """
        parent_info = super().display_info()  # Вызов метода родительского класса
        return f"{parent_info}, Качество аудио: {self.audio_quality}"


if __name__ == "__main__":
    try:
        cd_disk = CDDisk("My Favorite Album", "High Quality")
        print(cd_disk)
        print(cd_disk.display_info())
        print(repr(cd_disk))
        cd_disk.add_data(0.5)  # Добавляем данные на диск

