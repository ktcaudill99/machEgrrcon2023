import time
import can
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'can0'
from can.interface import Bus
bus = Bus()

def send_message(arbitration_id, data):
    "Send a single CAN message"
    with can.interface.Bus() as bus:
        msg = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")

def send_one():
    messages = [
        (0x3DA, [0x01, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x02, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x03, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x04, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x05, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00]),
        (0x3DA, [0x06, 0x65, 0x00, 0xFF, 0xC3, 0xFE, 0x00, 0x00])
    ]

    for arbitration_id, data in messages:
        send_message(arbitration_id, data)
   #     time.sleep(.001)  # Hold for a few seconds

def spam():
        ":param id: Spam the bus with messages including the data id."

#       with can.interface.Bus() as bus:

        while True:

                send_one()

                time.sleep(.001)

 
if __name__ == "__main__":
     #   send_one()
       spam()
