import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DirectionMapper_sub(Node):

    def __init__(self):
        super().__init__('direction_mapper_sub')
        self.subscription = self.create_subscription(String, 'directions', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        global to_send
        to_send = dict.get(msg.data)
        print(to_send)

class DirectionMapper_pub(Node):

    def __init__(self):
        super().__init__('direction_mapper_pub')
        self.publisher_ = self.create_publisher(String, 'motors', 10)
        timer_period = 0.5  # seconds     

        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        settings = saveTerminalSettings()
        key = getKey(settings)
        #print("letra presionada : "+ key)
        self.get_logger().info("letra presionada : "+ key)
        msg = String()
        # msg.data = 'Hello World: %d' % self.i
        msg.data= ("letra enviada : " + key)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: ' + msg.data)
            
        msg = String()
       # msg.data = 'Hello World: %d' % self.i
        msg.data= to_send
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

dict = {
    "FWD" : "1",
    "BKWD" : "2",
    "L" : "3",
    "R" : "4",
    "FWD_L" : "5",
    "FWD_R" : "6",
    "BKWD_L" : "7",
    "BKWD_R" : "8",
    "CW" : "9",
    "CCW" : "10",
    "STOP" : "11"
}

def main(args=None):
    
    rclpy.init(args=args)

    direction_mapper_sub = DirectionMapper_sub()
    direction_mapper_pub = DirectionMapper_pub()

    global to_send 
    to_send = ":w1-25;:w2-25;"
    
    rclpy.spin(direction_mapper_sub)
    rclpy.spin(direction_mapper_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    direction_mapper_sub.destroy_node()
    direction_mapper_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
