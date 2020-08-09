[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/brendan0powers/hwlab/master?urlpath=lab) Try this out right from your browser!

# Hardware Prototyping with Jupyter Lab

This is a POC exploring the possibility of using Jupyter notebooks to quickly test prototype hardware.
Instead of building bespoke test software from scratch, we can leverage the power of the python
interpreter, along with some helper APIs to quickly build a test harness, and then iterate from there.

A simple [API](./API.md) is provided that will help with the most common tasks when communicating and degging hardware. To make things simpler, a [simulated deive](./Simulated%20Hardware.md) is provided.

Try to use the API to interact with the hardware!

[Start Here](./Start%20Here.ipynb)

## Things to try

* Open a serial port, and communicate with the simulated hardware
* Use the ReigsterMachine class to make communicating with the hardware easier
* Try out the UI helpers registerReader, and registerWriter
* Generate some with register 200, and then plot the resulting data
* Attach a serial monitor to see the communications with the hardware

## Links
* Documentation for the [Simulated Hardware](./Simulated%20Hardware.md)
* [API Documentation](./API.md)
* If you get stuck, have a look at the [example notebook](./examples/Example%20Notebook.ipynb)