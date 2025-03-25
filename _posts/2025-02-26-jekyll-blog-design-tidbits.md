---
title: "Jekyll Blog Design Tidbits"
mathjax: false
layout: post
categories: media
excerpt_img_url: ../assets/images/2025-01-26-using-local-music-library-with-plexamp/Plexamp.jpg
comments: true
tags: audio-music programming
published: false
---

Instead of using streaming services you might prefer to keep your own music library. This way you don't need to have subscriptions, and can maintain your own files including live, obscure, or unique tracks you can't find streaming. A nice way to do this is with [Plexamp](https://www.plex.tv/plexamp/), a simple and great looking music player. This also allows you to self-host and listen across multiple devices.

To get your files visible in Plexamp, you'll have to import them to Plex, by setting a location for your music library and then scanning the files.

![](/assets/images/2025-01-26-using-local-music-library-with-plexamp/Plex.jpg)

To have the proper album artwork and other info show up in Plexamp, if these aren't already populated in your files you can use [Musicbrainz Picard](https://picard.musicbrainz.org/) to automatically find and save them.

- Open Musicbrainz Picard
- Add the folder you want to work in
- Select unclustered files on the left side, scan everything to have it find the metadata and album artwork from the audio tracks
- It'll show the organized/updated files on the right side. Select them all and hit save for the new info to be written

![](/assets/images/2025-01-26-using-local-music-library-with-plexamp/Picard.jpg)
*Musicbrainz Picard*

To then sort your files into subfolders by the artist and album, you can run the following Python script:

    {% highlight python linenos %}
    import os
    import colorama as cr
    from tkinter import filedialog

    import eyed3

    #get music directory from user
    music_dir = filedialog.askdirectory(title="Select Music Directory")
    os.chdir(music_dir)

    music_dir_files = os.listdir(music_dir) #get contents of directory
    music_dir_files = [f for f in music_dir_files if os.path.isfile(music_dir+'/'+f)] #filter for files only (no folders)
    num_files = len(music_dir_files)

    for index, filename in enumerate(music_dir_files): #loop through all files in root of folder
        iteration_string = f"{index + 1} of {num_files}: "

        #load mp3 file
        mp3_data = eyed3.load(filename)    

        #check if metadata is properly populated
        if mp3_data is None or mp3_data.tag is None or mp3_data.tag.artist is None or mp3_data.tag.album is None:
            print(cr.Fore.RED + iteration_string + f"File metadata not populated for {filename}")        
            continue

        #assemble full path
        file_dir = music_dir + "\\" + mp3_data.tag.artist + "\\" + mp3_data.tag.album.replace(":","")
        full_filename = file_dir + "\\" + filename

        #create file path if not existing
        if not os.path.isdir(file_dir):
            try:
                os.makedirs(file_dir)
            except:
                print(cr.Fore.RED + iteration_string + f"Failed to create directory {file_dir}")
                continue

        #move file to path
        try:
            os.rename(music_dir + "\\" + filename, full_filename)
            print(cr.Fore.GREEN + iteration_string + f"Moved {filename} to {file_dir}")
        except:
            print(cr.Fore.RED + iteration_string + f"Failed to move {filename} to {file_dir}")

    {% endhighlight %}

Upon running the script you'll see terminal output confirming by file whether they were successfully moved into folders. For any files that fail, Picard likely was not able to identify the track. This will often happen with live recordings.

![](/assets/images/2025-01-26-using-local-music-library-with-plexamp/TerminalOutput.jpg)
*Terminal Output*

Then your library is all set up, so run the Scan Files step above and listen!

![](/assets/images/2025-01-26-using-local-music-library-with-plexamp/Plexamp.jpg)
*Running Plexamp*
















