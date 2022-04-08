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
If you want a Caps Lock LED, the Teensy 2 or 2++ doesn't quite have enough pins, and needs a shift register to help.
If you can live without the LED, no other ICs are required.

The problem is that Teensy's are hard to find at the moment. 

I briefly considered the Pi Pico (as I have several) and then thought "ah, the Pico is 3.3v and the Apple keyboard needs 5v."
Then I realized: the Apple keyboard is passive. It doesn't care if it's 5v, 3.3v or 12 volts - it's just switches. Ok, the LED needs 5, but so?
So my plan is to write software using the Pico to decode the keyboard, because like the Teensy, it can act as a keyboard HID and it also has plenty of pins. And I have some Picos in my parts drawer.

The Apple IIe keyboard has been ordered from eBay.

## Software

* [Pico as a keyboard](https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/code-the-pico-keyboard)
* [RetroConnector](https://github.com/option8/RetroConnector/tree/master/IIe-USB)
* [Apple IIe Keyboard USB](https://github.com/xunker/apple_iie_keyboard_usb)
* [Keyduino](https://github.com/afiler/keyduino)
* [Arduino USB HID Keyboard](https://mitchtech.net/arduino-usb-hid-keyboard/)
* [Using USB Keyboard](https://www.pjrc.com/teensy/td_keyboard.html)