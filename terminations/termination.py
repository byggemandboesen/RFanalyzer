import numpy as np

class Load:
    def __init__(self, impedance: np.complex128 | np.ndarray) -> None:
        '''
        Load parent class
        '''
        self.impedance = impedance

class Open(Load):
    def __init__(self) -> None:
        '''
        Open load
        '''
        super().__init__(impedance=np.inf)

class Short(Load):
    def __init__(self) -> None:
        '''
        Short load
        '''
        super().__init__(impedance=0)