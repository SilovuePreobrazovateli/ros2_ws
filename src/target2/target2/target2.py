import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from serial import Serial

class Target2Node(Node):
    def __init__(self):
        super().__init__('target2')
        self.subscription = self.create_subscription(String, 'target1/gpio', self.listener_callback, 10)
        self.subscription
        self.sp = Serial('/dev/ttyACM1', baudrate=12000000)

    def listener_callback(self, msg):
        self.sp.write(str.encode(msg.data))
        self.get_logger().info(msg.data)

def main(args = None):
    rclpy.init(args=args)
    target2 = Target2Node()
    rclpy.spin(target2)

if __name__ == '__main__':
    main()