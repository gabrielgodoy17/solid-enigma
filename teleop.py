from std_msgs.msg import String
from rclpy.node import Node
from pynput import keyboard
import rclpy

class KeyboardRead(Node):

    def __init__(self):
        super().__init__('keyboard_read')
        self.publisher_ = self.create_publisher(String, 'directions', 10)
        # timer_period = 0.5  # seconds

        # self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = to_send
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def on_activate_FWD(pub):
    print(pub)
    global to_send
    to_send = "FWD"
    msg = String()
    msg.data = to_send
    pub.publisher_.publish(msg)
    pub.get_logger().info('Publishing: "%s"' % msg.data)
    pub.i += 1

def on_activate_BKWD():
    global to_send
    to_send = "BKWD" 

def on_activate_L():
    global to_send
    to_send = "L"

def on_activate_R():
    global to_send
    to_send = "R"   

def on_activate_FWD_L():
    global to_send
    to_send = "FWD_L"

def on_activate_FWD_R():
    global to_send
    to_send = "FWD_R"

def on_activate_BKWD_L():
    global to_send
    to_send = "BKWD_L"

def on_activate_BKWD_R():
    global to_send
    to_send = "BKWD_R"

def on_activate_CW():
    global to_send
    to_send = "CW"

def on_activate_CCW():
    global to_send
    to_send = "CCW"

def on_activate_STOP():
    global to_send
    to_send = "STOP"

def main(args=None):

    rclpy.init(args=args)

    keyboard_read = KeyboardRead()
    global to_send
    to_send = "STOP"

    #rclpy.spin(keyboard_read)

    with keyboard.GlobalHotKeys({
    '8' : on_activate_FWD,
    '2' : on_activate_BKWD,
    '4' : on_activate_L,
    '6' : on_activate_R,
    '7' : on_activate_FWD_L,
    '9' : on_activate_FWD_R,
    '1' : on_activate_BKWD_L,
    '3' : on_activate_BKWD_R,
    'x' : on_activate_CW,
    'z' : on_activate_CCW,
    '<space>' : on_activate_STOP,
    }) as h: h.join()



    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    keyboard_read.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
