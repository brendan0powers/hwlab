# Simulated Hardware

This example emulates a simple register machine.
Register machines consist of a chunk of adressable memroy.
You can read or write individual memory addresses to perform actions, and return results.

For example. Memory address 0 is a special status register.
When you read it, it will always return 100.
If you write a value to address 0, it has no effect.

Another example is memory address 100.
This address simulates a simple stack.
When you write a value to that adress, it is pushed onto the stack.
When you read a value from the address, it is popped from the stack.

See the registers section below for more information about the machines memory map.


## Serial Protocol

You can communicate with the hardware using a virtual serial port.
This port simulates a text-based, human readable serial interface to the hardware.
The protocol is line based, so every peice of data send or received by the hardware ends with a newline '\n'.

There are to possible actions, read data, and write data.
To read data, send a line starting with a lower case r, then the address to read.
The hardware will respond with the result.

To write, send a line starting with a lowercase w, followed by the address to write to, and the value to write.

### Examples

Read address 0
```
>>> r 0
<<< 100
```

Write adress 1
```
>>> w 1 123
<<< 0
```

Read address 1
```
>>> r 1
<<< 123
```

## Registers

| Address  | Description |
|----------|-------------|
| 0        | Always returns 100 when read, writes are ignored |
| 100      | Emulates a stack. Writing to the register pushed data to the stack, reading the register pops | 
| 200      | When written to, generates generates a signal with 100 datapoints. The result is places on registers 201-300. |
| 201-300  | See register 201 |
| *        | Will store a value when written to, and return it when read. The default value is 0 |

## How realistic is the simulation?

A register machine is a common pattern in hardware design.
It's used for devices as simple as I2C tempurature sensors, to complex logic in FPGAs.
Most microcontrollers also work this way, although accessing their memroy remotely via a serial port in the way simulated here would be unusual.

The biggest difference between the simulation and actual hardware is the data format.
The python simulation uses a normal python dictionary to store the data for each address.
This means you can use an arbitrarily large integer for the data, and for the address.
In most real hardware, memory addresses and data are limited to a fixed, and relativly small
number of bits.
8, 16 or 32 bits being common.

Another possible difference is in the serial protocol itself.
It's convenient, in that it's line based, and easy for humans to read.
Finding protocols like this is not unusual.
They have the advantage is making hardware easy to debug.
However, most hardware will opt to use a more efficient binary representation.
Instead of a line based protocol, you might have a dense binary format, with a fixed number of bytes.
For example, 1 byte for the command, and two for the address.