import random
from typing import List
from diverging_trajectories.pattern.IntervalPatternRepository import IntervalPatternRepository
from diverging_trajectories.pattern.Pattern import Pattern
from diverging_trajectories.pattern.TrajectoryFixed import TrajectoryFixed
from diverging_trajectories.generator.TrajectoryGenerator import TrajectoryGenerator


class BumpyGenerator(TrajectoryGenerator):
    """Bumpy generator stiches patterns without any smoothing. We can only constrain in the heading difference
    """

    def __init__(self, patternRepository: IntervalPatternRepository, interval: float, maxHeadingDiff: float) -> None:
        """_summary_

        Args:
            patternRepository (IntervalPatternRepository): _description_
            interval (float): in meters
            maxHeadingDiff (float): in degrees
        """
        self.patternRepository = patternRepository
        self.interval = interval
        self.maxHeadingDiff = maxHeadingDiff
        pass


    def generateByRoundedOffset(self, n: int) -> List[TrajectoryFixed]:
        interval = int(self.interval)
        roundYOffset = 0
        segmentPatterns = self.patternRepository.getPatternsByHeadingStart(startPositive=True, roundYOffset=roundYOffset)
        trajPatterns = []
        for i in range(n):
            trajPatterns.append([random.choice(segmentPatterns)])

        roundYOffset += interval
        segmentPatterns = self.patternRepository.getPatternsByHeadingStart(startPositive=True, roundYOffset=roundYOffset)
        while len(segmentPatterns) > 0:
            for i in range(n):
                trajPatterns[i].append(random.choice(segmentPatterns))
            roundYOffset += interval
            segmentPatterns = self.patternRepository.getPatternsByHeadingStart(startPositive=True, roundYOffset=roundYOffset)
        
        combinedPatterns = [self.combinePatterns(patterns) for patterns in trajPatterns]
        return combinedPatterns
        
        

