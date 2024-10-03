# FWCracker

This script will attempt to guess at your password using most laymens favorited of password paradigms, ie., abc123. It's handy if you often use such passwords 
with firmware locks on your devices.

*There are three things you'll need other than what you probably already have those being a Python interpreter and an IDE:*

	1. A HID recognizable Keyboard/emulator, preferably one which can send and recieve RS-232. These can be found easily online, but so far I've only found retailers overseas.
	2. A USB to TTL cable to connect to the emulator. These are more easily found here.
 	3. A module called PySerial which can be had from PyPi.org via pip.
	
*You can visit the following link to see what the hid/emulator looks like:* https://tinyurl.com/5xe4n4mn

Ok, honestly, this exploit was patched way back in 1984 around the time when the BIOS was first developed, when I was literally around 10 years old, and when I was first introduced to all this.
Most modern and ancient BIOS's have security features built in, like Admin passwords, or perhaps the system will kick out after a few failed attempts.
Anyhow, if you read further you may be able to tailor the code/script so to reach your goal(s). For very old systems it's most likely a timing issue which is defeating you.

# SUPPORT

If FWCracker can't find *pyserial-ports* you'll have to add it to your *PATH*.

You can find it on linux as su:

	find / -name pyserial-ports
 
