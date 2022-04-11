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

## Using a Pico to scan a keyboard

* [Circuitpython Raspberry Pi Pico USB HID Keyboard (the smallest keyboard, part 2)](https://youtu.be/V2ivH2PEoiA)
* [Adafruit HID Keyboard library](https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html)



-- Script in Progress ---

# CircuitPython/Raspberry Pi Pico'firmware' based on The Smallest Keyboard
# and adapted for Apple IIe keyboard. The order that the Pico's pins that are wired to the keyboard connector
# will determine the row_pins, column_pins and modifier_pins



# https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
#optional delay before creating the HID for maximum compatibility
time.sleep(1)
led.value = False
time.sleep(1)
led.value = True

#create the HID
kbd = Keyboard(usb_hid.devices)

#set up the row, column, and modifier arrays
rows = [] #  - ROW is OUTPUTS - Y in the Apple diagrams
row_pins = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP17, board.GP16, board.GP8, board.GP13]
for row in row_pins:
    row_key = digitalio.DigitalInOut(row)
    row_key.direction = digitalio.Direction.OUTPUT
    rows.append(row_key)

columns = [] # COLUMNS in INPUTS - X in the Apple diagrams
column_pins = [board.GP9, board.GP11, board.GP10, board.GP12, board.GP18, board.GP19, board.GP15, board.GP20]
for column in column_pins:
    column_key = digitalio.DigitalInOut(column)
    column_key.direction = digitalio.Direction.INPUT
    column_key.pull = digitalio.Pull.DOWN
    columns.append(column_key)

#this is 'overkill' for code consistency and hardware flexibility; you could alternatively connect modifiers directly to a constant high or low and read the switches without an enable/disable pin
#modifier_enable = []
#modifier_enable_pin = [board.GP22]
#for mod in modifier_enable_pin:
#    mod_enable = digitalio.DigitalInOut(mod)
#    mod_enable.direction = digitalio.Direction.OUTPUT
#    modifier_enable.append(mod_enable)

modifiers = []
modifier_pins = [board.GP26, board.GP27, board.GP22, board.GP21, board.GP14]
for mod_pin in modifier_pins:
    mod_key = digitalio.DigitalInOut(mod_pin)
    mod_key.direction = digitalio.Direction.INPUT
    mod_key.pull = digitalio.Pull.DOWN
    modifiers.append(mod_key)

#array of modifier keycodes
mod_keymap = [Keycode.RIGHT_ALT, Keycode.LEFT_ALT, Keycode.CONTROL, Keycode.OPTION, Keycode.SHIFT]

#array of keycodes; if you want to remap see: https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode /'None' values have no physical connection
keymap = [Keycode.ESCAPE,Keycode.TAB,Keycode.A,Keycode.Z,Keycode.FORWARD_SLASH,Keycode.RIGHT_BRACKET,Keycode.KEYPAD_ASTERISK,Keycode.ESCAPE,
	Keycode.ONE, Keycode.Q, Keycode.D, Keycode.X, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW,
	Keycode.TWO, Keycode.W ,Keycode.S, Keycode.C ,Keycode.ZERO, Keycode.FOUR,Keycode.EIGHT,Keycode.LEFT_BRACKET,
	Keycode.THREE, Keycode.E, Keycode.H, Keycode.V, Keycode.ONE, Keycode.FIVE,Keycode.NINE,Keycode.KEYPAD_MINUS,
	Keycode.FOUR, Keycode.R, Keycode.F, Keycode.S, Keycode.TWO, Keycode.SIX, Keycode.PERIOD, Keycode.RETURN,
	Keycode.SIX, Keycode.Y, Keycode.G, Keycode.N, Keycode.THREE, Keycode.SEVEN, Keycode.KEYPAD_PLUS, Keycode.COMMA,
	Keycode.FIVE, Keycode.T, Keycode.J, Keycode.M, Keycode.BACKSLASH, Keycode.QUOTE, Keycode.RETURN, Keycode.DELETE,
	Keycode.SEVEN, Keycode.U, Keycode.K, Keycode.COMMA, Keycode.KEYPAD_PLUS, Keycode.P, Keycode.UP_ARROW, Keycode.DOWN_ARROW,
	Keycode.EIGHT, Keycode.I, Keycode.SEMICOLON, Keycode.PERIOD, Keycode.ZERO, Keycode.LEFT_BRACKET, Keycode.SPACE, Keycode.LEFT_ARROW,
	Keycode.NINE, Keycode.O, Keycode.L, Keycode.FORWARD_SLASH, Keycode.MINUS, Keycode.RIGHT_BRACKET, Keycode.QUOTE, Keycode.RIGHT_ARROW]

