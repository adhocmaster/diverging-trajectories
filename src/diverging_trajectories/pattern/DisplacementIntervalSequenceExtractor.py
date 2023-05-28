from typing import *
import pandas as pd
import logging
import math
from sortedcontainers import SortedList
import numpy as np

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
            yHigh: float,
            xCol: str, yCol: str
            ) -> None:
        self.interval = interval
        self.tolerance = tolerance
        self.yLow = yLow # now we can use incomplete trajectories
        self.yHigh = yHigh
        self.xCol = xCol
        self.yCol = yCol

        assert yLow < yHigh, "yLow must be less than yHigh"

        self.segmentOffsets = SortedList([])
        for offset in np.arange(yLow, yHigh, interval):
            self.segmentOffsets.add(offset)
        print(self.segmentOffsets)

    def extract(self, trackId: str, track: pd.DataFrame) -> List[Pattern]:
        
        # corner cases
        # 1. may not start at yLow
        # 2. may not end at yHigh
        # 3. may not have enough points to form a pattern
        # 4. may not have enough points to form a pattern at the end
        # 5. may not have enough points to form a pattern at the beginning

        # now we walk along the track and extract patterns
        patterns = []
        patternStarted = False
        yOffset = None
        patternRows = []
        seqNo = 0
        t_0 = 0.0
        for _, row in track.iterrows():
            if not patternStarted:
                # find the segment first
                yOffset = self.getSegmentOffset(row[self.yCol])
                patternStarted = True
                print(f"pattern started at {row[self.yCol]} with offset {yOffset}")
            
            if patternStarted:
                # check if we are still in the segment
                if row[self.yCol] > yOffset + self.interval:
                    # we are out of the segment, so we need to create a pattern
                    print(f"pattern end at {row[self.yCol]} with offset {yOffset}")

                    if len(patternRows) > 0:
                        # convert it to a pattern
                        pattern = Pattern.fromDataFrameRows(
                            sourceId=trackId,
                            interval=self.interval,
                            patternSeqNo=seqNo,
                            rows=patternRows,
                            xCol=self.xCol,
                            yCol=self.yCol,
                            t_0=t_0,
                            yLow=self.yLow
                        )
                    patterns.append(pattern)
                    t_0 += len(patternRows)
                    patternStarted = False
                    patternRows = []
                    seqNo += 1
                else:
                    # we are still in the segment
                    patternRows.append(row)

        return patterns

    
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