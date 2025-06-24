from task_1 import Plate, Glasses, TShirt

if __name__ == "__main__":
    try:
        plate = Plate("ceramic", 20.5)
        glasses = Glasses("sunglasses", 0.0)
        tshirt = TShirt("M", "blue")
    except Exception as e:
        print(f"Ошибка при создании объекта: {e}")
    try:
        plate.use(-0.5)
    except ValueError as e:
        print(f"Ошибка в тарелке: {e}")

    try:
        glasses.wear(-2)
    except ValueError as e:
        print(f"Ошибка в очках: {e}")

    try:
        tshirt.wash(70)  # Попытка стирки при слишком высокой температуре
    except ValueError as e:
        print(f"Ошибка в футболке: {e}")
