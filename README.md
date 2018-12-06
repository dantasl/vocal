# Vocal: Voice Automated Lights

Vocal is a simple application written in Python that simulates the lights of a simple house with three rooms, following the client-server model. Each room is represented by a LED on a BeagleBone Black, that is turned on or off after a voice command given by the user.

## Setting up the BeagleBone Black

First you must configure the BeagleBone Black hardware. For Vocal, you'll need three different colored LEDs, three resistors and a few jumpers.
We've implemented like this:

<p align="center">
  <img src="https://github.com/vertumno/vocal/blob/master/docs/esquematico.jpeg?raw=true" alt="Implementation example"
       width="654" height="450">
</p>

Also, you'll need to install the [Adafruit Beaglebone I/O Python API](https://github.com/adafruit/adafruit-beaglebone-io-python) module on your BeagleBone.

## Setting up the server
