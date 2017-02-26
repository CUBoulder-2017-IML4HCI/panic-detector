import serial
import OSC


# monitor_serial() monitors the specified serial port for a line of
# data and returns it. Be sure the serial device uses newlines.
def monitor_serial(serial_path, rate=115200):
    s = serial.Serial(port=serial_path, baudrate=rate)
    test_readline = s.readline()
    return test_readline


# initialize_osc() returns a OSC client object
def initialize_osc(dest_ip, dest_port):
    destination = dest_ip, dest_port
    dest = OSC.OSCClient()
    dest.connect(destination)
    return dest


def main():

    # Set parameters
    serial_path = '/dev/cu.usbmodemFD132'  # path to serial device
    serial_rate = '115200'  # serial baud rate
    dest_ip = '127.0.0.1'  # wekinator ip
    dest_port = 6448  # wekinator port
    dest_addr = '/wek/inputs'


    wekinator = initialize_osc(dest_ip, dest_port)
    while True:
        incoming_data = monitor_serial(serial_path, serial_rate)
        osc_msg = OSC.OSCMessage()
        osc_msg.setAddress(dest_addr)
        data_temp, data_pitch, data_roll = incoming_data.split(',')
        osc_msg.append(float(data_temp))
        osc_msg.append(float(data_pitch))
        osc_msg.append(float(data_roll))
        wekinator.send(osc_msg)



if __name__ == '__main__':
   main()
