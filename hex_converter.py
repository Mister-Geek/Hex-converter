#-------------------------------------------------------------------------------
# Name:        hex encoder, and decoder
# Purpose:     A small tool created to assisit in <<SQL INJECTION>>
#              And of course, for us to learn together.
# Notice:      Coded in python 2.7
# Author:      <4sec>, <PTT>
# Created:     23/05/2013
# Copyright:   (c) <4sec> <PTT> 2013
# Licence:     <Opensource GNU>
# Version:     v1.2
# What's new:  Added a new function to find your ip address
# Love To:     MHU NullByte,Xero MHU,Master Leet,Little MHU,Tayalma MHU,
#              3zero MHU,Dongoth, and all Python Think Tank members
#-------------------------------------------------------------------------------

import os
import sys
from time import sleep
import urllib2
from os import sep

def whatismyip():
    ip = urllib2.urlopen('http://whatismyip.akamai.com/', timeout=10).read()
    print'Your ip address is ',ip
    print'\n\n'
    sleep(3)
    choice()

def clear_screen():
    if sys.platform == 'win32' or sys.platform == 'win':
        os.system('cls')
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        os.system('clear')

def banner():
    print('\n\n\n\n\n\n')
    print'''
    +=======================================================================+
    Name         : hex encoder and decoder!
    Developed by : 4sec team, Python think tank online
    Released by  : Python think tank online!
    Release Date : 23/5/2013
    Version      : v1.2
    Next Version : Have plan to implement tools useful in <<SQL Injection>>
    What's new   : Added a new feature to find your IP address.
    +=======================================================================+

    '''


def bye():
    clear_screen()
    print'''
    Good Bye!

    Product by Python Think Tank Online.
    +=================================================+
      http://www.facebook.com/groups/361983457247340/
    +=================================================+
    Feel Free to join our group, if you want to learn python with us!
    '''
    sleep(2)
    sys.exit()

def hex_convert(x,y):
    if y == 'e':
        enc_hex = '0x' + x.encode('hex')
        print'\n+==============================================================================+'
        print'Plaintext : ',x
        print'+==============================================================================+'
        print'Hex Value : ', enc_hex
        print'+==============================================================================+'
        sleep(3)
        print'\n\n\n'
        choice()
    elif y == 'd':
        if x[0] == '0' and x[1] == 'x':
            plain_hex = x.replace('0x','') # This is the part making error in version 1.
            # With a small trick.. No error anymore.!!
            dec_hex = plain_hex.decode('hex')
        else:
            dec_hex = x.decode('hex')
        print'\n+==============================================================================+'
        print'Hex Value : ',x
        print'+==============================================================================+'
        print'Plaintext : ', dec_hex
        print'+==============================================================================+'
        sleep(3)
        print'\n\n\n'
        choice()


def choice():
    print"\t  1. String to Hex"
    print"\t  2. Hex to string"
    print"\t  3. Find my IP "
    print"\n\n\n\t  0. exit"

    usr_input = input('\n # : ')
    if usr_input == 1:
       clear_screen()
       print'\n\nEnter string '
       string = raw_input(" : ")
       hex_convert(string,'e')
    elif usr_input == 2:
         clear_screen()
         #=====================================================
         #  You can also input hex with '0x' infront of it.
         #=====================================================
         print'\nEnter hex '
         hex = raw_input(" : ")
         hex_convert(hex,'d')
    elif usr_input == 3:
        whatismyip()
    elif usr_input == 0:
         bye()
    else:
        print'Invalid choice!'
        main()

def main():
    banner()
    choice()

main()



