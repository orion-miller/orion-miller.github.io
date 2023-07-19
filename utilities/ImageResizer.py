import os
from PIL import Image

'''This function will cycle through all the images in the assets/images folder and resize them as needed to ensure fast web page performance. 
PNG files are converted to JPG because of lower file, and then will be resized to below 500 KB if still larger than that.
The string "SKIPPNG" can be used in the filename of any PNG image that the JPG conversion needs to be skipped on for any reason'''

FullFileName = os.path.realpath(__file__)
WorkingDir = FullFileName.split('utilities')[0]
ImageDir = WorkingDir + "assets\\images\\"
ImageFolders = [ f.path for f in os.scandir(ImageDir) if f.is_dir() ]

for Folder in ImageFolders:
    os.chdir(Folder) #Switch dir to image folder
    for File in os.listdir(Folder):
        #Check if file is a PNG, not containing the "skip string" SKIPPNG
        if File.endswith(".png") & File.count('SKIPPNG') == 0:
            #Convert PNG to JPG, delete the original PNG file
            IMG = Image.open(File) #Read in as png
            # SaveName = Folder + "\\" + File.split('.png')[0] + ".jpg"
            SaveName = File.split('.png')[0] + ".jpg"  
            IMG_JPG = IMG.save(SaveName) #Write out as jpg

    


FileName = ImagesDir+'2023-07-10-adding-bluetooth-to-pontiac-radio\\1.png'
FileSize = os.path.getsize(FileName)

#Check if file is larger than 1 MB, if so resize it
if FileSize > 1000000: 
    IMG = Image.open(FileName)  # My image is a 200x374 jpeg that is 102kb large
    IMG.size  # (200, 374)
 
# downsize the image with an ANTIALIAS filter (gives the highest quality)
IMG = IMG.resize((160,300),Image.ANTIALIAS)
 
IMG.save('path/to/save/image_scaled.jpg', quality=95)  # The saved downsized image size is 24.8kb
 
IMG.save('path/to/save/image_scaled_opt.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb