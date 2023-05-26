from .db import db
from typing import List
from diverging_trajectories.pattern import Pattern
from diverging_trajectories.pattern.IntervalPatternSequence import IntervalPatternSequence
from diverging_trajectories.pattern.PatternModel import PatternModel
from diverging_trajectories.pattern.PatternSequence import PatternSequence


class PatternCollection:
    def __init__(self) -> None:
        pass


    def addSequence(self, sourceId: str, interval: float, patterns: List[Pattern]) -> IntervalPatternSequence:
        seqModel = IntervalPatternSequence.create(sourceId, interval=interval)
        for i, pattern in enumerate(patterns):
            PatternModel.create(
                sourceId = seqModel.sourceId,
                interval = seqModel.interval,
                patternSeqNo = i,
                points = pattern.points,
                t_0 = pattern.t_0,
                sequence = seqModel
            )
        return seqModel
    
    def getSequences(self) -> List[IntervalPatternSequence]:
        return IntervalPatternSequence.get()
    

    def getPatterns(self, patternSize: int) -> List[Pattern]:
        return Pattern.get(Pattern.patternSize == patternSize)