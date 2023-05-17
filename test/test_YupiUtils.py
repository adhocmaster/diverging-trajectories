from yupi import Trajectory, TrajectoryPoint

from src.diverging_trajectories.YupiUtils import YupiUtils

import numpy as np

def test_areSamePointsInTime():
    traj1 = Trajectory(points=[[1,2], [3,3], [4,2]])
    traj2 = Trajectory(points=[[1,2], [3,3], [4,2]])

    p1 = traj1[0]
    p2 = traj2[0]

    print(p1, p2)
    assert YupiUtils.haveSamePos(p1, p2)
    assert YupiUtils.haveSamePos(p1, traj2[1]) == False