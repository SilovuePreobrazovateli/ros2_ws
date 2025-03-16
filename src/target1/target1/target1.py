import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
from serial import Serial
import threading

lock = threading.Lock()

def read_serial(node):
    sp = Serial('/dev/ttyACM0', baudrate=12000000)
    sp.timeout = 0
    while True:
        buf = sp.read(size=1024)
        with lock:
            if len(buf) > 0:
                msg = String()
                msg.data = chr(buf[0])
                node.publisher.publish(msg)
                node.get_logger().info(msg.data)

class Target1Node(Node):
    def __init__(self):
        super().__init__('target1')
        self.publisher = self.create_publisher(String, 'target1/gpio', 10)
        # self.timer = self.create_timer(1.0, self.timer_callback)
        # self.ch = 'H'
        
    def timer_callback(self):
        msg = String()
        msg.data = self.ch
        self.publisher.publish(msg)
        if self.ch == 'H':
            self.ch = 'L'
        else:
            self.ch = 'H'

def main(args=None):
    rclpy.init(args=args)
    target1 = Target1Node()
    t = threading.Thread(target=read_serial, args=(target1,))
    t.daemon = True
    t.start()
    rclpy.spin(target1)

if __name__ == '__main__':
    main()
