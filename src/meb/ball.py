import diameter, check_subset
import meb_solver # comment out if not connected to the VPN 

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

    def plot(self, data) -> None:
        """
        Plots the given data with the minimum enclosing ball if dimension is 1,2, or 3

        Input:
            data (array like): data to be plotted
        
        Return:
            None
        """
        if self.center == None:
            print("MEB has not been computed")
        elif len(self.center) in [1,2,3]: 
            #TODO: plot for dimensions 1, 2, or 3
            pass
        else:
            print("Can not plot MEB for dimension")

        return None

    def set_approx_diameter(self, data) -> None:
        # is this even needed?
        pass

    def fit(self, data, eps) -> None:
        """
        does the thing
        """
        p = data[0]
        X = np.array(diameter.diameter_approx(p, data))
        delta = eps/163

        while True:
            c, r = meb_solver.MEB_solver(X) # compute MEB for X
            if check_subset.check_subset(data, c, r): # check if all the data is contained in this ball
                self.center = c
                self.radius = r
                self.core_set = X
                break
            else:
                p = diameter.find_furthest(c, data) # p = argmax_(x\in S) [||c'-x||]
            
            X = np.append(X,p)
        return None
