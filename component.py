import numpy as np

class Component:
    def __init__(self, type: str) -> None:
        '''
        Parent class for all components

        Contains the component type (lumped, distributed etc)
        '''
        self.type = type