# Vocal: Voice Automated Lights

Vocal is a simple application written in Python that simulates the lights of a simple house with three rooms, following the client-server model. Each room is represented by a LED on a BeagleBone Black, that is turned on or off after a voice command given by the user.

## Setting up the BeagleBone Black

First you must configure the BeagleBone Black hardware. For Vocal, you'll need three different colored LEDs, three resistors and a few jumpers.
We've implemented like this:

<p align="center">
  <img src="https://github.com/vertumno/vocal/blob/master/docs/esquematico.jpeg?raw=true" alt="Implementation example"
       width="654" height="450">
</p>

To proceed, you'll need to install the [Adafruit Beaglebone I/O Python API](https://github.com/adafruit/adafruit-beaglebone-io-python) module on your BeagleBone.

Also, in the file [board_assets.py](https://github.com/vertumno/vocal/blob/master/src/server/board_assets.py), you'll find a dictionary named ```house```. It has as keys all the rooms and as values the GPIO pin number associated to that room. You can change this configuration to the one that suits more your needs, but remember to put LEDs, jumpers and resistors connecting everything properly.

## Setting up the server

For running the server, transfer to your BeagleBone the files [vocal_server.py](https://github.com/vertumno/vocal/blob/master/src/server/vocal_server.py) and [board_assets.py](https://github.com/vertumno/vocal/blob/master/src/server/board_assets.py).

Notice that in ```vocal_server.py```, right at the beginning of the file theres two constants: ```HOST``` and ```PORT```. You must type there the IP address of your BeagleBone to the ```HOST``` (e.g. "192.168.0.24") and a valid port (recommended a number up to 1024) number to ```PORT``` (e.g. 6000).

After this, simply run: ```python vocal_server.py``` and you should see something like this:

<p align="center">
  <img src="https://github.com/vertumno/vocal/blob/master/assets/server%20exec.png?raw=true" alt="Server running"
       width="500" height="400">
</p>

The server configured the GPIO and is ready to receive socket connections and perform the voice commands.

## Setting up the client

The client will stay on your machine. To set it up, you'll need to install PyAudio and SpeechRecognition, as described at [requirements.txt](https://github.com/vertumno/vocal/blob/master/requirements.txt). You can do this simply by:

* ```pip install -r requirements.txt```

Before running, you'll have to provide host and port for the socket in [vocal_client.py](https://github.com/vertumno/vocal/blob/master/src/client/vocal_client.py), the same way you've done on ```vocal_server.py```.

After this, and having successfully installed all the requirements, you can execute the code typing on your terminal: ```python vocal_client.py```.

If everything goes well, you should see a screen similar to this:

<p align="center">
  <img src="https://github.com/vertumno/vocal/blob/master/assets/client%2001.png?raw=true" alt="Client running">
</p>

Its okay if you see those messages that begin with "ALSA" on Ubuntu. If you want ro remove them, check [this out](https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time).

## Running Vocal

