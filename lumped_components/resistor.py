import numpy as np

from RFanalyzer.lumped_components.lumped_component import LumpedComponent

class Resistor(LumpedComponent):
    def __init__(self, resistance: float) -> None:
        '''
        Resistor class


        resistance      - Resistance in ohms
        '''
        super().__init__(type='R', resistance=resistance)