# ImageEncoder example: Macbeth

## How to encode

```
python3 main.py --encode ./Macbeth.txt ./Macbeth.png
```
(``Macbeth.png`` should not exist)

## How to decode

```
python3 main.py --decode ./MacbethDecoded.txt ./Macbeth.png
```
(``MacbethDecoded.txt`` should not exist)

## How well does decoding work?

The decoded file is the exact same as the encoded one, output of ``md5sum Macbeth.txt MacbethDecoded.txt``:
```
5e5418007467543d0718d33875441155  Macbeth.txt
5e5418007467543d0718d33875441155  MacbethDecoded.txt
```