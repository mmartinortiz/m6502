# A Python 6502 Emulator

An m6502 emulator written in Python. Started thanks to [Hans Spaans](https://dailystuff.nl/projects/writing-a-6502-emulator-in-python)

## Writing and Reading words

The memory of the `m6502` uses the [little endian architecture](https://en.wikipedia.org/wiki/Endianness). This means that the least-significant byte (remember, 2 bytes == 1 word) at the smallest address.
