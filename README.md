# FWCracker_v1
Firmware Bypass CLI Utility

This is the original script for FWCracker which isn't very developed but works all the same. What you'll need to do is change the constants in the script to the words or phrases you might have used when you set the password.
The idea was to help with simple passwords, abc123 like patterns where the user has simply forgotten the number part of the sequence which is sometimes a average occurence. In that case you can guess what number you
would have used, and the word/phrase part of the sequence to hopefully regain access to your system without having to wipe any data. What the app will do is iterate the numbered part of the password until it guesses the 
right combination, given the phrase part of the sequence is correct. 

Although this can appear as kind of a half-measure, those who use these patterns of aware of how easily it is to forget the numbered portion and not the phrase, so, for those users this will likely help.

FWCracker 2 is a tad more practical since it asks you for these variables without you having to modify the script. FWCracker 3 will have a nice GUI wrapped around the utility to make things even smoother.

# Installation

Download/clone FWCracker_v1

    git clone https://github.com/odioski/FWCracker_v1.git

Install PySerial with pip

    pip install pyserial

Run the script:

    python FWCracker.py

# Support

As mentioned you'll need an HID keyboard/emulator, a tiny piece of hardware for this to work optimally. They can be had for a only a few bucks from a few different vendors. That and PySerial along with Python installed is all.

*You can see what the keyboard/emulator looks like by visiting here: https://tinyurl.com/5xe4n4mn*

As a precaution, you should run FWCracker from the safety of your venv. You should also launch your venv before you install PySerial. If FWCracker has trouble finding *pyserial-ports*, then you'll need to add it to your *PATH*