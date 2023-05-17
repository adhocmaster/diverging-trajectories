from yupi import Trajectory, TrajectoryPoint
import numpy as np

class YupiUtils:

    @staticmethod
    def haveSamePos(p1: TrajectoryPoint, p2: TrajectoryPoint) -> bool:
        return np.array_equal(p1.r, p2.r)
