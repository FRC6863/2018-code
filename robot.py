#!/usr/bin/env python3
'''
    The SampleRobot class is the base of a robot application that will
    automatically call your Autonomous and OperatorControl methods at
    the right time as controlled by the switches on the driver station
    or the field controls.
    
    WARNING: While it may look like a good choice to use for your code
    if you're inexperienced, don't. Unless you know what you are doing,
    complex code will be much more difficult under this system. Use
    IterativeRobot or Command-Based instead if you're new.
'''


import wpilib
import ctre
from wpilib.drive import DifferentialDrive
from _functools import partial
from toggle import Toggle
from toggle import Toggle2
import random
import time

class MyRobot (wpilib.IterativeRobot):

    def robotInit(self):
        self.leftFront = ctre.WPI_TalonSRX(2)
        self.rightFront = ctre.WPI_TalonSRX(4)
        self.leftBack = ctre.WPI_TalonSRX(1)
        self.rightBack = ctre.WPI_TalonSRX(3)
        self.left=wpilib.Spark(0)
        self.right=wpilib.Spark(1)
        self.left2=wpilib.Spark(2)
        self.right2=wpilib.Spark(3)
        self.leftJoystick = wpilib.Joystick(0)
        self.solenoid1=wpilib.DoubleSolenoid(3,4)
        self.solenoid2=wpilib.DoubleSolenoid(2,5)
        self.solenoid3=wpilib.DoubleSolenoid(1,6)
        self.sToggle=Toggle2(self.leftJoystick,1)
        self.compressor=wpilib.Compressor(0)
        self.shoot1=wpilib.Spark(4)
        self.shoot2=wpilib.Spark(5)
        self.shoot3=wpilib.Spark(6)
        self.shoot4=wpilib.Spark(7)
        self.compressor.clearAllPCMStickyFaults()   
        self.compressor.setClosedLoopControl(False)
        self.solenoid3On=True
    
    def autonomousInit(self):
        self.t_i=time.time()
    
    def autonomousPeriodic(self):
        if time.time()-self.t_i<2.5:
            self.rightFront.set(-1*1)
            self.leftBack.set(1)
            self.rightBack.set(-1*1)
            self.leftFront.set(1)
        else:
            self.rightFront.set(0)
            self.leftBack.set(0)
            self.rightBack.set(0)
            self.leftFront.set(0)

    def teleopPeriodic(self):
        leftSpeed = -1*self.leftJoystick.getRawAxis(1)
        rightSpeed = self.leftJoystick.getRawAxis(5)
        lt = self.leftJoystick.getRawAxis(2)
        rt = self.leftJoystick.getRawAxis(3)

        

        if (lt>0):
            self.left.set(-1*lt)
            self.right.set(lt)
            self.left2.set(-1*lt)
            self.right2.set(lt)
        

        else:
            self.left.set(rt)
            self.right.set(-1*rt)
            self.left2.set(rt)
            self.right2.set(-1*rt)

        self.leftFront.set(leftSpeed)
        self.leftBack.set(leftSpeed)
        self.rightFront.set(rightSpeed)
        self.rightBack.set(rightSpeed)
        
    
        #     if self.sToggle.on:
        #         print("a is on")
        #     else:
        #         print("a is off")
        #     if self.bToggle.on:
        #         print("b is on")
        #     else:
        #         print("b is off")
        # 
        if self.leftJoystick.getRawButton(4):
        
            # print("on")
            self.solenoid1.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
            self.solenoid1.set(wpilib.DoubleSolenoid.Value.kForward)
        # 
        if self.leftJoystick.getRawButton(1):
            if not self.solenoidOn:
                self.solenoid3On=not self.solenoid3On
                self.solenoid3.set(wpilib.DoubleSolenoid.Value.kForward)
            else self.solenoidOn:
                self.solenoid3On=not self.solenoid3On
                self.solenoid3.set(wpilib.DoubleSolenoid.Value.kReverse)
        # 
        # if not self.leftJoystick.getRawButton(2):
        #     # print("on")
        #     self.compressor.stop()
        # else:
        
        if not self.sToggle.on:
            # print("on")
            self.solenoid2.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.solenoid2.set(wpilib.DoubleSolenoid.Value.kReverse)
            self.solenoid3.set(wpilib.DoubleSolenoid.Value.kReverse)
        
        # 
        # 
        self.compressor.start()
        if random.randint(1,10)==3:
            print(self.compressor.enabled())
            
        if self.leftJoystick.getRawButton(3):
            self.shoot1.set(1.0)
            self.shoot2.set(1.0)
            self.shoot3.set(1.0)
            self.shoot4.set(1.0)
        else:
            self.shoot1.set(0.0)
            self.shoot2.set(0.0)
            self.shoot3.set(0.0)
            self.shoot4.set(0.0)

        

if __name__ == '__main__':
    wpilib.run(MyRobot)
    
