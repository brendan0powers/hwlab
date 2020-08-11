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

### openSerialPort(default_port=None, auto_open=False): Port
Displays a serial port widget allowing the user to select from the available ports.
A Port object is returned.

#### Arguments
* `default_port: string`: Selects the specified port
* `auto_open: bool`: Returns an opened port object. Uses the first available port if `default_port` is not specified.

#### Return Value
Returns a Port object.

#### Example

```python
# Show the widget with no options
port = openSerialPort()

# Show the widget, but also open COM3
port = openSerialPort(default_port="COM3", auto_open=True)
```

### registerReader(register_machine)
Creates a widget that let's the user read registers

#### Arguments
* `register_machine: RegisterMachine`: A RegisterMachine instance to use for reading registers

#### Return Value
None

#### Example

```python
machine = RegisterMachine(readFn, writeFn)
registerReader(machine)
```

### registerWriter(register_machine)
Creates a widget that let's the user write registers

#### Arguments
* `register_machine: RegisterMachine`: A RegisterMachine instance to use for writing registers

#### Return Value
None

#### Example

```python
machine = RegisterMachine(readFn, writeFn)
registerWriter(machine)
```

### plot(data)
Takes an array of numbers, and draws a graph with them.

#### Arguments
* `data: [numbers]`: An array of numbers to plot

#### Return Value
None

#### Example

```python
plot([1, 2, 3, 4])
```

### serialMonitor(port)
Displays any data read or written from a Port object.

#### Arguments
* `port: Port`: a Port object to monitor

#### Return Value
None

#### Example

```python
port = openSerialPort()
serialMonitor(port)
```