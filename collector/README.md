# Collector

Collector is an app that listens on the CLUE's serial connection,
reporting all data results to log files for later use.

# Running the App

```bash
$ python collector.py
```

# App Installation

- has a `.python-version` file, so use `pyenv` to set that
- then create a virtualenv for the project
  - cmd: `pyenv virtualenv clue-collector`
  - cmd: `pyenv activate clue-collector`
- install dependencies
  - cmd: `pip install -r requirements.txt`
- should be ready to run
  - see "Running the App" above

# Known Issues

### CLUE doesn't understand dates

- currently, CLUE's clock isn't set correctly
- seems like fixing it would be non-trivial
  - [Adafruit NTP Library Doc](https://docs.circuitpython.org/projects/ntp/en/latest/)
  - seems to say that we'd have to implement a server to respond as well
- workaround: collector overwrites the timestamp
  - as it receives the data
  - before writing the entry to the log
  - seems fast enough for now :shrug:

# Docs / Resources / Etc

- [pySerial (Github Repo)](https://github.com/pyserial/pyserial)
  - [module docs (ReadTheDocs)](https://pyserial.readthedocs.io/en/latest/shortintro.html)

# TODO / Wants / Wishes

- [ ] detect CLUE restarts
  - currently, see output like this from collector:
  ```
  at line: b'\r\n'
JSON Decode Error: Expecting value: line 1 column 1 (char 0)

  at line: b'Code stopped by auto-reload. Reloading soon.\r\n'
JSON Decode Error: Expecting value: line 1 column 1 (char 0)

  at line: b'soft reboot\r\n'
JSON Decode Error: Expecting value: line 2 column 1 (char 2)

  at line: b'\r\n'
JSON Decode Error: Expecting value: line 1 column 1 (char 0)

  at line: b'Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.\r\n'
JSON Decode Error: Expecting value: line 1 column 1 (char 0)

  at line: b'code.py output:\r\n'
JSON Decode Error: Expecting value: line 1 column 1 (char 0)

  at line: b'Hello World 9\r\n'
JSON Decode Error: Expecting value: line 2 column 1 (char 2)
  ```
  - being able to detect this & report it much nicer wourl be great
