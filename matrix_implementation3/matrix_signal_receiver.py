import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
import smbus
import time

I2C_SLAVE_ADDR = 0x08 

class MatrixSignalReceiver(Node):
    def __init__(self):

        super().__init__('matrix_signal_receiver')
        self.subscription = self.create_subscription(
            Int8,
            '/matrix_signal',
            self.listener_callback,
            10)
        self.subscription

        self.bus = smbus.SMBus(1)

        self.matrix_signal_to_color_dict = {
            0: "matrix_off",
            1: "blue",
            2: "red",
            3: "green",
            4: "quantum"
        }
        self.matrix_color = self.matrix_signal_to_color_dict[1]

    def send_data(self, data):
        self.bus.write_byte(I2C_SLAVE_ADDR, int(data))
        print("Data sent")

    def listener_callback(self, msg):

        self.matrix_color = self.matrix_signal_to_color_dict[msg.data]

        if self.matrix_color == "matrix_off":
            self.send_data("0")
        elif self.matrix_color == "blue":
            self.send_data("1")
        elif self.matrix_color == "red":
            self.send_data("2")
        elif self.matrix_color == "green":
            self.send_data("3")
        elif self.matrix_color == "quantum":
            self.send_data("4")

def main(args=None):
    rclpy.init(args=args)
    matrix_signal_receiver = MatrixSignalReceiver()
    rclpy.spin(matrix_signal_receiver)
    matrix_signal_receiver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