#main loop
while True:
    #for m_e in modifier_enable:
        #m_e.value=1 #set the modifier pin to high
    for r in rows: #for each row
        r.value=1 #set row r to high
        for c in columns: #and then for each column
            if c.value: #if a keypress is detected (high row output --> switch closing circuit --> high column input)
                while c.value: #wait until the key is released, which avoids sending duplicate keypresses
                    time.sleep(0.01) #sleep briefly before checking back
                key = rows.index(r) * 8 + columns.index(c) #identify the key pressed via the index of the current row (r) and column (c)
                for m in modifiers: #check each modifier to see if it is pressed
                    if m.value: #if pressed
                        m_key = modifiers.index(m) #identify which modifier
                        kbd.press((mod_keymap[m_key])) #and press (and hold) it
                kbd.press((keymap[key])) #press the (non-modifier) key
                kbd.release_all() #then release all keys pressed
        r.value=0 #return the row to a low state, in preparation for the next row in the loop




		



---

Copied from here: http://apple2.info/wiki/index.php?title=Pinouts#Apple_.2F.2Fe_Motherboard_keyboard_connector

J16 (Numeric Pad)         J17 (Keyboard)
11      X5                X6      26 25   Y7
10      X6                SHFT*   24 23   Y6
9       X4                Y9      22 21   X4
8       X7                X3      20 19   X5
7       n/c               X1      18 17   X7
6       Y5                X2      16 15   RESET*
5       Y2                XO      14 13   GND
4       Y4                Y8      12 11   CNTL*
3       Y3                Y5      10 9    CAPLOCK*
2       Y1                Y4      8  7    SW0/OAPL
1       Y0                Y3      6  5    SW1/CAPL
                          Y2      4  3    +5V
                          Y1      2  1    Y0

        Main Keyboard   Numeric Keypad
        XO      X1      X2      X3  |   X4      X5      X6      X7
------------------------------------+--------------------------------
YO      ESC     TAB     A       Z   |   /       )       *       ESC
                                    |
Y1      1!      Q       D       X   |   DOWN    UP      LEFT    RIGHT
                                    |
Y2      20      W       S       C   |   0       4       8       (
                                    |
Y3      34      E       H       V   |   1       5       9       -
                                    |
Y4      4$      R       F       S   |   2       6       .       RETURN
                                    |
Y5      6"      Y       G       N   |   3       7       +       ,
                                    +----------------------------------
Y6      5%      T       J       M       \|      `~      RETURN  DELETE

Y7      7&      U       K       ,<      +=       P      UP       DOWN

Y8      8*      I       ;:      .>      0)       [{     SPACE   LEFT

Y9      9(      O       L       /?      -_       ]}      '"      RIGHT
Notes:
1)      This is the US layout
2)      Early //e keyboard ROMs had ? LEFT ESC RIGHT SPACE replacing
        the ESC DOWN UP LEFT RIGHT in the numeric keypad section of the 
        above diagram
3)      If you want more details such as the influence of the Control and
        CAPS LOCK keys or the DVORAK layout see pages 7-16 and 7-17 
        of Jim Sather's Understanding the Apple IIe.
4)      Unlike the ][ & ][+, the //e keyboard is completely passive with
        the decoder chip located on the motherboard.
5)      The +5v connection is to run the power light and the Open/Closed
        Apple switches.
6)      The SHIFT, CONTROL, CAPSLOCK and RESET switches simply ground the
        appropriate pin of the connector (RESET via the CTRL line if the 
        jumpers are in the standard setting).