class Points:
    """
    Клас `Points` використовується для представлення точок для полігона
    на координатній площині та надання їм підписів (labels).

    Атрибути:
    points (list of tuples): Список координат точок [(x1, y1), (x2, y2), ..., (xn, yn)].
    labels (list of str): Список підписів для точок.

    """
    def __init__(self, polygon):
        self.points = polygon
        self.labels = ['a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z']
