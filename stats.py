import csv


class Stats():
    """statistics"""
    def __init__(self):
        """stat init"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """reset values"""
        self.score = 0