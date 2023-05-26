from dataclasses import dataclass
import pandas as pd
from typing import *
from yupi import Trajectory, TrajectoryPoint
from yupi.trajectory import Axis, Point

class Pattern(Trajectory):
    
    def __init__(
        self,
        sourceId: str,
        interval: float,
        patternSeqNo: int,
        points: Optional[Collection[Point]] = None,
        t_0: float = 0.0,
    ): 
        
        self.sourceId = sourceId
        self.interval = interval
        self.patternSeqNo = patternSeqNo
        self.points = points
        super().__init__(points=points, t_0=t_0)
    

    def __getitem__(self, index) -> Union[Trajectory, TrajectoryPoint]:
            index = index % len(self.r)
            return super().__getitem__(index) # fix
    
    @staticmethod
    def fromDataFrame(
         sourceId: str, 
         interval: float,
         patternSeqNo: int, 
         patternDf: pd.DataFrame, 
         xCol: str, 
         yCol: str, 
         t_0: float = 0, 
         minLen: int = 1
         ) -> 'Pattern':

        points = [(row[xCol], row[yCol]) for i, row in patternDf.iterrows()]
        # print(points)
        if minLen > len(points):
            toCopy = minLen - len(points)
            lastPoint = points[-1]
            points.extend([lastPoint] * toCopy)
            
        return Pattern(
            sourceId=sourceId,
            interval=interval,
            patternSeqNo=patternSeqNo,
            points=points,
            t_0=t_0
        )