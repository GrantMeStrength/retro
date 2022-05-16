# Robot Project: Omnibot 25

![](../images/robot1.jpg)

## Goals

1. A moving robot that can autonomously navigate the corridors at work to go from one office to another, which is not in line of sight.
Sensors can avoid collisions, and a camera and machine learning model can detect corners / doors / singage, and work with an internal map to find the destination. Humans along the way will be greated.

2. A simple telepresence device, allowing remote colleagues to explore the office via a web interface.


## Robot body & motors

Buggy designs are great and everything, and yes, they are practical. But are they cool? Will they look good navigating a corridor in work? No. They will not. Also, they're often small and the motors are not great on carpet. So why not build on the hard work of pioneering robot designs - like Japanese toy maker Tomy? In the 1980's Tomy made several robots toys (under the brand [Omnibot](http://www.theoldrobots.com/omnibot.html)) which not only have a fanatical following among middle-aged nerds to this day, starred in the TV show [How I met your mother](https://how-i-met-your-mother.fandom.com/wiki/The_Robot), but also appear on eBay in various states of decay. If you get lucky you can pick up a nice example (usually missing the remote control) and either play with it or replace the "brain" with a Raspberry Pi. 

(Believe it or not, you can also purchase new wheel tred and hand gripper rubber to replace the originals, which often fall apart or turn into gloop. See [Daboo Designs](https://daboodesigns.com/collections/all/tomy-omnibot)).

I am using an Omnibot 5402 model, given a serious overhaul.

## Sensors


### Raspberry Pi camera

The standard Pi camera is mounted on the front of the robot.

### LIDAR module

[This LiDAR range finder](https://www.amazon.com/dp/B088NVX2L7?psc=1&ref=ppx_yo2ov_dt_b_product_details) works great - much easier to interface with the Raspberry Pi compared to the sonar devices. The disadvantage is that it's harder to use more than one device, so the robot will have to rotate a bit to look around it.

### IMU 

No IMU yet. Waiting to see if one will help.

## Accuators / Output


### Motors

The Omnibot has two 6v DC motors. Nothing fancy, but they're good motors and can go forward, backwards or rotate. To drive them from a Raspberry Pi you will need a small board that accepts 3.3v logic and an external power source for the motors, and connects to them directly. Such as the **L298N Dual H Bridge DC Stepper Motor Driver Controller Board** which is cheap and readily available. 

### LEDs

The Omnibot has a pair of LEDs which are controlled by the robot's original circuit board. As these are 1980's LEDs, the 3.3v from a Raspberry Pi output pin can't drive them, so I swapped them for 2000's LEDs which are nice and bright. 

### Sound

The Pi's headphone jack can be amplified or connected to a speaker/amp combo to replay sounds - it just takes a line of Python like this to replay a sound sample.

However, it's a little more fun to use a speech synthesiser. I was going to use one of my classic old 1980's speech chips, but then I found that - of course - it's all possible in software now. A program for the Pi called [Festival](https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/installing-the-festival-speech-package) does it all, and even sounds like a 1980's chip. I'm sure there are better quality Text To Speech systems, but this is exactly what I was looking for.

**Install Festival**

```
sudo apt-get install -y libasound2-plugins festival

```

**Use Festival in Python**

```
import os
os.system('echo "Destroy all humans!" | festival --tts')
```


### Display

A SparkFun SerLCD board provides 2 lines of 16 characters of text: just to have some visual clue of what is happening on the front of the robot. The board was originally designed for use with Arduino but works well perfect for the Pi - if you can find the drivers.
Someone kindly made some: [CircuitPython library for the Sparkfun SerLCD displays](https://github.com/fourstix/Sparkfun_CircuitPython_SerLCD). I did find that about 1 time in 50 the driver crashes, so wrap all the Python that displays text in a try/except clause.


### Imports

A list of additional files required.

```
sudo apt-get install -y libasound2-plugins festival
sudo pip3 install adafruit-blinka
pip3 install RPI.GPIO
pip3 install sparkfun-circuitpython-serlcd
```

### Plans

I laser-cut replacement front panels for the Omnibot, and a base for the Raspberry Pi and motor driver to go on. Plans included in the repo.