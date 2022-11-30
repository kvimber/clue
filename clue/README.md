# Clue Application

This app runs on the CLUE hardware, reporting its measurements & status

The app's current state is not much more than the
[initial example (adafruit/Adafruit_CircuitPython_CLUE README)](https://github.com/adafruit/Adafruit_CircuitPython_CLUE)
at this point, just returning the measurements that it takes periodically.

# App Installation

### BEFORE INSTALLING THE APP

- should really verify that you can connect to the CLUE & stream output
- with the default app running, you can do this
  - although the output isn't particularly good
- see the "Connect & Stream Output to Verify App" section below for details

### Actual App Installation Instructions

- Followed Instructions Here: [CircuitPython on CLUE (Adafruit)](https://learn.adafruit.com/adafruit-clue/circuitpython)
- Install CircuitPython 7.3.3 on the CLUE device
  - [CircuitPython Downloads for CLUE (Adafruit)](https://circuitpython.org/board/clue_nrf52840_express/)
- Downloaded the library bundle for CircuitPython 7.x
  - [CircuitPython Libraries Page (CircuitPython)](https://circuitpython.org/libraries)
- Copied these libraries to the CLUE lib folder:
```
- adafruit_apds9960
- adafruit_bus_device
- adafruit_datetime.mpy
- adafruit_display_shapes
- adafruit_display_text
- adafruit_lsm6ds
- adafruit_register
- adafruit_bmp280.mpy
- adafruit_clue.mpy
- adafruit_lis3mdl.mpy
- adafruit_logging.mpy
- adafruit_sht31d.mpy
- adafruit_slideshow.mpy
- neopixel.mpy
```
  - **NOTE** (entries w/o `.mpy` extensions are folders)
- replace the `code.py` file w/the one from this directory
  - it should soft reboot & begin running

# Connect & Stream Output to Verify App

- **NOTE** you should really do this before 
- follow directions from [Advanced Serial Console on Linux](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-linux)
- short version:
  - find correct serial port
    - cmd: `ls -al /dev/ttyACM*`
    - if you don't see results, it's most likely that your USB cable isn't made to transfer data, just power
    - should be able to try new cables until you can see the data
  - connect w/ `screen`
    - cmd: `screen /dev/ttyACM0 115200`
  - if you immediately get the `[screen is terminating]` message:
    - have a perms problem
    - solve this by:
      - checking group of the TTY: `ls -al /dev/ttyACM0`
      - adding yourself to the group: `sudo adduser <your-username> <tty-group>`
      - I needed to restart the OS in order for fix to take effect
