ubit-usb
=============
https://github.com/urban-martin/ubit-usb


Description:
---
ubit-usb consists of two pieces.  One is a program written in C++ that runs on a BBC MicroBit device and exports temperature, pitch, and roll data over USB/Serial.  This data is taken from the embedded temperature sensor and acceleromater.

The second piece is a python script that listens on a USB/Serial port, parses the incoming data, and relays that data to Wekinator via OSC (three continuous inputs).

This could be used for many purposes, from controlling an electronic instrument to recording telemetry data from a drone.


Compiling:
---
For the program that runs the MicroBit, a pre-compiled binary has been included for convenience (microbit-temp-pitch_roll.hex).  It should be copied to the MicroBit device by accessing it as a USB drive.  If you want to modify the source (mb_sensors.cpp) or compile it manually for some other reason, the easiest way is to use the web-based IDE and compiler (https://developer.mbed.org/compiler).  Alternatively, the source can be compiled using a standard C++ compiler.  The MicroBit.h library is required in this case.

The feature extractor (ubit-extractor.py) requires Python 2.7, and the serial and pyOSC libraries.  The serial library should be readily available.  Version 0.3.5b of pyOSC is required (it supports Python 2.x).


Use:
---
To run the feature extractor, it may be necessary to modify serial_path or other configuration variables.  On a Macbook, the path to the MicroBit USB/Serial device can be found by running "ls /dev/cu.*".  It should have the form "/dev/cu.usbmodemFD132".


Inputs:
---
Input-1: temperature
Input-2: pitch
Input-3: roll
