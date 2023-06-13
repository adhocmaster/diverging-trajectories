from typing import List
from diverging_trajectories.pattern.IntervalPatternRepository import IntervalPatternRepository
from diverging_trajectories.pattern.Pattern import Pattern
from diverging_trajectories.pattern.TrajectoryFixed import TrajectoryFixed

class TrajectoryGenerator:

    def combinePatterns(self, patterns = List[Pattern]) -> Pattern:

        points = []
        interval  = 0
        for pattern in patterns:
            points.extend(pattern.points)
            interval += pattern.interval
        
        pattern = Pattern (
            sourceId = patterns[0].sourceId,
            interval = interval,
            patternSeqNo = patterns[0].patternSeqNo,
            points = points,
            t_0 = patterns[0].t_0,
            yOffset = patterns[0].yOffset
        )

        assert pattern.headingStart == patterns[0].headingStart
        assert pattern.headingEnd == patterns[-1].headingEnd
        
        return pattern
    