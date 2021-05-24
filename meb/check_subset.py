import numpy as np

def check_subset(data, center, radius) -> bool:
    """
    Checks if the given data is a subset of the ball with a given center and radius
    
    Input:
        data (array like): data to check if its a subset of the ball
        center (array like): co-ordinate of the center of the ball
        radius (float): radius of the ball

    Return:
        out (bool): true if data is contained in the ball, false otherwise
    """
    out = True
    # if any point is not in the ball, switch out to false and break loop
    for x in data:
        if np.linalg.norm(x-center) > radius:
            out = False
            break

    return out