import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


class Sample_Class():
    def __init__(self, type='cool'):
        self.type = type
        if type == 'cool':
            self.generate_letters()
        else:
            pass

    def generate_letters(self):
        self.patches = []
        scale = np.array([3, 4])

        shift = np.array([-4, 0])
        c_polygon = np.array([[0, 0], [2, 0], [2, 1], [1, 1], [1, 3], [2, 3], [2, 4], [0, 4]]) + shift
        polygon = Polygon(scale * c_polygon, True)
        self.patches.append(polygon)

        e_polygon = np.array(
            [[0., 0.], [2., 0.], [2., 1.], [1., 1.], [1., 1.5], [2., 1.5], [2., 1.5], [2., 2.5], [1., 2.5], [1., 3.],
             [2., 3.],
             [2., 4.], [0., 4.]]) + np.array([2.5, 0]) + shift
        polygon = Polygon(scale * e_polygon, True)
        self.patches.append(polygon)

        r_polygon = np.array(
            [[0, 0], [1, 0], [1, 2], [1.5, 0], [2.5, 0], [2, 2], [2.5, 2], [2.5, 4], [0, 4]]) + np.array([5, 0]) + shift
        polygon = Polygon(scale * r_polygon, True)
        self.patches.append(polygon)

        n_polygon = np.array([[0, 0], [1, 0], [1, 2], [3, 0], [3, 4], [2, 4], [2, 2], [0, 4]]) + np.array(
            [8, 0]) + shift
        polygon = Polygon(scale * n_polygon, True)
        self.patches.append(polygon)

        shift = np.array([-6, -4])

        r_polygon = np.array(
            [[0, 0], [1, 0], [1, 2], [1.5, 0], [2.5, 0], [2, 2], [2.5, 2], [2.5, 4], [0, 4]]) + shift
        polygon = Polygon(scale * r_polygon, True)
        self.patches.append(polygon)

        u_polygon = np.array(
            [[0, 0], [3, 0], [3, 4], [2, 4], [2, 1], [1, 1], [1, 4], [0, 4]]) + np.array([3, 0]) + shift
        polygon = Polygon(scale * u_polygon, True)
        self.patches.append(polygon)

        l_polygon = np.array(
            [[0, 0], [2, 0], [2, 1], [1, 1], [1, 4], [0, 4]]) + np.array([6.5, 0]) + shift
        polygon = Polygon(scale * l_polygon, True)
        self.patches.append(polygon)

        e_polygon = np.array(
            [[0., 0.], [2., 0.], [2., 1.], [1., 1.], [1., 1.5], [2., 1.5], [2., 1.5], [2., 2.5], [1., 2.5], [1., 3.],
             [2., 3.],
             [2., 4.], [0., 4.]]) + np.array([9, 0]) + shift
        polygon = Polygon(scale * e_polygon, True)
        self.patches.append(polygon)

        s_polygon = np.array(
            [[0, 0], [3, 0], [3, 2.4], [1, 2.4], [1, 3.2], [3, 3.2], [3, 4], [0, 4], [0, 1.6], [2, 1.6], [2, .8],
             [0, .8]]) + np.array([11.5, 0]) + shift
        polygon = Polygon(scale * s_polygon, True)
        self.patches.append(polygon)

        shift = np.array([-6, -5])
        bar_ploygon = np.array(
            [[0., 0.], [14.5, 0.], [14.5, 1], [0, 1]]) + shift
        polygon = Polygon(scale * bar_ploygon, True)
        self.patches.append(polygon)

    def plot_letters(self):
        fig, ax = plt.subplots()
        colors = np.linspace(0, 9, 10)
        print(colors)
        p = PatchCollection(self.patches, alpha=0.8)
        p.set_array(np.array(colors))
        ax.add_collection(p)
        # ax.set_ylim(-1, 1)
        # ax.set_xlim(-1, 1)
        plt.axis('off')
        fig.colorbar(p, ax=ax)

    def plot(self):
        if self.type == 'cool':
            self.plot_letters()

    def generate_sample(self, number, n=1):
        if self.type == 'cool':
            return self.generate_sample_letters(number, n)
        else:
            return self.generate_gaussian_sample(number, n)

    def generate_gaussian_sample(self, number, n):
        self.mean = [10 * np.cos((n * 2 * np.pi) / 10), 10 * np.sin((n * 2 * np.pi) / 10)]
        v1 = [np.cos((n * 2 * np.pi) / 10), np.sin((n * 2 * np.pi) / 10)]
        v2 = [-np.sin((n * 2 * np.pi) / 10), np.cos((n * 2 * np.pi) / 10)]
        a1 = .5
        a2 = .2
        M = np.vstack((v1, v2)).T
        S = np.array([[a1, 0], [0, a2]])
        self.cov = np.dot(np.dot(M, S), np.linalg.inv(M))
        return_value = np.random.multivariate_normal(mean=self.mean, cov=self.cov, size=number)

        return np.array([return_value])

    def generate_sample_letters(self, number, n):
        polygon = self.patches[n].get_verts()
        extend = [np.min(polygon[:, 0]), np.max(polygon[:, 0]),
                  np.min(polygon[:, 1]), np.max(polygon[:, 1])]
        bbPath = mplPath.Path(polygon)
        nr_points = 0
        points = []
        while nr_points < number:
            xp = np.random.uniform(low=extend[0], high=extend[1], size=1)
            yp = np.random.uniform(low=extend[2], high=extend[3], size=1)
            coordinates = np.array([xp, yp])  # np.dstack((xp,yp))[0]
            if bbPath.contains_point(coordinates):
                points.append(coordinates)
            nr_points = len(points)
        return_value = np.array(points)

        return return_value


instance = Sample_Class('noncool')

nr_samples = 500
for i in range(10):
    coordinates = instance.generate_sample(nr_samples, i)
    coordinates = coordinates.reshape(500,2,1)
    # print(coordinates.shape)
    plt.scatter(coordinates[:, 0], coordinates[:, 1], c='r')
    plt.title('First test 10D gaussian')

plt.show()

instance = Sample_Class()

for i in range(10):
    coordinates = instance.generate_sample(nr_samples, i)
    # print(coordinates.shape)
    plt.scatter(coordinates[:, 0], coordinates[:, 1], c='blue')
    plt.title('Cool stuff')

plt.show()


