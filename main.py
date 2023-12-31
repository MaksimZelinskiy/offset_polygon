from polygon import Polygon_App
from points import Points


def main():
    # створення координт для полігону
    polygon = [(10, 10), (15, 25), (20, 30), (27, 20), (25, 5), (10, 10)]
    # створення полігону
    polygon_app = Polygon_App(polygon=Points(polygon))
    # візуалізація
    polygon_app.visualize("Початковий полігон")

    cycle = True
    while cycle:
        try:
            segment_index = int(input("Введіть індекс сегменту для зсуву: "))
            offset_amount = float(input(f"Введіть величину зсуву для сегмента "
                                        f"{''.join(polygon_app.polygon.labels[segment_index-1:segment_index+1])}: "))

            # створення сегменту
            new_segment = polygon_app.offset_search(segment_index, offset_amount)
            # додавання сегменту
            polygon_app.offset_segment(new_segment, segment_index)
            # кінець циклу
            cycle = False
        except ValueError:
            print("Неправильний формат вводу.")

    # візуалізація
    polygon_app.visualize("Полігон після offset")


if __name__ == "__main__":
    # запуск файлу
    main()
