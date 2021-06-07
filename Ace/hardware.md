# Jupiter Ace Hardware

Back in 1984 I somehow had two Jupiter Ace RAM packs. I can't remember exactly why, but I think I was sent another Ace and RAM pack to help write some games by the company that wanted to publish some of my amazing (sic) stuff.

Anyway, I thought - wow, why don't I try and connect both RAM packs to the same computer. With a little messing with the addresses, I bet it would work. (A little knowledge is a dangerous thing). So I tried, and immediately broke the Ace. Luckily I had a second one, so just switched to using it.

But that broken Jupiter Ace has weighed heavily on me ever since. I can't find the PCB any more to try and repair it (sigh) but I do have the case and keyboard (well, they are at my mum's house). So, one day when I spotted an original Jupiter Ace unpopulated PCB on eBay, it was a total "buy now" situation. 

Since then I've been gathering all the parts to get it started. I was hoping to be visiting my mum soon to pick up the PCB but that was a year ago! so I'm going to have to get her to mail to me. I also have a ZX81 composite video adpator kit to sort out the display, and a [replacement for the 5v regulator](https://www.tindie.com/products/ddebeer/5v-1a-switch-mode-voltage-regulator/) to keep the heat down (I think I have the original heatsink metal piece but I'm not sure).

Aside from not having the PCB in front of me, I'm also blocked with the EPROMS. The Ace uses a pair of 4Kb 2532s which are odd compared to the 27c32 types I am more familiar with. For one thing, the programming requirements are different so my TL866II won't support them. They also have different pin-outs, so an adpator board would be required - which I'd like to avoid. I'm hoping someone in work can program them for me (I found some on eBay, and [according to my tester](https://store.backbit.io/product/chip-tester/) they are good.)

Ordering RAM was a pain. The Ace uses six 2114 static RAM chips. I initially thought it used three, and found and bought three on eBay. So I was half right.

The second place I tried was ABRA Electronics. Their website said they had them in stock, so I bought six to keep them all matched (there are different versions with different speeds, and matching might work but I'd like ot keep it simple - for $2 I can afford it). The postage was higher than the cost of the chips. Then I got an email saying "Sorry, we don't have them in stock. We're in Canada. And the minimum order is $50 anyway". (Their website said they did have stock, didn't mention they were Canadian - nothing wrong with that, BTW - and didn't mention the minimum order when I paid them..)

Thankfully good old [JameCo](https://www.jameco.com) had them (why didn't I check there first? No idea.) so they arrived the other day.

If you want to build your own without the original PCB, [here's the definitive guide](http://jupiter-ace.co.uk/hardware_diy_ace.html). As the Ace uses no custom chips at all, it should be "easy". 

If you want to build a new one from a kit, [ask these folks to start making the kit again](https://www.thefuturewas8bit.com/minstrel4th.html).

## May 30, 2021

My PCB arrived (thanks, Mum!) and I immediately got stuck into soldering the amassed collection of components. 

The only I had forgotten was, ironically, the easiest to get - 1K resistors. Thankfully I had time on Saturday to visit Vetco.net before it shut down for the Memorial Day break and stock up on the 30-ish that the kid required.

Finally I finished it, plugged it in and - garbage. Just random junk on the screen. And in fact, removing the Z80 or swapping in another Z80 didn't help. A check of the clock signal showed things were not great:

![](../images/ace-clock.png)

The trouble, as far as I can tell, is the transistor. The 2N2369 isn't easy to get hold of these days - but it's a very fast switching transistor - faster than any of the substitutes listed, and which I was using. So without a fast transistor I'm stuck until the one I found on Mouser arrives (hopefully next week).


## June 5, 2021

The replacement transistor arrived! Hurrah! I made no difference! Boo!

No, that's not true at all. The updated transistor meant that the CPU was getting a clock signal, and it was able to run - but the screen was displaying garbage still. RAM was a suspect, so I checked the RAM chips - and half were faulty! JAMECO had let me down! First time for everything, I suppose! I plugged in the first batch chips I had bought and there were enough to replace the broken ones - and there was movement! The keyboard did definitely cause the screen to update as though I were typing, but it was still nonsense. But this means the Z80 is running, the ROMs are working - but the RAM or the RAM control circuitry is broken. I don't trust any of the JAMECO RAM, so it's back to eBay, and another long wait for replacement chips.
