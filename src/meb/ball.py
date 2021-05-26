# import diameter, check_subset
from . import diameter, meb_solver

import numpy as np
import matplotlib.pyplot as plt

class Ball:
    """
    A class representing a ball with center and radius used to calculate minimum enclosing balls.
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
                n = len(data) # number of data points not in the core set
                m = len(self.core_set) # number of data points in the core set

                x = [data[i][0] for i in range(n)]
                y = [data[i][1] for i in range(n)]

                x_core = [self.core_set[i][0] for i in range(m)]
                y_core = [self.core_set[i][1] for i in range(m)]

                fig,ax = plt.subplots(figsize=(figsize,figsize))
                ax.set_aspect("equal")

                plt.scatter(x, y, color="blue", alpha=alpha, label="data")
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
        # if any point is not in the ball, switch out to false and break loop
        for x in data:
            if np.linalg.norm(x-self.center) > self.radius:
                out = False
                break

        return out

    def fit(self, data, eps):
        """
        does the thing
        """
        p = data[0]
        X = np.array(diameter.diameter_approx(p, data))
        delta = eps/163

        while True: # might want to set a max number of iterations
            c, r = meb_solver.MEB_solver(X) # compute MEB(X)
            r_dash = r*(1+delta) # get radius for (1+delta) approximation to MEB(X)
            temp_ball = Ball(c,r_dash*(1+eps/2)) # set temp ball

            if temp_ball.check_subset(data): # check if all the data is contained in temp ball
                self.center = c
                self.radius = temp_ball.radius
                self.core_set = X
                break
            else:
                p = diameter.find_furthest(c, data) # p = argmax_(x\in S) [||c'-x||]
            
            X = np.vstack((X,p)) # X := X U {p}
        return self