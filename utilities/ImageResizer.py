import os
from PIL import Image
import math

'''This function will cycle through all the images in the assets/images folder and resize them as needed to ensure fast web page performance. 
PNG files are converted to JPG because of lower file, and then will be resized to below 500 KB if still larger than that.
The string "SKIPPNG" can be used in the filename of any PNG image that the JPG conversion needs to be skipped on for any reason'''

#Find all subfolders under the assets/images directory
FullFileName = os.path.realpath(__file__)
WorkingDir = FullFileName.split('utilities')[0]
ImageDir = WorkingDir + "assets\\images\\"
ImageFolders = [ f.path for f in os.scandir(ImageDir) if f.is_dir() ]

#Loop thru folders and files, process image files
for Folder in ImageFolders:
    os.chdir(Folder) #Switch dir to image folder
    for File in os.listdir(Folder):
        #Check if file is a PNG, not containing the "skip string" SKIPPNG
        if File.endswith(".png") and File.count('SKIPPNG') == 0:
            #Convert PNG to JPG, delete the original PNG file
            IMG = Image.open(File) #Read in as png
            IMG = IMG.convert('RGB') #Ensure RGB format
            SaveName = File.split('.png')[0] + ".jpg"  
            IMG.save(SaveName, optimize=True, quality=85) #Write out as jpg
            os.remove(File) #Remove the original png file
            File = SaveName #Overwrite name of file - to be referenced in next step           

        #Check if file is a JPG, and over 500 KB
        if (File.endswith(".jpg") or File.endswith(".JPG")) and os.path.getsize(File) > 500000:   
            FileSize = os.path.getsize(File)
            ResizeRatio = 500000/(FileSize + 10000) #Resize ratio, with a little fudge factor to make sure final file comes below 500 KB (math below is not exact)
            IMG = Image.open(File) #Read in jpg

            #Calculate new dimensions       
            NumPixels = IMG.size[0]*IMG.size[1]
            AspectRatio = IMG.size[0]/IMG.size[1]
            NumPixelsNew = ResizeRatio*NumPixels
            HeightNew = math.sqrt(NumPixelsNew)/1 + AspectRatio
            HeightNew = int(HeightNew)
            WidthNew = int(HeightNew*AspectRatio)

            #Resize and over-write
            IMG = IMG.resize((WidthNew,HeightNew),Image.ANTIALIAS) #Resize  
            IMG.save(File, optimize=True, quality=85) #Rewrite out jpg                   
