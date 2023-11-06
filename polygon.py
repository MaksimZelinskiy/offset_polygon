import matplotlib.pyplot as plt
import math

from points import Points
from segment import Segment


class Polygon_App:

    def __init__(self, polygon: Points):
        if polygon.points[0] != polygon.points[-1]:
            raise ValueError("Полігон має бути замкнутий (перша точка = остання точка)")

        self.polygon = polygon

    def visualize(self, title):
        plt.figure()

        prv_element = None
        for i, element_point in enumerate(self.polygon.points):
            if i+1 != len(self.polygon.points):
                plt.annotate(self.polygon.labels[i], (element_point[0], element_point[1]), textcoords="offset points",
                             xytext=(0, 10), ha='center')

            if prv_element is not None:

                plt.plot([element_point[0], prv_element[0]], [element_point[1], prv_element[1]],
                         marker='o', linestyle='-', color='b')

            prv_element = element_point

        plt.title(title)
        plt.show()

    def offset_search(self, segment_index: int, amount_offset: float):
        if segment_index < 0 or segment_index >= len(self.polygon.points):
            print(f"Помилка: Неправильний індекс сегменту (макс: {len(self.polygon.points) - 1})")
            return

        x1, y1 = self.polygon.points[segment_index-1]
        x2, y2 = self.polygon.points[segment_index]

        tilt_angle = math.atan((y2-y1)/(x2-x1))
        tilt_angle = tilt_angle * (180/math.pi)

        x1_offset = x1 + amount_offset * math.sin(tilt_angle)
        x2_offset = x2 + amount_offset * math.sin(tilt_angle)

        y1_offset = y1 - amount_offset * math.cos(tilt_angle)
        y2_offset = y2 - amount_offset * math.cos(tilt_angle)

        return Segment((x1_offset, y1_offset), (x2_offset, y2_offset))

    def offset_segment(self, new_segment: Segment, segment_index: int):

        self.polygon.points[segment_index - 1] = new_segment.start
        self.polygon.points[segment_index] = new_segment.end

        if self.polygon.points[0] != self.polygon.points[-1]:
            self.polygon.points[-1] = self.polygon.points[0]

