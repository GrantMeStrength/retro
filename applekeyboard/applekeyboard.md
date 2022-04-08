# Connecting an Apple II keyboard to other systems


The Apple IIe keyboard is a passive matrix of switches. This means it should be relatively easy to connect to some other systems, by means of a microcontroller.
For example, it could be used in a real Apple II but connected to, say, a Raspberry Pi running an emulator - thus replacing broken, missing or just tired Apple original electronics.
It would also be an option for connecting to other random systems, such as [Zog](https://github.com/GrantMeStrength/retro/blob/gh-pages/zog/zog.md).

That's what this section is about.



## Circuit Diagram

* [Apple IIe keyboard schematic](https://www.applefritter.com/node/7257)
* [Apple IIe schematic - Look for J17](https://www.apple.asimov.net/documentation/hardware/schematics/Schematic%20Diagram%20of%20the%20Apple%20IIe.pdf)
* [Keyboard pinout](https://gist.github.com/papodaca/5d854b296a5f7943e245)


## Microcontroller choice

It appears that while Arduinos are my usual go-to, a Teensy is better as it can appear as a USB keyboard very easily.


## Software

* [Keyduino](https://github.com/afiler/keyduino)
* [Arduino USB HID Keyboard](https://mitchtech.net/arduino-usb-hid-keyboard/)
* [Using USB Keyboard](https://www.pjrc.com/teensy/td_keyboard.html)