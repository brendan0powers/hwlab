from .machine import Machine

machine = Machine()

class Port:
    def __init__(self):
        self.is_open = False
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
        machine.reset()
    
    def writeln(self, data):
        if not self.is_open:
            raise RuntimeError("Port not open")
        machine.write(data)
    
    def readln(self):
        if not self.is_open:
            raise RuntimeError("Port not open")
        return machine.read()