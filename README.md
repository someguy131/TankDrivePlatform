# TankDrivePlatform
Mid sized general purpose robot platform and its attachments.

<img width="927" alt="TDP picture" src="https://github.com/user-attachments/assets/fc21cb75-32fa-48a9-9e93-b51e18124da0" />

# Goals
The overall goal for this project is to create a large, capable tank drive chassis to be used as a general work-horse robot, keeping modularity in mind.
The requirements to reach this goal are outlined as follows:

  -Have enough torque to move itself and whatever loads may be put on it:
  
    -Trailers
    -Attachments
    -Buckets
    -Standardized Bolt Mounting Pattern

  -Be able to traverse basic off road terrain

    -Offroad tires
    -Ground clearance

  -Be durable and weather resistant

    -Skid Plate
    -Enclosed Gearboxes
    -Weather resistant electronics

  -Expandable electrical system

    -Power distribution board with extra slots
    -Raspberry Pi head computer controlling an Arduino MEGA 2560 for subsystem controls

# Design



# Electrical

To meet the requirement of being weather resistant, all fragile and important electronics are housed within a harbor freight ammo box. These boxes are easy to modify, easy to access the internals, and have a built in gasket on the lid. Holes were drilled for wire routing, cooling fans, and RSL.

![Electrical Box Diagram](https://github.com/user-attachments/assets/73345639-4510-4ce1-9794-49588136e640)

With the Raspberry Pi 3B acting as the head computer for the robot, all actuators and sensors are controlled via serial to a microcontroller (in this case an Arduino Mega 2560). This setup was chosen to provide easier future expandability, and plenty of options for software. The Pi has reasonable computation power, though not a ton is needed. More importantly, the Pi provides many options for communication. USB allows easy serial communication to peripheral devices, while having an ethernet port makes it easy to program, and also gives the future option of fully remote control using a router. 

Two 40x20mm fans are used in push-pull configuration to cool the electronics box. The RPi and ESCs already get fairly hot while running normally, and on a hot summer day, thermal issues are likely to occur. 

-add cfd stuff in here

# Software

