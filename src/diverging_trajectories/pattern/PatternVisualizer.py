from typing import List
import matplotlib.pyplot as plt
from yupi.graphics import plot_2d

from diverging_trajectories.pattern.Pattern import Pattern

class PatternVisualizer:

    def plotPatterns(
            self,
            patterns: List[Pattern],
            hLines: List[float] = None,
            xmin: float = None,
            xmax: float = None,
            title: str = None,
            legend: bool = True,
        ):

        ax = plot_2d(patterns, show=False, legend=legend)
        if title is not None:
            ax.set_title(title)
        if hLines is not None:
            ax.hlines(hLines, colors="gray", linestyles='dotted', xmin=xmin, xmax=xmax)
            ax.set_xlim(xmin, xmax)
        plt.show()