import numpy as np

from RFanalyzer.lumped_components.lumped_component import LumpedComponent

class Inductor(LumpedComponent):
    def __init__(self, inductance: float) -> None:
        '''
        Inductor class


        inductance      - Inductance in henry
        '''
        super().__init__(type='L', inductance=inductance)