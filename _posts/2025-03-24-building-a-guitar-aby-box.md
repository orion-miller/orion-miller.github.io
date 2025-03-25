---
title: "Building a Passive AB/Y Guitar Pedal"
mathjax: false
layout: post
categories: media
excerpt_img_url: ../assets/images/2025-03-24-building-a-guitar-aby-box/20250324_082947048_iOS.jpg
comments: true
tags: audio-music hands-on
---

This details how to build an AB/Y box. For 2 different outputs A and B, this allows you to send to either, or both, by stepping on a couple rocker switches. In my case this is for routing signal to 2 different guitar amps to change between sounds on the fly. This design requires no external power and is very simple to build.

## Parts & Equipment

|#|Parts List|
|-|-----------|
|1|Enclosure - Hammond 1590B or similar|
|2|3x 1/4" mono audio jacks - Switchcraft or similar|
|3|2x DPDT rocker switches|
|4|Electrical wire|

[Digikey](https://www.digikey.com/) is a good resource for parts! 

|#|Equipment List|
|-|-----------|
|1|Drill|
|2|Soldering Iron|
|3|Dremel or other cutting tool for rocker switch holes|

## Design

The upper rocker switch when pressed up or down controls whether sound is sent to the ```A/B``` switch, or directly to both outputs. (```Y```). The lower rocker switch when pressed left or right controls whether the signal is sent to output ```A``` or ```B```.

![](/assets/images/2025-03-24-building-a-guitar-aby-box/ABY_Schematic.jpg)
*Schematic*

Because of the way the switches contacts move, the wiring may appear "reversed", but operation is as follows:

|Upper Switch|Lower Switch|Effect|
|-|-----------|-----------|
|Down|Left|Signal goes to output A|
|Down|Right|Signal goes to output B|
|Up|N/A|Signal goes to output A and B, lower rocker switch has no effect|


## Steps

1) Drill holes for jacks, one in right side, 2 in top (yes I mis-drilled a hole in the bottom, but used the enclosure anyways!). Can also pre-drill round holes for the step following.

![](/assets/images/2025-03-24-building-a-guitar-aby-box/20250126_191951.JPG)

2) Create rectangular slots in top for rocker switches. I used a mill which is a little overkill, but a dremel or other cutting tool can do the job.

![](/assets/images/2025-03-24-building-a-guitar-aby-box/2.jpg)

3) Install components and wire up according to the schematic.

![](/assets/images/2025-03-24-building-a-guitar-aby-box/20250324_081355901_iOS.jpg)

On the outside of the enclosure I also crudely drew the signal paths, and added paint to the ends of the rockers, to give a clean visual indicator of the switch positions. Most switches use footswitches and LED's, where here with painted rockers we get something thats still operated by foot, still indicates status, but doesn't need to use another spot on the power supply!

![](/assets/images/2025-03-24-building-a-guitar-aby-box/20250324_082947048_iOS.jpg)

















