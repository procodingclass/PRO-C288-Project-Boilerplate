from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

# create unique identifier for each device


timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)


# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   

    # write code to move the joints with keyboard
