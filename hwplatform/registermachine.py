
class RegisterMachine:
    def __init__(self, readFn, writeFn):
        self.readFn = readFn
        self.writeFn = writeFn
    
    def read(self, addr):
        return self.readFn(addr)
    
    def write(self, addr, value):
        result = self.writeFn(addr, value)
        if not result:
            raise RuntimeError(f"Write to addr {addr} with value {value} failed: {result}")
        return True
    
    def readBytes(self, addr, length, auto_increment = False):
        result = []
        for i in range(0, length):
            result.append(self.read(addr))
            if auto_increment:
                addr += 1
        
        return result
    
    def writeBytes(self, addr, data, auto_increment = False):
        for b in data:
            self.write(addr, b)
            if auto_increment:
                addr += 1