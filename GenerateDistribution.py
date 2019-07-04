import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


class Sample_Cern_Letters():
    def __init__(self):
        self.patches = []

        shift = np.array([2, 0])
        c_polygon = np.array([[0, 0], [2, 0], [2, 1], [1, 1], [1, 3], [2, 3], [2, 4], [0, 4]]) + shift
        polygon = Polygon(c_polygon, True)
        self.patches.append(polygon)

        e_polygon = np.array(
            [[0., 0.], [2., 0.], [2., 1.], [1., 1.], [1., 1.5], [2., 1.5], [2., 1.5], [2., 2.5], [1., 2.5], [1., 3.], [2., 3.],
             [2., 4.], [0., 4.]]) + np.array([2.5, 0]) + shift
        polygon = Polygon(e_polygon, True)
        self.patches.append(polygon)

        r_polygon = np.array(
            [[0, 0], [1, 0], [1, 2], [1.5, 0], [2.5, 0], [2, 2], [2.5, 2], [2.5, 4], [0, 4]]) + np.array([5, 0]) + shift
        polygon = Polygon(r_polygon, True)
        self.patches.append(polygon)

        n_polygon = np.array([[0, 0], [1, 0], [1, 2], [3, 0], [3, 4], [2, 4], [2, 2], [0, 4]]) + np.array([8, 0]) + shift
        polygon = Polygon(n_polygon, True)
        self.patches.append(polygon)

        r_polygon = np.array(
            [[5, 0], [6, 0], [6, 2], [6.5, 0], [7.5, 0], [7, 2], [7.5, 2], [7.5, 4], [5, 4]]) + np.array([-5, -5])
        polygon = Polygon(r_polygon, True)
        self.patches.append(polygon)

        u_polygon = np.array(
            [[0, 0], [3, 0], [3, 4], [2, 4], [2, 1], [1, 1], [1, 4], [0, 4]]) + np.array([3, -5])
        polygon = Polygon(u_polygon, True)
        self.patches.append(polygon)

        l_polygon = np.array(
            [[0, 0], [2, 0], [2, 1], [1, 1], [1, 4], [0, 4]]) + np.array([6.5, -5])
        polygon = Polygon(l_polygon, True)
        self.patches.append(polygon)

        e_polygon = np.array(
            [[0., 0.], [2., 0.], [2., 1.], [1., 1.], [1., 1.5], [2., 1.5], [2., 1.5], [2., 2.5], [1., 2.5], [1., 3.], [2., 3.],
             [2., 4.], [0., 4.]]) + np.array([9, -5])
        polygon = Polygon(e_polygon, True)
        self.patches.append(polygon)

        s_polygon = np.array(
            [[0, 0], [3, 0], [3, 2.4], [1, 2.4], [1, 3.2], [3, 3.2], [3, 4], [0, 4], [0, 1.6], [2, 1.6], [2, .8],
             [0, .8]]) + np.array([11.5, -5])
        polygon = Polygon(s_polygon, True)
        self.patches.append(polygon)

        bar_ploygon = np.array(
            [[0., 0.], [14.5, 0.],  [14.5, 1], [0,1]]) + np.array([0, -6.5])
        polygon = Polygon(bar_ploygon, True)
        self.patches.append(polygon)

    def plot(self):
        fig, ax = plt.subplots()
        colors = np.linspace(0, 9, 10)
        print(colors)
        p = PatchCollection(self.patches, alpha=0.8)
        p.set_array(np.array(colors))
        ax.add_collection(p)
        ax.set_ylim(-8, 6)
        ax.set_xlim(-1, 15)
        plt.axis('off')
        fig.colorbar(p, ax=ax)



    def generate_sample(self, number, n):
        polygon  = self.patches[n].get_verts()
        extend = [np.min(polygon[:, 0]), np.max(polygon[:, 0]),
                  np.min(polygon[:, 1]), np.max(polygon[:, 1])]
        bbPath = mplPath.Path(polygon)
        nr_points = 0
        points = []
        while  nr_points < number:
            xp = np.random.uniform(low=extend[0],high=extend[1], size=1)
            yp = np.random.uniform(low=extend[2],high=extend[3], size=1)
            coordinates = np.array([xp, yp])#np.dstack((xp,yp))[0]
            if bbPath.contains_point(coordinates):
                points.append(coordinates)
            nr_points = len(points)
        return np.array(points)




# instance = Sample_Cern_Letters()
#
# for i in range(10):
#     coordinates = instance.generate_sample(500, i)
#     plt.scatter(coordinates[:,0], coordinates[:,1],c='r')
#
# plt.show()