
# Oasis
# what it is?
A drone that can fly and also drive
# How to use it?
  Oasis is a remote controlled quad-copter drone with land driving capabilities. It can navigate a vast variety of terrain to escape the end of the world and make it to... The Oasis. Having two alternate modes travel provide a versitility that is not achieved by anything else. In strong winds it can drop down to travel on the ground. And in situations where driving is just not possible, Oasis can fly up and overcome obstacles. It is powered by a 4S 14.8V Li-Po battery and controlled by a Raspberry Pi Zero 2W and SpeedyBee F405 V5 FC/ESC stack to manage four 2207 1968KV drone motors, two MG90S servos for steering and one driving motors. It has a front-mounted non-adjustable camera, and TOF sensors to prevent collisions both in-air, and on the ground.
  It is controlled through a codded mobile app and has cameras mounted on the front underneath the propellers to allow for controll over a distance 
# WHY it exists?
  The world is ending in 7 days, to make sure that everyone can keep building we created a vehical that could get to our hardware oasis.This means travling all sorts of terrian and a single type vehical could just not cut it therefore Oasis came to life.To get YOU to hide in a hardware oasis with all of us. 


# Zine
<img width="1414" height="2000" alt="Oasis" src="https://github.com/user-attachments/assets/303b708e-5bd1-4e52-b64c-ed02fd3ea6dd" />



# BOM
| Product Name        | Application + discription                                                                                                                                                                                   | Product unit price  [¥] | Product amount | shipping cost  |       |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------|----------------|-------|
| car motor           | brushed motor, 300 RPM , used to power the back wheels of the car, geared dows 3:1 to travel about 7 kmm hour                                                                                               |                      20 |              2 |              0 |    42 |
| Axle/ shaft         | 3mm shaft that sits in beween plates and bearings that transfer power between the wheels                                                                                                                    |                    8.05 |              1 |              0 | 10.05 |
| bearings            | beaings for the shaft this one has a inner diameter of 3mm for the 3mm shaft we bought                                                                                                                      |                     2.3 |              6 |             10 |  15.8 |
| gears               | Double helix gears to transfer power from the motors to the shaft and wheels                                                                                                                                |                       0 |              0 |              0 |     2 |
| Power switch        | Turns the power on and off to make sure not wasting any electricity and also act as a saftey                                                                                                                |                     5.6 |              4 |              2 |  24.4 |
| Flight controllers  | Controllers the drone and calculates the disired speed for each of the four motors                                                                                                                          |                     380 |              1 |              0 |   382 |
| propellers          | To provide thrust and lift for the drone is mounted to the drone motors                                                                                                                                     |                       5 |              4 |              0 |    22 |
| servo 9g*2          | a compact 180° rotation micro servo motor ideal for robotics, RC models, and DIY automation projects. Two are used to steer the wheels to make turns and aviod appications.                                 |                      10 |              2 |              0 |    22 |
| raspi 02W           | an upgraded RP3A0 system-in-package (SiP) incorporates a quad-core 64-bit Arm Cortex-A53 CPU, clocked at 1GHz The SiP integrates a Broadcom BCM2710A1 die with 512MB of LPDDR2 SDRAM. Computer of the drone |                     360 |              1 |              0 |   362 |
| Wheels              | Rubber RC wheels that are going to be the wheels for the Car subsystem of our project                                                                                                                       |                       5 |              4 |              0 |    22 |
| Camera              | rasoberry Pi camera Rev 1.3 compatible with rassberry pie via HBV raspberry 150fpc, facing forward below the propellers                                                                                     |                      25 |              1 |              0 |    27 |
| Lipo battery        | High Discarge Lipo battery 4S1P 14.8V 20.72 POWERS EVERYTHING                                                                                                                                               |                     200 |              1 |                |   202 |
| Flight sensor ToF   | illuminating the scene with a modulated light source, and observing the reflected light and mounted under the drone motors                                                                                  |                       0 |              4 |              0 |     2 |
| Wires               | wires                                                                                                                                                                                                       |                       0 |             20 |              0 |     2 |
| Frame               | 3D printed frame                                                                                                                                                                                            |                       0 |              0 |              0 |     2 |
| step down converter | converts higher input voltages (typically 2S to 8S LiPo, or 5.5V to 35V) into a stable 5.25V output                                                                                                         |                      20 |              1 |              0 |    22 |
| Drone moters        | motor 2207.8  1968KV gives us thrust and lets us fly                                                                                                                                                        |                      80 |              4 |              0 |   322 |
| Battery charger     | charges the lipo battery                                                                                                                                                                                    |                     260 |              1 |              0 |   262 |
|                     |                                                                                                                                                                                                             |                         |                |                |       |
| Total sum           |                                                                                                                                                                                                     1745.25 |                         |                |                |       |


# wiring 
<img width="1260" height="840" alt="circuit" src="https://github.com/user-attachments/assets/a1c2f578-64f5-498d-925f-8081793e35b8" />





|     Pin     |                                     Connects to                                    |   |   |   |   |
|:-----------:|:----------------------------------------------------------------------------------:|---|---|---|---|
| 5V          | DC-DC Converter VOUT+ (5V logic rail)                                              |   |   |   |   |
| GND         | Common ground                                                                      |   |   |   |   |
| TX (GPIO14) | Flight Controller RX                                                               |   |   |   |   |
| RX (GPIO15) | Flight Controller TX                                                               |   |   |   |   |
| CSI         | Camera CSI                                                                         |   |   |   |   |
| SDA (GPIO2) | Shared I2C bus → Flight Controller SDA + all 4 ToF sensors' SCL... wait, SDA lines |   |   |   |   |
| SCL (GPIO3) | Shared I2C bus → Flight Controller SCL + all 4 ToF sensors' SCL line               |   |   |   |   |
|     GPIO    |                                     Connects to                                    |   |   |   |   |
| GPIO17      | Motor Driver — BIN2                                                                |   |   |   |   |
| GPIO18      | Motor Driver — PWMA                                                                |   |   |   |   |
| GPIO22      | Motor Driver — AIN1                                                                |   |   |   |   |
| GPIO23      | Motor Driver — AIN2                                                                |   |   |   |   |
| GPIO24      | Motor Driver — BIN1                                                                |   |   |   |   |
| GPIO13      | Motor Driver — PWMB                                                                |   |   |   |   |
| GPIO4       | ToF Sensor 1 — XSHUT                                                               |   |   |   |   |
| GPIO5       | ToF Sensor 2 — XSHUT                                                               |   |   |   |   |
| GPIO6       | ToF Sensor 3 — XSHUT                                                               |   |   |   |   |
| GPIO16      | ToF Sensor 4 — XSHUT                                                               |   |   |   |   |
| GPIO26      | ESC — TLM                                                                          |   |   |   |   |
| GPIO27      | ESC — CUR                                                                          |   |   |   |   |



# CAD
Top side-
<img width="682" height="411" alt="image" src="https://github.com/user-attachments/assets/b614422a-536b-4694-9eea-909fa3bc9c29" />
Top- 
<img width="710" height="575" alt="image" src="https://github.com/user-attachments/assets/20723ade-6e23-4b08-ac8b-2262cbc95340" />
Right- 
<img width="941" height="461" alt="image" src="https://github.com/user-attachments/assets/d6d68e25-34e5-43b7-a994-0f4d333b1556" />a
Bottem - 
<img width="668" height="587" alt="image" src="https://github.com/user-attachments/assets/4e1e0b29-173e-492a-a112-2889fbd552f7" />



