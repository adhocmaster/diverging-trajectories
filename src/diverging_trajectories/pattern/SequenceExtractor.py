from abc import ABC, abstractmethod
from typing import *
import pandas as pd

from diverging_trajectories.pattern import Pattern
from diverging_trajectories.YupiUtils import YupiUtils

class SequenceExtractor(ABC):

    @abstractmethod
    def extract(self, track: pd.DataFrame) -> List[Pattern]:
        raise NotImplementedError()
    
    def validateSequence(self, patterns: List[Pattern]) -> bool:
        # sequence validity checks that the starting point of a Pattern is the ending point of the previous only
        prevPattern = None
        for pattern in patterns:
            if prevPattern is not None:
                prevEnd = prevPattern[-1]
                currStart = pattern[0]
                if not YupiUtils.areSamePointsInTime(prevEnd, currStart) # match pos and time

            prevPattern = pattern