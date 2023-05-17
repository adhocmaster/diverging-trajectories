from dataclasses import dataclass
from typing import *
from yupi import Trajectory
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
    
