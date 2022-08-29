from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

# create unique identifier for each device
motorA = robot.getDevice("A motor")

timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)

motorA_pos = 0


# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   
    print(key_pressed) 
    
    # here's is an example of keyboard movement for A motor
    if(key_pressed == 49):
        motorA_pos += 0.01
    if(key_pressed == 50):
        motorA_pos -= 0.01
        
   
    motorA.setPosition(motorA_pos)
