from PIL import Image
import math
import os
import base64
import zlib

class ImageEncoderHelper:
    def calculateImageSize(self, data_arr):
        length = 8
        lines = ""
        for data in data_arr:
            lines += data
        length += len(base64.b64encode(zlib.compress(lines.encode())).decode())
        imgsz = round(math.sqrt(length))
        print(f"imgsz: {str(imgsz)} x {str(imgsz)}")
        return imgsz
    def getImageSize(self, img_p):
        img = Image.open(img_p)
        return img.size

class ImageEncoder:
    def __init__(self, image_path, sz = 100):
        self.imgPath = image_path
        self.x = 0
        self.y = 0
        if (os.path.exists(self.imgPath)):
            print("warn! img path points to existing image, any command will overwrite this image without further warning")
            self.img = Image.open(self.imgPath)
        else:
            self.img = Image.new("RGB", (sz, sz))

    def fileToImg(self, filename):
        if (not os.path.exists(filename)):
            print("fileToImg(): err! file doesn't exist")
            return
        with open(filename, "r") as f:
            lines = f.readlines()
            lineFull = ""
            for i, line in enumerate(lines):
                print(f"fileToImg(): wrote {str(i)} lines", end="\r")
                lineFull += line
            line = base64.b64encode(zlib.compress(lineFull.encode())).decode()
            self.strToPixel(line, self.x, self.y)
            self.setPixel(self.x, self.y, 255, 0, 0)
            print("\n", end="")
    
    def imgToFile(self, file):
        if (os.path.exists(file)):
            print("imgToFile(): err! file exists")
            return
        w,h = self.img.size
        string = ""
        breakAll = False
        for y in range(h):
            for x in range(w):
                pix = self.getPixel(x,y)
                if (pix == (255,0,0)):
                    breakAll = True
                    break
                r,g,b = pix
                string += chr(b)
            if (breakAll):
                break
        with open(file, "w") as f:
            f.write(zlib.decompress(base64.b64decode(string.encode())).decode())

    def setPixel(self, pX, pY, r, g, b):
        self.img.putpixel((pX, pY), (r,g,b))

    def getPixel(self, pX, pY):
        return self.img.getpixel((pX, pY))

    def strToPixel(self, string, pX, pY, overflow = True):
        self.y = pY
        self.x = pX
        w,h = self.img.size
        for s in string:
            rCol = ord(s)
            self.setPixel(self.x, self.y, 0,0,rCol)
            self.x += 1
            if (self.x >= w):
                if overflow:
                    self.y += 1
                    self.x = 0
                else:
                    print("err: image too small, overflow = false, stopping here")
                    return
            if (self.y >= h):
                print("err: image too small. stopping here")
                return
    def save(self):
        self.img.save(self.imgPath)
