"""
This is a script for automatically registering keys on the Bittensor network when the price is under the limit you set.
This script is provided as is, and has no guarantee.
It mostly works in my test, but some errors are unhandeled and in that case it will skip to the next hotkey.

NEVER EVER share coldkey mnemonics with anyone or put it in any script. And always be extremely careful with how you use your keys. Please check this script to make sure it hasn't been tampered with.

Usage:
1. Check the script to control it has not been tampered with, and you know it is safe.
2. Fill in wallet name, hotkey names, and the max cost and password for your coldkey.
3. Paste all the code into a file called re_keys.py
4. Start the program by running: python3 reg_keys.py
"""


wallet = "name_of_your_coldkey"
hotkeys = ["1","2","3"] #a list with the names of all the hotkeys you want to register
highest_cost = 2.0 #The maximal amount of Tao you are willing to burn to register
password = "" #Password for your cold key

import pexpect
import re
import sys
import time
import traceback
from datetime import datetime

iterate=False
while True:
    for hotkey in hotkeys:
        while True:
            try:
                iterate=False
                command = 'btcli recycle_register -subtensor.network finney --netuid 1 --wallet.name {} --wallet.hotkey {}'.format(wallet,hotkey)
                # Get the current time
                current_time = datetime.now().time()
                
                # Format the time as HH:MM:SS
                formatted_time = current_time.strftime("%H:%M:%S")
                
                # Print the formatted time
                print("\nColdkey:",wallet,"Hotkey:", hotkey, flush=True)
                print(formatted_time,flush=True)

                child = pexpect.spawn(command)
                
                child.logfile_read = sys.stdout.buffer
                
                child.expect('Enter subtensor network')
                print("\nSending: <enter>", flush=True)
                child.sendline('')
                
                child.expect(r'The cost to register by recycle is (.*?)(?:\n|$)')
                cost_str = child.match.group(1).decode('utf-8').replace('τ', '')
                clean_cost_str = re.sub(r'\x1b\[[0-9;]*m', '', cost_str).strip()
                cost = float(clean_cost_str)
                
                if cost > highest_cost:
                    print("Not buying: n", flush=True)
                    child.sendline('n')
                    continue
                else:
                    print("Sending1: y", flush=True)
                    child.sendline('y')
                
                child.expect('Enter password to unlock key')
                print("\nSending: password")
                child.sendline(password)
                print("\nPassword sent")
                try:
                    child.expect(r'Recycle (.*?) to register on subnet')
                except:
                    break
                recycle_cost_str = child.match.group(1).decode('utf-8').replace('τ', '')
                clean_recycle_cost_str = re.sub(r'\x1b\[[0-9;]*m', '', recycle_cost_str).strip()
                recycle_cost = float(clean_recycle_cost_str)
                print("Recycle cost:", recycle_cost)
                
                if recycle_cost > highest_cost:
                    print("Sending: n", flush=True)
                    child.sendline('n')
                else:
                    print("Sending2: y", flush=True)
                    child.sendline('y')
                    
                    child.expect(r'Registered',timeout=120)
                    break
            except Exception as e:
                print("An error occured", e)
                print(traceback.format_exc())
                child.sendintr()  # Send Ctrl+C
                child.expect(pexpect.EOF)  # Wait for the command to exit
                if iterate:
                    break
                else:
                    continue
