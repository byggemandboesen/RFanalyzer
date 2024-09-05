import numpy as np

# TODO - Optimize lumped component values for best matching
# TODO - Monte carlo sensitivity analysis on circuit

class Circuit:
    def __init__(self, components: list, stackup: "Stackup") -> None:
        '''
        Build a circuit from a list of components
        '''
        self.COMPONENTS = components
        self.STACKUP = stackup
    
    def __str__(self) -> str:
        '''
        TODO - Print circuit illustration
        '''
        pass

    def size(self) -> int:
        '''
        Return total number of components in circuit
        '''
        n = 0
        for i in range(len(self.COMPONENTS)):
            if len(self.COMPONENTS[i]) == 1:
                n += 0 if None in self.COMPONENTS[i] else 1
            else:
                add = Circuit(components=[[component] for component in self.COMPONENTS[i]], stackup=self.STACKUP).size()
                n += add

        return n

    def inputImpedance(self, f: float | np.ndarray) -> np.complex128 | np.ndarray:
        '''
        Calculate input impedance of circuit
        '''
        # Initially check that end of circuit is terminated
        if not self.COMPONENTS[-1][0].type == "Load":
            raise ValueError(f"Not terminating load was found! Got component type: {self.COMPONENTS[-1][0].type}")

        # Calculate input impedance
        Z_in = 0
        for i in range(len(self.COMPONENTS)):
            component = self.COMPONENTS[::-1][i][0]

            # Consider impedance of parallel branch
            if component == None:
                subcircuit = Circuit(components=[[component] for component in self.COMPONENTS[::-1][i][1:]], stackup=self.STACKUP)
                Z_in = 1/(1/Z_in+1/subcircuit.inputImpedance(f=f))
            else:
                match component.type:
                    case "Load":
                        Z_in = component.impedance
                    case "TL":
                        Z_in = component.inputImpedance(stackup=self.STACKUP, load_impedance=Z_in, f=f)
                    case "Lumped":
                        Z_in += component.impedance(f=f)
                    case _:
                        raise ValueError(f"Unexpected error occured when parsing component type: \"{component.type}\"")
            
        return Z_in
        
    def returnLoss(self, f: float | np.ndarray, Z_source: np.complex128 | np.ndarray) -> np.complex128 | np.ndarray:
        '''
        Calculate return loss of circuit
        '''
        Z_in = self.inputImpedance(f=f)
        
        return 20*np.log10(np.abs((Z_in-Z_source)/(Z_in+Z_source)))