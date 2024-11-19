# machEgrrcon2023
# README for `rainbowRave.py`

## Overview
`rainbowRave.py` is a Python script that communicates with the CAN bus of a Ford Mach-E to change the colors of its interior lighting. It is designed to send a sequence of CAN messages that alter the light colors, creating a "rave" or cycling effect. The script utilizes the `python-can` library for CAN bus interaction.

## Requirements
- **Python 3.x**
- `python-can` library
- SocketCAN interface on a Linux system (e.g., Raspberry Pi, PC with CAN interface)
- A CAN transceiver connected to the vehicle's CAN bus

## Installation
1. Ensure Python is installed:
   ```bash
   sudo apt-get install python3
   ```

2. Install the `python-can` library:
   ```bash
   pip install python-can
   ```

3. Set up the CAN interface (e.g., SocketCAN):
   ```bash
   sudo ip link set can0 up type can bitrate 500000
   sudo ifconfig can0 up
   ```

## Script Structure
- **Imports**: The script imports the required modules: `time`, `can`, and sets up the `Bus` interface.
- **`send_message()` function**: Sends a single CAN message with a specified arbitration ID and data payload.
- **`send_one()` function**: Sends a series of predefined CAN messages that change the interior color.
- **`spam()` function**: Continuously sends CAN messages in a loop with a brief delay to create a continuous lighting effect.

## How to Use
1. Ensure that your CAN transceiver is properly connected to the vehicle and configured on `can0`.
2. Run the script:
   ```bash
   python rainbowRave.py
   ```

3. The script will execute the `spam()` function by default, continuously sending color-change messages to the CAN bus to cycle through colors.

## Functions Explained

### `send_message(arbitration_id, data)`
- **Purpose**: Sends a CAN message to the bus.
- **Parameters**:
  - `arbitration_id`: The CAN ID for the message.
  - `data`: An array of bytes representing the payload.
- **Returns**: None. Prints a confirmation if successful or an error message if not.

### `send_one()`
- **Purpose**: Sends a predefined set of messages with different data payloads that correspond to color changes.
- **Message Details**:
  - Arbitration ID: `0x3DA`
  - Data payloads: Different sets that adjust the color values.
- **Returns**: None. Calls `send_message()` iteratively for each data payload.

### `spam()`
- **Purpose**: Continuously calls `send_one()` to create a cycling color effect.
- **Behavior**: Runs indefinitely with a slight delay (`time.sleep(0.001)`) between iterations to avoid overwhelming the CAN bus.

## Important Notes
- **Safety First**: This script interacts with the vehicle's CAN bus. Improper use can lead to unexpected behavior. Ensure you are familiar with CAN bus communication and its implications.
- **Test Environment**: Always test on a simulated environment or bench setup before running on a live vehicle.
- **CAN Bus Integrity**: Avoid spamming messages too rapidly as it may interfere with other vehicle systems.

## Customization
To customize the color sequences or behavior:
- Modify the `messages` array in `send_one()` with different data payloads to experiment with different color outputs.
- Adjust the delay in the `spam()` function to modify the speed of the color cycling.

## License
This script is provided as-is for educational and experimental purposes. Use at your own risk. Ensure compliance with local laws and regulations regarding vehicle modifications.

## Disclaimer
Manipulating the CAN bus of a vehicle should be performed with caution. The author is not responsible for any damages, legal implications, or issues resulting from the use of this script.