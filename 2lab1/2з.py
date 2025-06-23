from task_1 import Car, Tree, SocialNetwork

if __name__ == "__main__":
    try:
        car = Car("Toyota", "Camry", 2023)
        tree = Tree(10.0, "Oak")
        social_network = SocialNetwork("FacebookClone", 2000000)
    except Exception as e:
        print(f"Ошибка при создании объекта: {e}")

    try:
        car.change_color("Red")  # Попробуем изменить цвет автомобиля
    except ValueError as e:
        print(f"Ошибка: невозможно изменить цвет автомобиля")

    try:
        tree.grow(-5)  # Попытаться увеличить возраст дерева на отрицательное количество лет
    except ValueError as e:
        print(f"Ошибка: неправильное значение возраста")

    try:
        social_network.add_users(-100)  # Вызвать метод с некорректным количеством новых пользователей
    except ValueError as e:
        print(f"Ошибка: неправильные данные")
