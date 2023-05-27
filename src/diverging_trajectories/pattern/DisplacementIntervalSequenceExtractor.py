from typing import *
import pandas as pd
import logging
import math

from diverging_trajectories.pattern import Pattern
from diverging_trajectories.YupiUtils import YupiUtils
from diverging_trajectories.pattern.SequenceExtractor import SequenceExtractor


class DisplacementIntervalSequenceExtractor(SequenceExtractor):
    
    def __init__(
            self,
            interval: float
            ) -> None:
        self.interval = interval

    def extract(self, trackId: str, track: pd.DataFrame) -> List[Pattern]:
        raise NotImplementedError()