---
title: "How to Add Bluetooth to a Pontiac Monsoon Radio"
mathjax: true
layout: post
categories: media
excerpt_img_url: ../assets/images/2022-10-14-outboard-motor-repair/79_mercarb.png
tags: hands-on
---

![](/assets/images/2023-07-10-adding-bluetooth-to-pontiac-radio/1.png)

This details how to add a bluetooth transmitter to a Pontiac AC Delco Monsoon radio for a 1998 Pontiac Trans Am. The same process may be applicable for other Trans Ams and Camaros of similar year.

## The Goal
The idea of this install is to add bluetooth to the car while keeping the look and functionality of the original radio. The total cost will be around $40.

## The Approach

![](/assets/images/2023-07-10-adding-bluetooth-to-pontiac-radio/Parts_Assembly.png)

|#|Parts List|
|-|-----------|
|1|Bluetooth 5V Receiver Board|
|2|Small aux cord - 3.5 mm to 3.5mm|
|3|Ground Loop Isolator|
|4|Small aux cord - 3.5 mm to bare wires|
|5|USB to Micro-USB Cable|
|6|USB Car Charger|

The receiver board makes the bluetooth connection and transmits the audio to the CD player audio inputs, through the ground loop isolator and auxilary cords. To run the board requires a 5V power source or 3.7-5V battery. We will be powering it off the car to avoid having to recharge/replace a battery. A cheap USB car charger will be used to accomplish this is an easy pre-made circuit for converting 12V to 5V. The car charger will be taken apart and its internals will be connected to the 12V accessory power of the cigarette lighter.

# Steps
The board was first tested with its ground loop isolator to confirm these work as expected before doing the install. Playing sound from a computer and then from the bluetooth board little to no difference in audio quality was noticed.

Pop off the front plastic faceplate and remove the bolts holding in the radio.
Pull out the radio and undo the connections.
Disassemble the radio with torx screwdrivers, and undo the connector from the CD player to the main board.

Strip the outer insulation off the aux wire to get the 3 strands on their own. Solder the red wire to the first connector pin (left audio channel) and the white wire to the third connector pin (right audio channel). The yellow wire can then be soldered anywhere convenient on the radio chassis for the ground.Tape off the original audio wires from the CD player that have been cut.
The correct colors for the aux wire were confirmed by testing continuity. 

Mount the bluetooth board on the chassis. There is room on the side with the heatsink for this. Then run the power and aux cord out the back of the radio, either through the CD player mounting holes or drilling separate holes. Attach the ground loop isolator onto the back of the radio towards the top, so it wont interfere when re-installing the radio into the dash. Re-assemble the radio.

Pull off the casing from the car charger and solder new wires onto the positive and negative. In this case I also extended the existing LED to use as a gear indicator light under the shifter because the car doesn't come with one originally.

Remove the traction control panel and strip the wires on the 12V accessory/cigarette lighter for a T-splice. Solder the car chargers new wires in and secure the car charger down somehow (here just wrapped it in shop cloth and taped it down).

Reinstall the radio, feeding the power cable down in behind the traction control panel to the power source, and reinstall the faceplate.

Turn the radio on in CD mode (with a CD inside), connect with bluetooth to the board, and play audio!















