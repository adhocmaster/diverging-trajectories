from yupi import Trajectory, TrajectoryPoint
import numpy as np

class YupiUtils:

    @staticmethod
    def haveSamePos(p1: TrajectoryPoint, p2: TrajectoryPoint) -> bool:
        return np.array_equal(p1.r, p2.r)

    @staticmethod
    def areSamePointsInTime(p1: TrajectoryPoint, p2: TrajectoryPoint) -> bool:
        return YupiUtils.haveSamePos(p1, p2) and p1.t == p2.t
