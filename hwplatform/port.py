from .machine import Machine
import time

machine = Machine()

class Port:
    def __init__(self):
        self.is_open = False
        self.on_read = None
        self.on_write = None
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
        machine.reset()
    
    def writeln(self, data):
        if not self.is_open:
            raise RuntimeError("Port not open")
        machine.write(data)
        time.sleep(0)
        if self.on_write:
            self.on_write(data)
    
    def readln(self):
        if not self.is_open:
            raise RuntimeError("Port not open")
        data = machine.read()
        time.sleep(0)
        if self.on_read:
            self.on_read(data)
        return data