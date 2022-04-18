import os
import sys
from ImageEncode import ImageEncoder, ImageEncoderHelper

lines = []

def encodeImg(fp, ip):
    with open(fp) as f:
        lines = f.readlines()

    imgh = ImageEncoderHelper()
    img = ImageEncoder(ip, imgh.calculateImageSize(lines))
    img.fileToImg(fp)
    img.save()

def decodeImg(fp, ip):
    imgh = ImageEncoderHelper()
    img = ImageEncoder(ip, imgh.getImageSize(ip))
    img.imgToFile(fp)

if __name__ == "__main__":
    if (sys.argv[1] == "--encode"):
        fp = sys.argv[2]
        ip = sys.argv[3]
        if (not os.path.exists(fp) or os.path.exists(ip)):
            print("Error: the filepath must already exist and the image path must not already exist")
        else:
            if (not ip.endswith(".png")):
                print("Error: only .png files are supported for the image")
            else:
                encodeImg(fp, ip)
    if (sys.argv[1] == "--decode"):
        fp = sys.argv[2]
        ip = sys.argv[3]
        if (os.path.exists(fp) or not os.path.exists(ip)):
            print("Error: the filepath must not already exist and the image path must already exist")
        else:
            if (not ip.endswith(".png")):
                print("Error: only .png files are supported for the image")
            else:
                decodeImg(fp, ip)