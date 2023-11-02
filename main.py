from polygon import Polygon_App


def main():
    polygon = Polygon_App(
        [(29, 20), (10, 2), (15, 32)]
    )
    polygon.visualize("Початковий полігон")

    cycle = True
    while cycle:
        try:
            segment_index = int(input("Введіть індекс сегменту для зсуву: "))
            offset_amount = float(input("Введіть величину зсуву: "))

            polygon.offset_segment(segment_index, offset_amount)
            cycle = False

        except ValueError:
            print("Неправильний формат вводу.")

    polygon.visualize("Полігон після offset")


if __name__ == "__main__":
    main()
