# midiwatcher

midiwatcher prints midi traffic out in real time.

## Requires:

Python3 (no specific version really), python3-mido, and python3-rtmidi

For example:
```
sudo apt install python3-mido python3-rtmidi
```

## Install:
```
git clone https://github.com/eliggett/midiwatcher
cd midiwatcher
chmod +x midiwatcher.py
```

## Run: 
```
./midiwatch.py 
Available MIDI input ports:
  [0] Midi Through:Midi Through Port-0 14:0
  [1] 4ACBCC15:4ACBCC15 MIDI 1 28:0
  [2] Midi Through:Midi Through Port-0 14:0
  [3] 4ACBCC15:4ACBCC15 MIDI 1 28:0

Enter port number to monitor: 1

Monitoring: 4ACBCC15:4ACBCC15 MIDI 1 28:0
Press Ctrl+C to exit.

RAW HEX         | EVENT TYPE       | DETAILS
----------------------------------------------------------------------
B3 0E 42        | Control Change   | Ch: 4  | CC: 14    | Val: 66 
B3 0E 43        | Control Change   | Ch: 4  | CC: 14    | Val: 67 
B3 0E 44        | Control Change   | Ch: 4  | CC: 14    | Val: 68 
B3 0E 45        | Control Change   | Ch: 4  | CC: 14    | Val: 69 
B3 0E 46        | Control Change   | Ch: 4  | CC: 14    | Val: 70 
B3 0E 47        | Control Change   | Ch: 4  | CC: 14    | Val: 71 
B3 0E 48        | Control Change   | Ch: 4  | CC: 14    | Val: 72 
B3 0E 49        | Control Change   | Ch: 4  | CC: 14    | Val: 73 

```
