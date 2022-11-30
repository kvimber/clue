# clue

CLUE board management &amp; data collection

The repo is managed into a _monorepo_ style, so each folder holds an application
that runs in different places.

Note that there are sub-READMEs with notes specific to that app:

- [CLUE README](clue/README.md)
- [collector README](collector/README.md)

### Glossary

- clue: [Adafruit CLUE - nRF52840 Express w/Bluetooth LE](https://www.adafruit.com/product/4500)
  - can either mean the hardware device itself
  - or the software for it, in the clue folder at this level
- collector: software that listens for clue output & writes it to log files for later use

### TODO / Wishlist

- [ ] differentiate CLUE screen output
  - right now, just outputs the same lines
  - would be better to have a status
- [ ] collector status messages
  - collector just sits in silence while running
  - should have some sort of periodic output w/status
  - perhaps "X messages collected in last hour"??
- [ ] data analysis
  - perhaps a jupyter notebook or something
  - that can plot out data for a particular time period
  - using old data files seems fine to start
    - but eventually watching for new data eventually
- [ ] other forms of connectivity
  - CURRENTLY, only supports USB connection from CLUE to connector
  - but CLUEs support bluetooth, for instance
  - so perhaps I could setup a number of them running independently
    - w/a server that's collecting from multiple at a time
