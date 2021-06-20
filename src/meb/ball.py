import numpy as np
import matplotlib.pyplot as plt

from . import meb_algorithms, mebwo_algorithms, geometry

class Ball:
    """
    A class representing a ball with center and radius

    Attributes:
        center (array like): center of the ball
        radius (float): radius of the ball
        core_set (array like): the core set used to find the MEB of the data the ball is fit to
    
    Methods:
        plot (None): plots the fit ball if it is dimension 2 or 3
        check_subset (bool): checks if a given data set is a subset of the ball
    """
    def __init__(self, center=None, radius=None, core_set=None) -> None:
        self.center = center
        self.radius = radius
        self.core_set = core_set

    def __str__(self) -> str:
        return (
            "Center:\t{}\n".format(self.center) +
            "Radius:\t{}".format(self.radius)
        )

    def check_params(self) -> True:
        """
        Checks if the center and radius of the ball have been set, if not raise ValueError()

        Input:
            None
        Return:
            bool: True if center and radius are set
        """
        if self.center is None or self.radius is None:
            raise ValueError("Center/radius not set")
        
        yield True # if center and radius have been set, assume they will not be un-set
    
    def contains(self, x) -> bool:
        """
        Checks if x is inside the ball

        Input:
            x (array like): data point to check if it is inside the ball
        
        Return:
            out (bool): True if x is inside the ball, False otherwise
        """
        # don't check_params here since this is called repeatedly by check_subset()
        out = np.linalg.norm(x-self.center) <= self.radius
        return out

    def check_subset(self, data) -> bool:
        #TODO: check if theres a better way of doing this
        """
        Checks if the given data is a subset of the ball
        
        Input:
            data (array like): data to check if its a subset of the ball

        Return:
            out (bool): true if data is contained in the ball, false otherwise
        """
        self.check_params()
        # if any point is not in the ball, switch out to false and break loop
        out = True
        for x in data:
            if not self.contains(x):
                out = False
                break

        return out

    def plot(self, data, alpha=1, figsize=8, show=True) -> None:
        """
        Plots the given data with the minimum enclosing ball if dimension is 1,2, or 3

        Input:
            data (array like): data to be plotted
            alpha (float): opacity from 0 to 1 for data points
            figsize (float): size of the figure (1:1 aspect ratio)
            show (bool): whether to call plt.show() or not
        
        Return:
            None
        """
        self.check_params()
        
        dimension = len(self.center)

        if dimension == 2:
            fig,ax = plt.subplots(figsize=(figsize,figsize))
            plt.gca().set_aspect('equal')

            n = len(data) # number of data points not in the core set
            x = [data[i][0] for i in range(n)]
            y = [data[i][1] for i in range(n)]

            plt.scatter(x, y, color="blue", alpha=alpha, label="data")    
            
            if self.core_set is not None:
                m = len(self.core_set) # number of data points in the core set
                x_core = [self.core_set[i][0] for i in range(m)]
                y_core = [self.core_set[i][1] for i in range(m)]
                
                plt.scatter(x_core, y_core, color="orange", label="core set")

            plt.scatter(self.center[0], self.center[1], color="red", marker="x", label="center")
            ax.add_patch(
                plt.Circle(self.center, self.radius, color="red", fill=False, label="ball")
            )
            
            if show:
                plt.legend()
                plt.show()

        elif dimension == 3:
            #TODO: plot for 3d
            pass
        else:
            print("Can not plot MEB for dimension {}".format(dimension))

        return None

    def distance_graph(self, data):
        #TODO: document this method if its useful
        n = len(data)
        mean = geometry.mean_vector(data)

        distances = {i: np.linalg.norm(data[i]-mean) for i in range(n)}
        sorted_distances = {index: dist for index, dist in sorted(distances.items(), key=lambda item: item[1])}

        #TODO: refactor this as a function
        dist = list(sorted_distances.values())
        gradients_list = [dist[i+1]-dist[i] for i in range(len(dist)-1)]
        gradients = {index: gradient for index, gradient in zip(sorted_distances.keys(), gradients_list)}
    
        dist2 = list(gradients.values())
        gradients_list2 = [dist2[i+1]-dist2[i] for i in range(len(dist2)-1)]
        gradients2 = {index: gradient for index, gradient in zip(gradients.keys(), gradients_list2)}

        fig, ax = plt.subplots(1,3, figsize=(12,4))
        ax[0].plot(range(n), sorted_distances.values())
        ax[1].plot(range(n-1), gradients.values())
        ax[2].plot(range(n-2), gradients2.values())
        plt.show()
        return None

