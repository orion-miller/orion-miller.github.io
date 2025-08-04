---
title: "Viewing rFactor 2 Vehicle Data in Motec i2 Pro"
mathjax: false
layout: post
categories: media
excerpt_img_url: ../assets/images/2025-08-03-rfactor2-motec-workspace/1.jpg
comments: true
tags: automotive data-analysis
---


I recently set up a Motec i2 Pro worskpace for viewing rFactor 2 vehicle telemetry data [here](https://github.com/orion-miller/RFactor2-Motec-Workspace)

![Screenshot](/assets/images/2025-08-03-rfactor2-motec-workspace/1.jpg)

It includes a range of helpful plots making use of most available data channels, and additional calculated math channels.

## Setup Steps

1. [Download Motec i2 Pro](https://www.motec.com.au/downloads)

2. Download this workspace:
![Screenshot](/assets/images/2025-08-03-rfactor2-motec-workspace/repo_download.jpg)

3. Extract workspace, place somewhere convenient, and open in Motec i2 Pro

4. Set up [DAMPlugin](https://forum.studio-397.com/index.php?threads/damplugin-for-rf2.49363/) for rFactor 2 data logging

5. Configure data logging by overwriting the ```DAMPlugin.INI``` file with the one included here, or otherwise setting up as desired. This file controls channel groups to include, and at what resolutions.

You should now be able to log and view data. The sample dataset can be used as a reference to ensure your setup is working properly.

## Logged Channels

Once your DAMPlugin file is configured, population of all channels in this workbook still depends on the car being driven. Tire and/or aero channels are not populated for all cars, although there will still be plenty of useful info without them.

I've made a (non-comprehensive) list of cars that I have found to include full tire data output. 

![Screenshot](/assets/images/2025-08-03-rfactor2-motec-workspace/tire_data.jpg)

Many cars do not output tire data due to confidentiality agreements for rFactor's partnerships with tire companies.

## Math Channels

Calculations are included for a range of math channels:

![Screenshot](/assets/images/2025-08-03-rfactor2-motec-workspace/math.jpg)
