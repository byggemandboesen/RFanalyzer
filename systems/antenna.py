import numpy as np

class Antenna:
    def __init__(self, gain: float) -> None:
        '''
        Antenna class
        '''
        self.G = gain