class MEB(Ball):
    """
    Extends meb.Ball
    A Ball object used to calculate minimum enclosing balls.

    Methods:
        fit (Ball): fits the MEB to the given data
    """
    def __init__(self, center=None, radius=None, core_set=None) -> None:
        super().__init__(center=center, radius=radius, core_set=core_set)
    
    def fit(self, data, method="heuristic", **kwargs):
        """
        Fits a MEB to the given data using the specified method

        Input:
            data (array like): data to fit the MEB to
            method (str): which method to use to find MEB
        
        Return:
            self (Ball): the MEB for the data
        """
        # get the function corresponding to method
        algorithm = meb_algorithms.algorithms.get("alg_{}".format(method)) # returns none if 'alg_method' not in algorithms dict
        if algorithm is None:
            raise NotImplementedError("Method '{}' not implemented".format(method))
        
        c, r, X = algorithm(data, **kwargs)

        self.center = c
        self.radius = r
        self.core_set = X
        
        return self

class MEBwO(MEB):
    """
    Extends MEB
    A ball object used to calculate minimum enclosing balls with outliers
    """
    def __init__(self, center=None, radius=None, core_set=None, pct_containment=None) -> None:
            super().__init__(center=center, radius=radius, core_set=core_set)
            self.pct_containment = pct_containment
        
    def __str__(self) -> str:
        return (
            super().__str__() + "\n" +
            "Cont:\t{}".format(self.pct_containment)
        )
    
    def fit(self, data, method, calc_pct=False, **kwargs):
        #TODO: refactor input sanitation and algorithm retrieval
        # get the function corresponding to method
        algorithm = mebwo_algorithms.algorithms.get("alg_{}".format(method)) # returns none if 'alg_method' not in algorithms dict
        if algorithm is None:
            raise NotImplementedError("Method '{}' not implemented".format(method))

        c, r, xi = algorithm(data, **kwargs)

        self.center = c
        self.radius = r

        if calc_pct:
            self.calc_pct(data)

        return self

    def calc_pct(self, data) -> float:
        """
        Finds what % of points in data are inside the ball

        Input:
            data (array like): data to check
        
        Return:
            pct (float): percentage of points contained in the ball
        """
        n = len(data) # total number of points
        inside = 0 # number of points inside the ball

        for x in data:
            if self.contains(x):
                inside += 1

        pct = inside/n
        self.pct_containment = pct
        return pct

    def plot(self, data, alpha=1, figsize=8, show=True) -> None:
        """
        Plots the MEBwO

        Input:
            data (array like): data to be plotted
            alpha (float): opacity from 0 to 1 for data points
            figsize (float): size of the figure (1:1 aspect ratio)
            show (bool): whether to call plt.show() or not
        
        Return:
            None
        """

        self.check_params()
        dimension = len(self.center)

        if dimension == 2:
            inliers = [x for x in data if self.contains(x)]
            outliers = [x for x in data if not self.contains(x)]

            super().plot(data=inliers, alpha=alpha, figsize=figsize, show=False)

            k = len(outliers)
            #TODO: refactor this as a function
            x_outliers = [outliers[i][0] for i in range(k)]
            y_outliers = [outliers[i][1] for i in range(k)]
            plt.scatter(x_outliers, y_outliers, color="g", alpha=alpha, label="outliers")   

            if show:
                plt.legend()
                plt.show()
        
        return None