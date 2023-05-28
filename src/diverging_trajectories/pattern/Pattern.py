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
        yOffset: float = None,
    ): 
        """_summary_

        Args:
            sourceId (str): _description_
            interval (float): _description_
            patternSeqNo (int): _description_
            points (Optional[Collection[Point]], optional): _description_. Defaults to None.
            t_0 (float, optional): _description_. Defaults to 0.0.
            yOffset (float, optional): yOffset is the relative distance along y-axis from the one side of the scene. Defaults to None.
        """
        
        self.sourceId = sourceId
        self.interval = interval
        self.patternSeqNo = patternSeqNo
        self.points = points
        self.yOffset = yOffset

        super().__init__(points=points, t_0=t_0)
    

    def __getitem__(self, index) -> Union[Trajectory, TrajectoryPoint]:
            if isinstance(index, int):
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
         minLen: int = 1,
         yLow: float = None,
         ) -> 'Pattern':

        points = [(row[xCol], row[yCol]) for i, row in patternDf.iterrows()]

        yOffset = None
        if yLow is not None:
             firstY = patternDf.iloc[0]["sceneY"]
             yOffset = firstY - yLow
             assert yOffset >= 0, f"yOffset={yOffset} < 0"

             
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
            t_0=t_0,
            yOffset=yOffset
        )
    @staticmethod
    def fromDataFrameRows(
         sourceId: str, 
         interval: float,
         patternSeqNo: int, 
         rows: List[pd.Series], 
         xCol: str, 
         yCol: str, 
         t_0: float = 0, 
         minLen: int = 1,
         yLow: float = None,
         ) -> 'Pattern':

        points = [(row[xCol], row[yCol]) for row in rows]

        yOffset = None
        if yLow is not None:
             firstY = rows[0]["sceneY"]
             yOffset = firstY - yLow
             assert yOffset >= 0, f"yOffset={yOffset} < 0"

             
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
            t_0=t_0,
            yOffset=yOffset
        )