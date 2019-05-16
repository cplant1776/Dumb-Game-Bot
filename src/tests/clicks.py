import random
import matplotlib.pyplot as plt
from src.actors.actions import Actions
from shapely.geometry import Polygon


def view_click_region(poly):
    if not poly:
        poly = Polygon([(0, 0), (1, 0), (1, 2/3), (2/3, 2/3), (2/3, 1/3), (1/3, 1/3), (1/3, 2/3), (0, 2/3)])
    rand_points = Actions().generate_random_points_in_polygon(10000, polygon=poly)

    points = []
    for p in rand_points:
        points.append((p.x, p.y))
    x, y = zip(*points)

    s = 1
    plt.scatter(x, y, s=s)
    plt.axis([0, 1, 0, 1])
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == '__main__':
    view_click_region(None)
