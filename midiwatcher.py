#!/usr/bin/env python3
import mido
import sys

def main():
    # 1. Fetch available MIDI input ports from PipeWire/ALSA
    ports = mido.get_input_names()
    if not ports:
        print("No MIDI input ports found. Please connect a device or start a virtual port.")
        return

    print("Available MIDI input ports:")
    for i, port in enumerate(ports):
        print(f"  [{i}] {port}")

    # 2. Select port via command-line argument or interactive prompt
    port_idx = -1
    if len(sys.argv) > 1:
        try:
            port_idx = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid port number.")
            sys.exit(1)
    else:
        try:
            choice = input("\nEnter port number to monitor: ")
            port_idx = int(choice)
        except (KeyboardInterrupt, ValueError):
            print("\nExited.")
            sys.exit(1)

    if port_idx < 0 or port_idx >= len(ports):
        print("Invalid port selected.")
        sys.exit(1)

    port_name = ports[port_idx]
    
    # 3. Open the port and listen
    print(f"\nMonitoring: {port_name}")
    print("Press Ctrl+C to exit.\n")
    
    # Table Header
    print(f"{'RAW HEX':<15} | {'EVENT TYPE':<16} | {'DETAILS'}")
    print("-" * 70)

    try:
        with mido.open_input(port_name) as inport:
            for msg in inport:
                # Get raw byte array and convert to uppercase Hex strings
                raw_bytes = msg.bytes()
                hex_str = ' '.join([f"{b:02X}" for b in raw_bytes])
                
                # Format the bonus event details
                details = ""
                if msg.type in ('note_on', 'note_off'):
                    details = f"Ch: {msg.channel + 1:<2} | Note: {msg.note:<3} | Vel: {msg.velocity:<3}"
                elif msg.type == 'control_change':
                    details = f"Ch: {msg.channel + 1:<2} | CC: {msg.control:<5} | Val: {msg.value:<3}"
                elif msg.type == 'pitchwheel':
                    details = f"Ch: {msg.channel + 1:<2} | Pitch: {msg.pitch}"
                elif msg.type == 'program_change':
                    details = f"Ch: {msg.channel + 1:<2} | Program: {msg.program}"
                elif msg.type == 'sysex':
                    details = f"System Exclusive ({len(raw_bytes)} bytes)"
                elif msg.type == 'clock':
                    details = "Timing Clock"
                else:
                    # For unmapped types, display the raw attributes (stripping 'type')
                    d = msg.dict()
                    d.pop('type', None)
                    d.pop('time', None)
                    details = str(d)

                # Format the event type string for cleaner reading
                event_type = msg.type.replace('_', ' ').title()

                print(f"{hex_str:<15} | {event_type:<16} | {details}")

    except KeyboardInterrupt:
        print("\n\nExiting MIDI monitor...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == '__main__':
    main()
