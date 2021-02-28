# Zog

Zog is a Z80 based collection of parts that I've been playing with. It consists of a vintage S-100 card called the [Solid State Music SSM CB2 Z80 CPU S-100](http://www.s100computers.com/Hardware%20Folder/SSM/Z80%20CPU%20Board/Z80%20CPU.htm) that I was lucky enough to find on ebay for a pittance, and it still works!

I originally bought it to bring Z80 support to the [Altair8800c](https://deramp.com/altair_8800c.html) kit that I built, but I found another - more barebones but Altair friendly - card on ebay, and used that in the Altair instead. This one sits in the small S-100 set of slots and I can build my own cards and do weird stuff. I really should stick to the [RC2014](https://rc2014.co.uk) which is Z80 based and because it has *always* been Z80 based doesn't have the weird 8080-compatible I/O stuff or power requirements that S-100 uses, and is therefore a lot simpler to build hardware for. But there is something about the size of these big old cards that I enjoy.

![](zog.jpg)

The SSM card has two sockets for memory on it: in my case, the first holds a ROM at address 0x0000 and the second a 2Kb RAM chip at address 0x2000. The SSM card has an 8-bit I/O port which I use to connect to random things, including a set of original [TIL311](https://www.hackster.io/news/build-a-replica-til311-with-22-leds-and-an-atmega328p-e2fac423b974) LEDs on a [board](https://github.com/GrantMeStrength/Electronics/tree/master/TIL%20Display) I built and an Arduino Nano which drives an LCD panel over a crude DIY serial protocol.

I've recently been using the [EPROM-EMU](https://www.tindie.com/products/mygeekyhobby/eprom-emulator-diy-arduino/) to speed up development, and can send Z80 binary code to it without issue. However, I'm currently unable to get [z88dk](https://z88dk.org/site/) to compile C for it, and that's what I am hoping to use a development platform to write a simple OS.

Status: Blocked until I can get Z88dk working. I have a [S-100 bus card](https://deramp.com/downloads/mfe_archive/010-S100%20Computers%20and%20Boards/01-Jade/10-Jade%20S100%20Boards/Jade%20Bus%20Probes/Jade%20S100%20Bus%20Probe%20card.pdf) to build which might help diagnose which is going on, but I suspect the non-RC2014 memory map of the SSM card is the issue and if I add 32Kb of RAM at 0xC000 it might work. Or there is some interupt stuff going on in which case who knows.

## Video

I found a video card on eBay - the [SSM VB1B](https://wiki.theretrowagon.com/wiki/SSM_VB1B). I've had luck with SSM cards, and this one was cheap, so... Even came with the [manual](http://www.s100computers.com/Hardware%20Manuals/SSM/SSM%20VDB-1.pdf). I see one on eBay today for ten times the price I paid, so I guess I lucked out. I was getting ready to try it when someone spotted it was missing one of the voltage regulators. Oops! Luckily 7805 regulators is something I've got in my parts drawer, so I swapped out the existing regulator and replaced the missing one. I removed the Character Generator ROM and some other odd look chips (hard to find a replacement maybe?) and tested the voltages - all good. So I put it all back together, added a video cable and dropped it into the Altair 8800c clone and after some fiddling with various video leads and monitors.. it works! Mostly. It ould do with some adjusting or maybe replacing some tired chips, but hey - not bad! 

The (super cheap) composite to HDMI adaptor I have produces rolling junk on an LCD display, but the Apple IIc mono monitor worked.. and so did the LCD monitor when I connected the composite lead directly. Need to check the video signal with the 'scope and see if there are obvious issues.

![](1.jpeg)

![](3.jpeg)

To display something, the card just needs something poked into memory between $EC00 to $EFFF. The front panel wasn't doing it (the front panel is picky about what it can write to, and this card has some special magic to allow both the S-100 bus and the video generator to see the on-board RAM) but a small Z80 test program that I toggled in made the text update away. Success! The character set is actually considerably better than the ZX81 from 4 years later.. Lowercase, symbols and graphics. Not bad.

![](2.jpeg)

I can't move this card into Zog yet, as the Zog only has a 5 volt supply and this card requires a few milliamps at 12 and -3 volts for that character ROM. However, DigiKey is mailing me a [small unit](https://www.digikey.com/en/products/detail/mornsun-america-llc/A0512S-1WR3/13168378) that can take +5 and provide +/- 12v which should be ideal. 

![](4.jpeg)
