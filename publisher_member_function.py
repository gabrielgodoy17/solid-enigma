# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import rclpy
import keyboard
from rclpy.node import Node

from std_msgs.msg import String

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty

def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)

def getKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class MinimalPublisher(Node):
    
    
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
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

def callback1():
    print ("callback1")
    global to_send
    to_send=":w1-25;:w2-25;"

def callback2():
    print ("callback2")
    global to_send
    to_send=":w1+25;:w2+25;"


def callback3():
    print ("callback3")
    global to_send
    to_send=":w1+00;:w2+00;"

keyboard.add_hotkey('a',callback1)
#keyboard.add_hotkey('b',callback2)
#keyboard.add_hotkey('c',callback3)

def getKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main(args=None):
    
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    global to_send 
    to_send = ":w1-25;:w2-25;"
    

        
   
    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
