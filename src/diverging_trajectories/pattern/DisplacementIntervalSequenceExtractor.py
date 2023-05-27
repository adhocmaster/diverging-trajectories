from typing import *
import pandas as pd
import logging
import math
from sortedcontainers import SortedList

from diverging_trajectories.pattern import Pattern
from diverging_trajectories.YupiUtils import YupiUtils
from diverging_trajectories.pattern.SequenceExtractor import SequenceExtractor


class DisplacementIntervalSequenceExtractor(SequenceExtractor):
    """This extractor discards if a pattern does not equal interval in length with a little bit of tolerance.

    Args:
        SequenceExtractor (_type_): _description_
    """
    
    def __init__(
            self,
            interval: float,
            tolerance: float, # fraction of interval
            yLow: float,
            yhigh: float,
            xCol: str, yCol: str
            ) -> None:
        self.interval = interval
        self.tolerance = tolerance
        self.yLow = yLow # now we can use incomplete trajectories
        self.yHigh = yhigh
        self.xCol = xCol
        self.yCol = yCol

        assert yLow < yhigh, "yLow must be less than yhigh"

        self.segmentOffsets = SortedList([])
        for offset in range(yLow, yhigh, interval):
            self.segmentOffsets.append(offset)

    def extract(self, trackId: str, track: pd.DataFrame) -> List[Pattern]:
        
        # corner cases
        # 1. may not start at yLow
        # 2. may not end at yHigh
        # 3. may not have enough points to form a pattern
        # 4. may not have enough points to form a pattern at the end
        # 5. may not have enough points to form a pattern at the beginning

        # now we walk along the track and extract patterns
        patternStarted = False
        yOffset = None
        patternRows = []
        for row in track.iterrows():
            if not patternStarted:
                # find the segment first
                yOffset = self.getSegmentOffset(row[self.yCol])




        raise NotImplementedError()
    
    def getSegmentOffset(self, y: float) -> float:
        """Get the offset of the segment that contains the y value.

        Args:
            y (float): y value

        Returns:
            float: offset of the segment
        """
        assert y >= self.yLow and y <= self.yHigh, f"y must be within the range of {self.yLow} and {self.yHigh}"
        idx = self.segmentOffsets.bisect_left(y)
        if y not in self.segmentOffsets:
            idx -= 1
        return self.segmentOffsets[idx]