import numpy as np
import scipy.stats as stats

class Machine:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.registers = {}
        self.read_buffer = []
    
    def write(self, data):
        parts = data.split(' ');
        addr = int(parts[1])
        
        if parts[0] == 'r':
            result = self.read_register(addr)
            self.read_buffer.append(result)
        else:
            value = int(parts[2])
            status = self.write_register(addr, value)
            self.read_buffer.append(status)
    
    def read(self):
        if self.read_buffer:
            return self.read_buffer.pop(0)
        else:
            return ""
    
    def write_register(self, register, value):
        if register == 200:
            mu = 0
            std = value
            x = np.linspace(start=-4, stop=4, num=100)
            y = stats.norm.pdf(x, mu, std)
            
            for i in range(0, 100):
                self.registers[201+i] = y[i]*1000
        
        self.registers[register] = value;
        return 0
        
    def read_register(self, register):
        return self.registers.get(register, 0)