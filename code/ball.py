import diameter
import meb_solver

class Ball:
    """
    A class representing a ball with center and radius used to calculate minimum enclosing balls.
    """
    def __init__(self, center=None, radius=None, approx_diameter=None) -> None:
        self.center = center
        self.radius = radius
        self.approx_diameter = approx_diameter

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
        
        """
        p = data[0]
        X = list(diameter.diameter_approx(p, data))
        delta = eps/163

        #TODO: algorithm 1
        pass
