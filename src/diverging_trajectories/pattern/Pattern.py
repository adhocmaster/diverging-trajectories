from dataclasses import dataclass
from typing import *
from yupi import Trajectory, TrajectoryPoint
from yupi.trajectory import Axis, Point

class Pattern(Trajectory):
    
    def __init__(
        self,
        sourceId: str,
        patternSeqNo: int,
        points: Optional[Collection[Point]] = None,
        t0: Optional[float] = None,  
    ): 
        self.sourceId = sourceId
        self.patternSeqNo = patternSeqNo
        super().__init__(points=points, t0=t0)
    

    def __getitem__(self, index) -> Union[Trajectory, TrajectoryPoint]:
            index = index % len(self.r)
            return super().__getitem__(index) # fix