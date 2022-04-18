# ImageEncoder
Encode any text into an image! Written in Python.

**Disclaimer:** Make sure ``ImageEncoder.py`` and ``main.py`` are in the same directory when running the program!

**If you would like to compile this program**, install ``pyinstaller`` and run ``pyinstaller --onefile main.py`` in the program directory. It will create a file called ``main`` in the ``dist/`` folder, which you can use without having to use Python. The commandline arguments are the same for the compiled binary.

**For an example** see the ``example/`` directory.

## Dependencies
- PIL library (to modify images)
- Base64 library (to store binary as text)
- ZLib library (for txt compression)