import matplotlib.pyplot as plt

# Зсув полігону
def shift_polygon(polygon, segment_index, shift_amount):

    # перевірка потрібних елементів для роботи
    if segment_index < 0 or segment_index >= len(polygon):
        # помилка
        print(f"У вас сталося помилка\n\nНеправильний індекс сегменту (макс: {len(polygon)-1})")

        return polygon

    # копіювання полігону
    new_polygon = polygon.copy()

    # зсув сегмента (двух точек)
    for index_segment in [segment_index-1, segment_index]:
        x, y = new_polygon[index_segment]

        if int(shift_amount) >= 0:
            x += abs(shift_amount)
        elif int(shift_amount) < 0:
            x -= abs(shift_amount)

        new_polygon[index_segment] = (x, y)

    return new_polygon


def visualize_polygon(polygon, title):
    plt.figure()

    prv_element = None
    for element in polygon:
        if prv_element != None:
            plt.plot([element[0], prv_element[0]], [element[1], prv_element[1]],
                     marker='o', linestyle='-', color='b')
        prv_element = element

    plt.title(title)
    plt.show()


def main():
    # стандартний полігон
    polygon = [(10, 10), (20, 15), (30, 23), (22, 40)]
    visualize_polygon(polygon, "Початковий полігон")

    cycle = True
    while cycle:
        try:
            segment_index = int(input("Введіть індекс сегменту для зсуву: "))
            shift_amount = float(input("Введіть величину зсуву: "))

            shifted_polygon = shift_polygon(polygon, segment_index, shift_amount)

            if shifted_polygon != polygon:
                cycle = False

        except ValueError:
            print("Неправильний формат вводу.")

    visualize_polygon(shifted_polygon, "Полігон після зсуву")


if __name__ == "__main__":
    main()
