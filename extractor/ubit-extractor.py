import serial
import OSC
import math


# monitor_serial() monitors the specified serial port for a line of
# data and returns it. Be sure the serial device uses newlines.
def monitor_serial(serial_path, rate=115200):
    s = serial.Serial(port=serial_path, baudrate=rate, timeout=None)
    return s


# initialize_osc() returns a OSC client object
def initialize_osc(dest_ip, dest_port):
    destination = dest_ip, dest_port
    dest = OSC.OSCClient()
    dest.connect(destination)
    return dest

# # initialize_osc_listener() returns a OSC server object
# def initialize_osc_listener(recv_ip, recv_port):
#     receive_address = recv_ip, recv_port
#     server = OSC.OSCServer(receive_address)



def main():

    # Set parameters
    serial_path = '/dev/cu.usbmodemFD132'  # path to serial device
    serial_rate = '115200'  # serial baud rate
    dest_ip = '127.0.0.1'  # wekinator ip
    dest_port = 6448  # wekinator port
    dest_addr = '/wek/inputs'
    keys = ['pulse', 'acc_roll', 'temp', 'pos_x', 'poz_y', 'pos_z']

    # pulses_buffer =[]
    # number_abv_th = 0
    # threshold = 0

    wekinator = initialize_osc(dest_ip, dest_port)
    serial_thing = monitor_serial(serial_path, serial_rate)
    while True:

        incoming_data = serial_thing.readline()
        osc_msg = OSC.OSCMessage()
        osc_msg.setAddress(dest_addr)
        values = []
        values += [0.0 + (int(value) if (value != '' and value != '-') else 0) for value in incoming_data.rstrip().split(",")]
        if len(values) < 6:
            #print incoming_data
            values += [0]
        #
        # print threshold
        # if len(pulses_buffer) < 60:
        #     pulses_buffer += [values[0]]
        #     values += [0]
        # else:
        #     threshold = max(pulses_buffer) * 0.9
        #     pulses_buffer.pop(0)
        #     pulses_buffer += [values[0]]
        #     number_abv_th = len([a for a in pulses_buffer if a > threshold])
        #     values += [number_abv_th]

        for ii in range(len(values)):
            print values
            #print "Feature" + str(ii) + ": " + str(values[ii])
            osc_msg.append(float(values[ii]))
        wekinator.send(osc_msg)

        #wekinator.send(osc_msg)
            # for ii in range(len(values)):
            #   print "Feature" + str(ii) + ": " + value
            #time.sleep(0.5)



if __name__ == '__main__':
   main()
