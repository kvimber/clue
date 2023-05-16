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
        now = dt.now()
        # something is currently wrong with the CLUE timestamps
        # there is an adafruit_ntp module that seems like it could
        # fix this, but you have to provide the server implementation.
        # Instead, we'll fix this on the receive side for now
        line_data["timestamp"] = now.isoformat()
        line_str = json.dumps(line_data, sort_keys=True)
        line_str_final = "{},\n".format(line_str)

        now_str = now.isoformat(sep=' ', timespec='seconds')
        temp_c_str = line_data['temperature']
        temp_c = float(temp_c_str.split(" ")[0])
        temp_f = (temp_c * (9/5)) + 32
        log_line = f"{now_str} temp {temp_c_str}/{temp_f} F"
        print(log_line)

        date_str = date.today().isoformat()
        logfile_name = "clue_logs/{}.log".format(date_str)
        with open(logfile_name, 'a') as fo:
            fo.write(line_str_final)
