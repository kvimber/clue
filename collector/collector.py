import serial
import json
from datetime import datetime as dt
from datetime import date

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
    while True:
        line_in = ser.readline()
        try:
            line_data = json.loads(line_in)
        except json.decoder.JSONDecodeError as e:
            if line_in == b'':
                continue
            print("JSON Decode Error: {}".format(e))
            print("")
            print("  at line: {}".format(line_in))
            continue

        # now = dt.now()
        now_str = dt.now().isoformat()
        # something is currently wrong with the CLUE timestamps
        # there is an adafruit_ntp module that seems like it could
        # fix this, but you have to provide the server implementation.
        # Instead, we'll fix this on the receive side for now
        line_data["timestamp"] = now_str
        line_str = json.dumps(line_data, sort_keys=True)
        line_str_final = "{},\n".format(line_str)

        date_str = date.today().isoformat()
        logfile_name = "clue_logs/{}.log".format(date_str)
        with open(logfile_name, 'a') as fo:
            fo.write(line_str_final)
