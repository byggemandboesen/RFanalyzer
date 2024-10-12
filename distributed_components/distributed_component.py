from abc import abstractmethod
import numpy as np

from RFanalyzer.component import Component

class DistributedComponent(Component):
    def __init__(self) -> None:
        super().__init__(type="Distributed")
    
    @abstractmethod
    def inputImpedance(self) -> np.complex128:
        '''
        Placeholder method for calculating input impedance of distributed component
        '''
        raise NotImplementedError("Not implemented for this type of distributed component!")
