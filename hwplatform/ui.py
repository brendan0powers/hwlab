import ipywidgets as widgets
from IPython.display import display, Javascript
import numpy as np
import matplotlib.pyplot as plt
from .port import Port

def openSerialPort(auto_open=False, default_port=None):
    port = Port()
    
    button = widgets.Button(description="Open Port")
    label = widgets.Label(value="Closed")
    
    w = widgets.Dropdown(
        options=['one', 'two', 'three'],
        value= default_port if default_port else 'two',
        disabled=False
    )
    
    def on_open(b):
        if port.is_open:
            label.value = "Closed"
            w.disabled=False
            button.description="Open Port"
            port.close()
        else:
            label.value = f"Opened port: {w.value}"
            w.disabled=True
            button.description="Close Port"
            port.open()
            
    button.on_click(on_open)
    
    layout = widgets.HBox(
        [widgets.Label(value="Port"), w, button, label],
        layout=widgets.Layout(
            justify_content="flex-start",
            gap="10px"
        )
    )
    
    display(layout)
    
    if auto_open:
        on_open(None)
    
    return port

def registerReader(machine):
    label = widgets.Label(value="Read Register")
    inputV = widgets.Text(
        value='',
        placeholder='###',
        disabled=False
    )
    button = widgets.Button(description="Read")
    value = widgets.Label(value="")
    
    layout = widgets.HBox(
        [label, inputV, button, value],
        layout=widgets.Layout(
            justify_content="flex-start",
            gap="10px"
        )
    )
    
    def on_read(b):
        addr = int(inputV.value)
        result = machine.read(addr)
        value.value = str(result)
    
    button.on_click(on_read)
    
    display(layout)
    
def registerWriter(machine):
    label = widgets.Label(value="Read Register")
    inputV = widgets.Text(
        value='',
        placeholder='###',
        disabled=False
    )
    valueV = widgets.Text(
        value='',
        placeholder='###',
        disabled=False
    )
    button = widgets.Button(description="Write")
    
    layout = widgets.HBox(
        [label, inputV, valueV, button],
        layout=widgets.Layout(
            justify_content="flex-start",
            gap="10px"
        )
    )
    
    def on_write(b):
        addr = int(inputV.value)
        value = int(valueV.value)
        result = machine.write(addr, value)
    
    button.on_click(on_write)
    
    display(layout)
    
def plot(data):
    x = np.linspace(start=0, stop=len(data), num=len(data))
    y = data
    plt.plot(x, y)
    plt.show()