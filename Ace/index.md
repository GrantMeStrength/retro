## Jupiter Ace Software

Here you will find a collection of games for the [Jupiter Ace](https://jupiter-ace.co.uk/whatisanace.html) microcomputer, written by me in around 1984. They are mostly in [FORTH](https://jupiter-ace.co.uk/whatisforth.html), with the occasional Z80 assembler for sound effects, or extra-fast scrolling routine.

I had planned to make my fortune by selling these games to Boldfield Limited Computer, the company that had bought the assets of Jupiter Cantab. Sadly that did not work out, so they're still all my intellectual property (I am using the term lightly :))

## Writing games for the Ace

The Jupiter Ace had a character-mapped screen, with a limited number of User Defined Graphics. This meant writing games with smooth animation was a challenge.

At once point I investigated if I could fake a kind of higher resolution by displaying the User Defined Graphics on the screen and then writing into them on the fly - hoping to get a 256 by 192 resolution screen, at least in parts of the screen (there aren't enough UDG to cover the entire screen). Unfortunately writing to the UDG memory every frame quickly caused it to be become corrupt, so I had to give up that approach.

The Ace was described as "fast", and it was in the sense that instead of a slow BASIC, as on the ZX81 or ZXSpectrum, it came with Forth in ROM. Forth is nothing if not fast, and was perfect for writing simple games. Under the (thin plastic) hood it was still a Z80 and a handful of chips, with a cassette interface for saving and loading programs to tape. Running machine code wasn't any faster than a Spectrum. 

![](jupiter_ace_advert.png)

The Ace was not in production for long (the ZXSpectrum soon stole any of its potential sales, with its flashy games, better case and colour graphics), so is seen as something of a quirky experiment. Originals turn up on eBay from time to time, but there is also at least one [kit called the Minstrel4th](https://www.thefuturewas8bit.com/minstrel4th.html) around to recreate it. The PCBs also are avalable. There are no custom chips, so there are no surprises. If you look on Tindie there is now an [SD card interface called the Jester Ace](https://www.tindie.com/stores/dr_ian_johnson/) to save/load software. It's these kits, and a forthcoming emulator for iPhones and iPads, that encouraged me to get these games uploaded somewhere.


Here then is what I came up with - mostly adaptations of arcade games I had seen at the time.

![](shot1.png)

![](shot2.png)

![](shot3.png)

![](shot4.png)

## Files

The games can be downloaded in TAP format, and used on various emulators and recreations of the hardware.

Note: Some games use IN to read the keyboard port, and these won't work on anything other than the real hardware.

I hope to get around to updating them to work in a more emulator-friendly way.


## Thanks

Thanks to the [Jupiter Ace Archive Site](https://jupiter-ace.co.uk) for recovering, capturing and storing my software. Without them, they'd have been lost forever.