## API Documentation

## Hardware Helpers

### Port
The Port class simulates a serial port.
You can open and close the port, check it's status, read and write lines.

#### Methods
* `constructor Port():` Creates a port, and takes no arguments. The port is closed by default.
* `open():` Opens the port
* `close():` Closes the port, and re-sets the virtual hardware
* `readLn():` Reads a line of text, stopping at the first newline '\n' found. The data is returned, and the trailing newline is omitted.
* `wirteLn(data):` Writes a line of text, automatically appending a newline '\n'

#### Properties
* `is_open:` Boolean, indicating weather the port is open.

#### Example
```python
port = Port()
port.open()
print(port.is_open)
port.writeLn("Some data to send")
print(port.readLn())
```

### RegisterMachine

#### Methods
* `constructor RegisterMachine(readFn, writeFn):` Creates a new ReigsterMachine instance. Takes a read function and write function as parameters. See the example for more information on read and write functions.
* `read(address):` Reads the register at the specified address, and returns the value
* `write(address, value):` Writes the given value to the provided address. Throws an exceptoin on write failure.
* `readBytes(address, num_bytes, auto_increment=False):` Reads a series of bytes from the provided address. If auto increment is set to False, the same address is read num_bytes times. If auto_increment is set to true, then for each read, the address is incremented by one. This is useful for reading a range of addresses.
* `writeBytes(address, data, auto_increment=False):` Writes a series of bytes to an address. If auto increment is set to False, the same address is written to for each byte provided. If auto_increment is set to true, then for each byte, the address is incremented by one. This is useful for writing to a range of addresses.

#### Example
```python
# Takes the register address as the argument, returns the data
def readFn(addr):
    return 0

# Takes the register address and value to write as arguments.
# Returns true if the write was successful, false otherwise
def writeFn(addr, value)
    return True

machine = RegisterMachine(readFn, writeFn)
machine.write(1, 123)
machine.read(1)
print(machine.readBytes(2, 8, auto_increment=True))
```

## UI Helpers

### openSerialPort(name=None, auto_open=False)

### registerReader(register_machine)

### registerWriter(register_machine)

### plot(data)

### serialMonitor(port)