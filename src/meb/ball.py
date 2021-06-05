from . import geometry, socp_solver

import numpy as np
import matplotlib.pyplot as plt

class Ball:
    """
    A class representing a ball with center and radius

    Attributes:
        center (array like): center of the ball
        radius (float): radius of the ball
        approx_diameter (float): approximate diameter of the ball (estimated)
        core_set (array like): the core set used to find the MEB of the data the ball is fit to
    
    Methods:
        plot (None): plots the fit ball if it is dimension 2 or 3
        check_subset (bool): checks if a given data set is a subset of the ball
    """
    def __init__(self, center=None, radius=None, approx_diameter=None, core_set=None) -> None:
        self.center = center
        self.radius = radius
        self.approx_diameter = approx_diameter
        self.core_set = core_set

    def __str__(self) -> str:
        return (
            "Center:\t {}\n".format(self.center) +
            "Radius:\t {}\n".format(self.radius) +
            "Approximate diameter:\t {}".format(self.approx_diameter)
        )

    def plot(self, data, alpha=1, figsize=8) -> None:
        """
        Plots the given data with the minimum enclosing ball if dimension is 1,2, or 3

        Input:
            data (array like): data to be plotted
            alpha (float): opacity from 0 to 1 for data points
            figsize (float): size of the figure (1:1 aspect ratio)
        
        Return:
            None
        """
        if self.center is None:
            print("MEB has not been computed")
        else:
            dimension = len(self.center)
            if dimension == 1:
                print("Why do you want to plot for dimension 1?")
            elif dimension == 2:
                fig,ax = plt.subplots(figsize=(figsize,figsize))
                
                
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
                
                plt.legend()

                plt.show()
            elif dimension == 3:
                #TODO: plot for 3d
                pass
            else:
                print("Can not plot MEB for dimension {}".format(dimension))

        return None

    def set_approx_diameter(self, data) -> None:
        # is this even needed?
        pass

    def check_subset(self, data) -> bool:
        #TODO: check if theres a better way of doing this
        """
        Checks if the given data is a subset of the ball
        
        Input:
            data (array like): data to check if its a subset of the ball

        Return:
            out (bool): true if data is contained in the ball, false otherwise
        """
        out = True
        if self.center is None:
            print("MEB has not been computed")
            out = False
        else:
            # if any point is not in the ball, switch out to false and break loop
            for x in data:
                if np.linalg.norm(x-self.center) > self.radius:
                    out = False
                    break

        return out

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
    def __init__(self, center=None, radius=None, approx_diameter=None, core_set=None) -> None:
        super().__init__(center=center, radius=radius, approx_diameter=approx_diameter, core_set=core_set)
    
    def fit(self, data, method="heuristic", eps=1e-4):
        """
        Fits a MEB to the given data using the specified method

        Input:
            data (array like): data to fit the MEB to
            method (str): which method to use to find MEB ("heuristic" or "exact")
            eps (float): error tolerance if using heuristic
        
        Return:
            self (Ball): the MEB for the data
        """
        if method == "exact": # solves the exact optimisation problem for MEB
            c, r = socp_solver.socp_solver(data)
            self.center = c
            self.radius = r
        
        elif method == "socp_heuristic": # algorithm 1 https://dl.acm.org/doi/10.1145/996546.996548
            p = data[0]
            X = np.array(geometry.diameter_approx(p, data))
            delta = eps/163

            while True: # might want to set a max number of iterations
                c, r = socp_solver.socp_solver(X) # compute MEB(X)
                r_dash = r*(1+delta) # get radius for (1+delta) approximation to MEB(X)
                temp_ball = Ball(c,r_dash*(1+eps/2)) # set temp ball

                if temp_ball.check_subset(data): # check if all the data is contained in temp ball
                    self.center = c
                    self.radius = temp_ball.radius
                    self.core_set = X
                    break
                else:
                    p = geometry.find_furthest(c, data) # p = argmax_(x\in S) [||c'-x||]
                
                X = np.vstack((X,p)) # X := X U {p}
        
        else:
            raise ValueError("Invalid/unknown method passed to MEB.fit()")
        
        return self

class MEBwo(Ball):
    """
    A ball object used to calculate minimum enclosing balls with outliers
    """
    def __init__(self, center=None, radius=None, approx_diameter=None, core_set=None) -> None:
            super().__init__(center=center, radius=radius, approx_diameter=approx_diameter, core_set=core_set)