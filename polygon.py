import matplotlib.pyplot as plt
import math

from points import Points
from segment import Segment


class Polygon_App:
    """
    Клас `Polygon_App` призначений для роботи з полігонами.

    Атрибути:
    polygon (Points): Полігон, представлений класом Points, що містить точки та їх підписи.

    Методи:
    __init__(self, polygon: Points):
                        Конструктор класу, ініціалізує об'єкт `Polygon_App` з вказаним полігоном.
    visualize(self, title: str):
                        Візуалізує полігон та його сегменти з підписами.
    offset_search(self, segment_index: int, amount_offset: float):
                        Виконує пошук та обчислення/створення сегмента на координатах.
    offset_segment(self, new_segment: Segment, segment_index: int):
                        Додає новий сегмент до полігону на вказаному індексі.
    """
    def __init__(self, polygon: Points):
        if polygon.points[0] != polygon.points[-1]:
            raise ValueError("Полігон має бути замкнутий (перша точка = остання точка)")

        self.polygon = polygon

    def visualize(self, title: str):
        """
        Візуалізація полігону

        :param title:
        :return:
        """
        # створення фігури
        plt.figure()

        # Цикл малюючий всі сегменти
        # попередня точка
        prv_element = None
        for i, element_point in enumerate(self.polygon.points):
            # перевірка для останьої точки
            if i+1 != len(self.polygon.points):
                # додавання labelʼа до точки
                plt.annotate(self.polygon.labels[i], (element_point[0], element_point[1]), textcoords="offset points",
                             xytext=(0, 10), ha='center')
            # перевірка попередньої точки (чи вона є)
            if prv_element is not None:
                # малювання сегмента
                plt.plot([element_point[0], prv_element[0]], [element_point[1], prv_element[1]],
                         marker='o', linestyle='-', color='b')
            # змінення попередньої точки
            prv_element = element_point
        # заголовок
        plt.title(title)
        # показ
        plt.show()

    def offset_search(self, segment_index: int, amount_offset: float):
        """
        Пошук сегмента та зсув його

        :param segment_index:
        :param amount_offset:
        :return:
        """

        # перевірка індекса сегмента
        if segment_index < 0 or segment_index >= len(self.polygon.points):
            print(f"Помилка: Неправильний індекс сегменту (макс: {len(self.polygon.points) - 1})")
            return

        # отримення координатів сегмента
        x1, y1 = self.polygon.points[segment_index-1]
        x2, y2 = self.polygon.points[segment_index]

        # обчислення нахилу кута
        angle_radians = math.atan((y2-y1)/(x2-x1))
        # в градусах
        angle_degrees = angle_radians * (180/math.pi)

        # offset сегмента на координатах
        x1_offset = x1 + amount_offset * math.sin(angle_degrees)
        x2_offset = x2 + amount_offset * math.sin(angle_degrees)

        y1_offset = y1 - amount_offset * math.cos(angle_degrees)
        y2_offset = y2 - amount_offset * math.cos(angle_degrees)

        # Збереження сегмента
        return Segment((x1_offset, y1_offset), (x2_offset, y2_offset))

    def offset_segment(self, new_segment: Segment, segment_index: int):
        """
        Додавання сегмента до полігону

        :param new_segment:
        :param segment_index:
        :return:
        """
        # змінення координатів
        self.polygon.points[segment_index - 1] = new_segment.start
        self.polygon.points[segment_index] = new_segment.end

        # перевірка на замикання полігону
        if self.polygon.points[0] != self.polygon.points[-1]:
            # замикання полігону
            self.polygon.points[-1] = self.polygon.points[0]

