# from PIL import Image


# a = "original.jpg"

# #open file with the original image

# with Image.open(a) as file:
#     print(file.size)
#     print(file.mode)
#     print(file.format)

# pic_gray = original.convert('L')
# pic_blured = original.filter(ImageFilter.BLUR)
# pic_up = original.transpose(Image.ROTATE_180)

# pic_gray.save('gray.jpg')
# pic_blured.save('blured.jpg')
# pic_up.save('uo.jpg')

# image.FLIP_LEFT_RIGHT




from PIL import Image
from PIL import ImageFilter

with Image.open('original.jpg') as file:
    print(file.size)
    print(file.mode)
    print(file.format)


with Image.open('original.jpg') as pic_original:
 
 pic_original.show()
 pic_gray = pic_original.convert('L') 
 pic_gray.save('gray.jpg')
 pic_gray.show()

 pic_blured = pic_original.filter(ImageFilter.BLUR)
 pic_blured.save('blured.jpg')
 pic_blured.show()
 
 pic_up = pic_original.transpose(Image.ROTATE_180)
 pic_up.save('up.jpg')
 pic_up.show()

 pic_up = pic_gray.transpose(Image.ROTATE_180)
 pic_up.save('up.jpg')
 pic_up.show()

pic_flip = pic_original.image.FLIP_LEFT_RIGHT
pic_flip.save('miror.jpg')
pic_flip.show()
#pic_mirror = pic_original

#change the color of original to white and black 

#make the image blur 

#rotate original by 180 degrees

