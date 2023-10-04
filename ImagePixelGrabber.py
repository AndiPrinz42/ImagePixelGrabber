# ImagePixelGrabber 1.0
# by Andreas Prinz
# All rights reserved

from PIL import Image
import pathlib
from numpy import savetxt
print("----------------------------------------------")
print("ImagePixelGrabber1.0 by Andreas Prinz\nAll rights reserved")
print("----------------------------------------------\n\n")

image = None
imagePath = None
while True:
    try:
        print("Image Path (Relative or Absolute)")
        imagePath = input(">>> ")
        image = Image.open(imagePath)
        break
    except Exception as e:
        print(e)
        print("Please try again!\n")
        pass

fileFormat = pathlib.Path(imagePath).suffix
transparency = False
if fileFormat == '.png' or fileFormat == '.gif':
    transparency = True

width, height = image.size
print()
print("Width: " + str(width))
print("Height: " + str(height))
print()

include = None
while include == None:
    print("'include' or 'exclude' color values?")
    inputStr = input(">>> ")
    if inputStr == 'include':
        include = True
    elif inputStr == 'exclude':
        include = False
    else:
        print("Invalid Input!\nPlease try again!\n")
print()
if include:
    print("Enter color value for included color")
else:
    print("Enter color value for excluded color")

red = -1
green = -1
blue = -1
alpha = -1

while True:
    red = int(input("R > "))
    if red in range(0, 256):
        break
    print("Invalid Input\n")

while True:
    green = int(input("G > "))
    if green in range(0, 256):
        break
    print("Invalid Input\n")

while True:
    blue = int(input("B > "))
    if blue in range(0, 256):
        break
    print("Invalid Input\n")

image_rgb = None
if transparency:
    while True:
        alpha = int(input("A > "))
        if alpha in range(0, 256):
            break
        print("Invalid Input\n")
else:
    alpha = 255

image_rgb = image.convert("RGBA")
smallestSide = None
if width > height:
    smallestSide = height
else:
    smallestSide = width

print()
precision = None
while True:
    print("Enter precision (Higher Value = Lower Precision)")
    precision = int(input(">>> "))
    if precision in range(1, smallestSide+1):
        break
    print("Invalid Input!\nPlease try again!\n")
print()
print("Processing...", end="\r")
xValues = []
yValues = []

count = 0
if include:
    y = 0
    while y < height:
        x = 0
        while x < width:
            pixel = image_rgb.getpixel((x, y))
            found = False
            if pixel[0] == red:
                if pixel[1] == blue:
                    if pixel[2] == green:
                        if pixel[3] == alpha:
                            found = True
            if found:
                xValues.append(x)
                yValues.append(y)
                count += 1
            x += precision
        y += precision

else:
    y = 0
    while y < height:
        x = 0
        while x < width:
            pixel = image_rgb.getpixel((x, y))
            found = False
            if pixel[0] != red or pixel[1] != blue or pixel[2] != green or pixel[3] != alpha:
                found = True

            if found:
                xValues.append(x)
                yValues.append(y)
                count += 1
            x += precision
        y += precision

print("Found "+str(count)+" matches!")

while True:
    print("\n'print' calculated values to Console\n'save' calculated values to Text-File\n'exit' the Program")
    inputStr = input(">>> ")
    if inputStr == 'print':
        while True:
            print("'x' or 'y' coordinates?")
            inputStr = input(">>> ")
            if inputStr == 'x' or inputStr == 'y':
               break
            else:
               print("Invalid Input!\nPlease try again!\n")
        print("\n")
        if inputStr == 'x':
            print(xValues)
        else:
            print(yValues)
    elif inputStr == 'save':
        while True:
            print("'x' or 'y' coordinates?")
            inputStr = input(">>> ")
            if inputStr == 'x' or inputStr == 'y':
                break
            else:
                print("Invalid Input!\nPlease try again!\n")

        print("filename?")
        filename = input(">>> ")
        try:
            print("Saving...", end="\r")
            if inputStr == 'x':
                savetxt(filename+'.txt', xValues, fmt='%s', newline=",")
            else:
                savetxt(filename+'.txt', yValues, fmt='%s', newline=",")
            print("Saved as '"+filename+".txt'\t\t")
        except Exception as e:
            print(e)
            print("Please try again!\n")
            pass
    elif inputStr == 'exit':
        break
    else:
        print("Invalid Input!\nPlease try again!\n")