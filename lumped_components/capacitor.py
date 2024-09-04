import numpy as np

from RFanalyzer.lumped_components.lumped_component import LumpedComponent

class Capacitor(LumpedComponent):
    def __init__(self, capacitance: float) -> None:
        '''
        Capacitor class


        capacitance     - Capacitance in farad
        '''
        super().__init__(type='C', capacitance=capacitance)