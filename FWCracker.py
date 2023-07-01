
###################################################################################################################################################################################
##
##  THE ORIGINAL FWCracker.............
##
###################################################################################################################################################################################
##   This script will attempt to guess at your password using most laymens favorited of password paradignms, ie., abc123. It's handy if you often use such passwords 
##   with firmware locks on your devices. Most have long since stoped using these particular patterns but if you change the constants to suite your needs, 
##   it should work just fine.
##
##   There are three things you'll need other than what you probably already have those being a Python interpreter and an IDE:
##
##   -- A HID recognizable Keyboard/emulator, preferably one which can send and recieve RS-232. These can be found easily online, but so far I've only found retailers overseas.
##   -- A USB to TTL cable to talk to the emulator. These are more easily found here.
##   -- A module called PySerial which can be had from PyPi.org via pip
##
##   I've considered expanding it to include user input (hints) and possibly some randomization with the hopes of making it faster.
##   That's why it's there on Github.
##  
##   I'm sure you realize that most modern hardware has some kind of lockout enabled after mutltiple failed attempts. For some instances this will still work fine,
##   mostly for older hardware and of course some of the relics are more than accessible. If the password is simple and if it is indeed a 
##   firmware lock you're trying to bypass or a boot-up lock. Against an OS, I imagine you'll only have success with the most ancient of systems.
##
##   And, if you haven't realized, hints or some idea of what the password is, is actually neccessary for this to work. This is why future versions will
##   queery for hints, in order to help the app guess the right combination. Therefore, this application wouldn't be of much use to the Black Hat market, but owners 
##   of the gear, and some repair personnel could gain some use from it. Some Black Hat's could possibly use this, but those are the truly embedded (practiced) ones.
##
##   Lastly, Brute-force makes an attempt for every possible combination of characters used in the suspected password. It takes more or less the same amount of code to write such, 
##   however more complex, but due to the speed of CMOS or BIOS in general, it would take infinitly longer to complete. For the most part they're fire and forget 
##   but they're also notoriously slow. This approach requires a little detective work before deploying, so, with a lttle info and a ton of luck results can 
##   possibly be gained faster. 
##
##   I think you can see the idea clearly now and what my hopes are for this app. I'll continue to develop it, and branch off to create something more user friendly. 
##   I haven't gotten into gui development yet but if I find a good source on the subject I'll gladly add that in.
##
#################################################################################################################################################################################
#


import time
#   although we really love Mac's they can be a little janky...need to slow down the transmissions to some degree.
import subprocess
#   this is to run a line of code which might aide the eu.
import serial
#   and this piece is the real magic behind the script.


WORD_1 = "Xbox"
WORD_2 = "xbox"
WORD_3 = "XBOX"
WORD_4 = "xBOX"
#
#   These were my favorite words for simple passwords like firmware passwords. As you can see, bruteforce is hard to do.
#   I don't use any of these with my devices anymore so don't feel suspect for reading this...
#   You can and should change the constants to your own word patterns or add more or less if needed.
#
WORD_5 = "App"
WORD_6 = "app"
WORD_7 = "APP"
WORD_8 = "aPP"
#
#
#


code = "pyserial-ports -v"
#   The little helper I mentioned earlier...

global counter
global attempts

counter = 0
attempts = 0

#   Counters,



def status(attempts):
    print("\n So far, you've made " + str(attempts) + " attempts to penetrate this machine...and counting.\n")
#   A bit of joke, since this will take a while, it's ok to get a little comfortable.


def FWCracker(counter, attempts):
    #   The attempts.
    n = 0
    while n <= 9999:                         ##############################################################
        #   Trying for Xbox...                                                                          #            This loop can be and is iterated for each suspected
        counter += 1    #   Titan                                                                       #            word pattern. As far as the part of the combo which
        WordPattrn = WORD_1                                                                             #            includes numbers, use 'the imagined largest factor 
        passcode = WordPattrn + str(n) + "\r"                                                     ###############    of those combined digits real number'~Boris
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))      ###########      So if you suspect the number is 4195, maybe, then count 
        do_writer_do(passcode, ser, clear)                                                              #            to 5000. If you think it's 332 then count to 400 or
        n += 1                                                                                          #            maybe 350, etc... This is why adding some radomization 
        #                                                                                               #            could speed things up. Once user input is added, we can
    n = 1                                                  ###############################################           replace these loops for ones which are more tailored
    int(counter)                                                                                        #            and can then condense some things.
    int(attempts)
    #   Oddly enough, the variables need to be converted back to integers every iteration. 
    #   I may be missing something but I thought a variable's type was determined by it's usage or how it's referenced, here in python.
    attempts += counter
    #   You have to keep a record outside of the loop to count precisely. This precept escaped me for many years.
    #   If you think about it, you can't add or take from a loop, something that's already cycling without stopping the cycle or waiting for it to end, right?
    status(attempts)
    counter = 0
    while n <= 9999:
        #   Trying for xbox
        WordPattrn = WORD_2
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for XBOX...
        WordPattrn = WORD_3
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        # Trying for xBOX...
        WordPattrn = WORD_4
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for App...
        WordPattrn = WORD_5
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for app...
        WordPattrn = WORD_6
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for APP...
        WordPattrn = WORD_7
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for aPP...
        WordPattrn = WORD_8
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)



def do_writer_do(passcode, ser, clear):
    #   The writer...
    print(ser.name + " " + str(passcode) + " " + str(clear))
    to_bytes = passcode.encode(encoding='ascii')
    #   Your emulator will most likely convert 'ascii' to the corresponding keycodes.
    ser.write(to_bytes)
    print("\n")
    time.sleep(3)


subprocess.run(code)
#   This is as dangerous as it's known to be, however this tool is meant for offline use.
#   Plus, in this scenario there's no advanced system or OS present, only the BIOS and CMOS are encountered.
#   Not sure how one would exploit it from this vantage point, or why, or if one could possibly profit.


hid_port = input("Enter your emulator's serial port: ")
ser = serial.Serial(hid_port)
clear = ser.is_open
print("Your emulator's serial port is " + hid_port + " " + str(clear))
time.sleep(1)
#   User input, it's good when you can get it.

ser.baudrate = 9600
# PySerial as well, neccesary protocols for this app and your device.

FWCracker(counter, attempts)

