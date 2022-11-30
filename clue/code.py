print("Hello World 9")

import board
import digitalio
import time
import json
import adafruit_logging as al
from adafruit_clue import clue
from adafruit_datetime import datetime as dt

# led = digitalio.DigitalInOut(board.LED)
# led.direction = digitalio.Direction.OUTPUT

logger = al.Logger("CLUE")
stream_handler = al.StreamHandler()
logger.addHandler(stream_handler)

while True:
    time.sleep(10.0)
    # led.value = True
    # time.sleep(0.5)
    # led.value = False
    # time.sleep(0.5)
    # logger.warning("wat")
    acceleration_str = "{:.2f} {:.2f} {:.2f} m/s^2".format( *clue.acceleration)
    gyro_str =         "{:.2f} {:.2f} {:.2f} dps".format(   *clue.gyro)
    magnetic_str =     "{:.3f} {:.3f} {:.3f} uTesla".format(*clue.magnetic)
    color_str =        "R: {} G: {}, B: {}".format(         *clue.color)
    data = {
        "timestamp":    dt.now().isoformat(),
        "acceleration": acceleration_str,
        "gyro":         gyro_str,
        "magnetic":     magnetic_str,
        "pressure":     "{:.3f} hPa".format(clue.pressure),
        "altitude":     "{:.1f} m".format(clue.altitude),
        "temperature":  "{:.1f} C".format(clue.temperature),
        "humidity":     "{:.1f} %".format(clue.humidity),
        "proximity":    clue.proximity,
        "gesture":      clue.gesture,
        "color":        color_str,
        "buttons": {
            "a": clue.button_a,
            "b": clue.button_b
        },
        "touches": {
            0: clue.touch_0,
            1: clue.touch_1,
            2: clue.touch_2
        }
    }
    data_str = json.dumps(data)
    print(data_str)
