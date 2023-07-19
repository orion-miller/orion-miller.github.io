from PIL import Image

foo = Image.open('..\\assets\\images\\2023-07-10-adding-bluetooth-to-pontiac-radio\\1.png')  # My image is a 200x374 jpeg that is 102kb large
foo.size  # (200, 374)
 
# downsize the image with an ANTIALIAS filter (gives the highest quality)
foo = foo.resize((160,300),Image.ANTIALIAS)
 
foo.save('path/to/save/image_scaled.jpg', quality=95)  # The saved downsized image size is 24.8kb
 
foo.save('path/to/save/image_scaled_opt.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb