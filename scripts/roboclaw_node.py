#!/usr/bin/env python

from my_roboclaw.roboclaw import Roboclaw
from time import sleep
import rospy

class RoboclawTest:
    def __init__(self):

        self.counts_per_rev = 1497.325

        self.address = 0x80
        self.roboclaw = Roboclaw("/dev/ttyS0", 38400)
        self.roboclaw.Open()

        # Reset encoders
        self.roboclaw.ResetEncoders(self.address)

    def test_motors_open_loop(self):
        self.roboclaw.ForwardM1(self.address,64)
        sleep(2)
        self.roboclaw.ForwardM1(self.address,0)
        sleep(2)

        self.roboclaw.BackwardM1(self.address,64)
        sleep(2)
        self.roboclaw.BackwardM1(self.address,0)
        sleep(2)
        
        self.roboclaw.ForwardM2(self.address, 64)
        sleep(2)
        self.roboclaw.ForwardM2(self.address,0)
        sleep(2)

        self.roboclaw.BackwardM2(self.address, 64)
        sleep(2)
        self.roboclaw.BackwardM2(self.address,0)
        sleep(2)

    def test_encoders(self):
        # Read encoder 1
        print "Encoder 1 initial count:"
        print self.roboclaw.ReadEncM1(self.address)
        sleep(2)
        # Set encoder and then read and print to test operation
        self.roboclaw.SetEncM1(self.address, 10000)
        print "Encoder 1 after setting count:"
        print self.roboclaw.ReadEncM1(self.address)
        sleep(2)
        # Reset encoders and read and print value to test operation
        self.roboclaw.ResetEncoders(self.address)
        print "Encoder 1 after resetting count:"
        print self.roboclaw.ReadEncM1(self.address)

        # Read encoder 2
        print "Encoder 2 initial count:"
        print self.roboclaw.ReadEncM1(self.address)
        sleep(2)
        # Set encoder and then read and print to test operation
        self.roboclaw.SetEncM2(self.address, 10000)
        print "Encoder 2 after setting count:"
        print self.roboclaw.ReadEncM2(self.address)
        sleep(2)
        # Reset encoders and read and print value to test operation
        self.roboclaw.ResetEncoders(self.address)
        print "Encoder 2 after resetting count:"
        print self.roboclaw.ReadEncM2(self.address)
        sleep(2)

    def test_velocity_control(self):
        # move one rotation, 1000 counts/sec * X revs/count
        speed_cps = 200
        revs = 1
        time_on = revs/(speed_cps / self.counts_per_rev)
        self.roboclaw.SpeedM1M2(self.address, speed_cps, 0)
        sleep(time_on)

        self.roboclaw.SpeedM1M2(self.address, 0, 0)
        sleep(1)

if __name__ == '__main__':
    # rospy.init_node('roboclaw_node', anonymous=True)
    test = RoboclawTest()
    # test.test_motors_open_loop()
    # test.test_encoders()
    test.test_velocity_control()