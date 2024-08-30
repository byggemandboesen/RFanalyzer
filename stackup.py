import numpy as np

class Stackup:
    def __init__(self, er: float, ur: float, h: float) -> None:
        '''
        Stackup class used to calculate impedance of distributed components

        er      - Relative permittivity

        ur      - Relative permeability

        h       - Height of substrate (mm)
        '''
        self.er = er
        self.ur = ur
        self.H = h