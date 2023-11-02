import matplotlib.pyplot as plt


class Polygon_App:

    def __init__(self, points):
        self.points = points

    def visualize(self, title):
        plt.figure()

        prv_element = None
        for element in self.points:

            if prv_element != None:
                plt.plot([element[0], prv_element[0]], [element[1], prv_element[1]], marker='o', linestyle='-', color='b')

            prv_element = element

        plt.title(title)
        plt.show()

    def offset_segment(self, segment_index: int, amount_offset: float):
        if segment_index < 0 or segment_index >= len(self.points):
            print(f"Помилка: Неправильний індекс сегменту (макс: {len(self.points) - 1})")
            return

        new_points = self.points.copy()

        for index_segment in [segment_index, segment_index - 1]:
            x, y = new_points[index_segment]

            if int(amount_offset) >= 0:
                x += abs(amount_offset)
            elif int(amount_offset) < 0:
                x -= abs(amount_offset)

            new_points[index_segment] = (x, y)

        self.points = new_points








