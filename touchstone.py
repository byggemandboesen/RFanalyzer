import skrf
import numpy as np
import matplotlib.pyplot as plt

class Touchstone:
    def __init__(self, path: str, format: str = "DB") -> None:
        '''
        Create Touchstone object from .snp file path


        path    - Path to touchstone file

        format  - Format to parse touchstone file
        '''
        self.PATH = path
        # Read touchstone file
        self.NETWORK = skrf.Network(self.PATH)
        
        # Retrieve data
        self.f = self.NETWORK.f
        match format.upper():
            case "DB":
                self.s = self.NETWORK.s_db
            case "MA":
                self.s = self.NETWORK.s_mag
            case "RI":
                self.s = self.NETWORK.s_re
                self.p = self.NETWORK.s_im
        
        self.p = self.NETWORK.s_deg
        self.Z = self.NETWORK.z

    def parameters(self) -> str:
        '''
        Return network parameters
        '''
        return self.NETWORK.params
    
    def comments(self) -> str:
        '''
        Return network comments
        '''
        return self.NETWORK.comments

    def frequency(self) -> np.ndarray:
        '''
        Get frequency axis of touchstone file
        '''
        return self.f
    
    def S11(self) -> tuple[np.ndarray, np.ndarray]:
        '''
        Return return loss and phase
        '''
        return self.s[:,0,0], self.p[:,0,0]
    
    def S21(self) -> tuple[np.ndarray, np.ndarray]:
        '''
        Return insertion loss and phase
        '''
        return self.s[:,1,0], self.p[:,1,0]
    
    def plot(self) -> None:
        '''
        Show plot of S11 and S21
        '''
        f = self.frequency()
        s11, _ = self.S11()
        s21, _ = self.S21()
        
        plt.plot(f, s11, label="S11")
        plt.plot(f, s21, label="S21")

        plt.xlim((f[0], f[-1]))
        plt.grid(alpha=0.5)
        plt.legend()
        plt.show()

# s[:,0,0] = s11
# s[:,0,1] = s12
# s[:,1,0] = s21
# s[:,1,1] = s22