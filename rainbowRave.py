import time
import can

# Configure the CAN interface to use 'socketcan' and the channel 'can0'
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'can0'

from can.interface import Bus

# Create a CAN bus instance
bus = Bus()

def send_message(arbitration_id, data):
     """
    Send a single CAN message.
    
    :param arbitration_id: The CAN ID of the message
    :param data: The data payload of the message as a list of bytes
    """
    # Initialize the bus interface to send the message
    with can.interface.Bus() as bus:
                # Create a CAN message with the given ID and data
        msg = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
        try:
             # Attempt to send the message on the CAN bus
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            # Handle the case where the message could not be sent
            print("Message NOT sent")

def send_one():
     """
    Send a predefined set of CAN messages that change the interior color of the car.
    """
    # List of CAN messages with different data payloads to create color variations
    messages = [
        (0x3DA, [0x01, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x02, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x03, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x04, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x05, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x06, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00])
    ]

        # Loop through each message and send it using the send_message function
    for arbitration_id, data in messages:
        send_message(arbitration_id, data)
        # Optional: Add a slight delay between each message if needed
        # time.sleep(0.001)

def spam():
     """
    Continuously send CAN messages to create a continuous color cycling effect.
    """
    # Infinite loop to repeatedly send messages from the send_one function
    while True:

        send_one()
        # Short delay to avoid overwhelming the CAN bus
        time.sleep(.001)

 # Run the spam function if the script is executed directly
if __name__ == "__main__":
     #   send_one()
       spam()
