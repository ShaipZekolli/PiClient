#!/usr/bin/python3

import os
import glob
import time
#import Adafruit_DHT
import urllib.request
from urllib.request import urlopen
from datetime import datetime
import socket
import re
import grovepi
import math

# DECLARATIONS
sensor = 8
now = datetime.now()                            # Get time right now
timestamp = now.strftime("%Y-%m-%d-%H:%M:%S")   # Format the timestamp
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.
i = 1
while i < 4:
# adding 1 seconds time delay
    time.sleep(1)
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type $
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
            i += 1
    except IOError:
        print ("Error")

# Function to read raw temperature from the DS18b20
# It opens the device_file (/w1_slave), and reads the content, then close the file
def read_temp_raw():
# adding 2 seconds time delay
    time.sleep(2)
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type $
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
            global t
            t = temp
            global h
            h = humidity
    except IOError:
        print ("Error")
# Function to get the local hostname
# It is used for identify the "senor" in the mySQL database
def get_host_name():
    global local_hostname
    local_hostname = socket.gethostname()

# Function that get the external IP-adress
def get_external_ip_address():
    global external_ip
    url = "http://checkip.dyndns.org"           # This site return one line of text.
    my_request = urlopen(url).read()            # Read the URL
    res = re.findall(b'\d{1,3}', my_request)    # Search and findall integers in my_request
    my_ip_list = list(map(int, res))            # Clean up the list
    my_ip = str(my_ip_list)[1:-1]               # Remove the square brackets
    temp_ip = my_ip.replace(",", ".")           # Replace comma with periods
    external_ip = temp_ip.replace(" ", "")      # Replace <space> with none-space
    print ("External IP: " +external_ip)        # Print the External IP address as xxx.xxx.xxx.xxx

# Function that actualle sends data and adds it to the database
def send_data():
    print (timestamp)                           # For debug purpose
    print (t)                             # For debug purpose
    print (h)                            # For debug purpose
    print (local_hostname)                      # For debug purpose
    output = "http://192.168.2.108/temperature/add_temp.php?temp="+str(t) \
    +"&humi="+str(h)+"&time="+str(timestamp)+"&sensor="+str(local_hostname)+"&ip=" \
    +str(external_ip)                           # string that is called by the urlopen
    print (output)                              # debug
    html = urlopen(output).read()               # executing url
    print (html)                                # debug

def main():
    read_temp_raw()
    #read_humidity()
    get_host_name()
    get_external_ip_address()
    send_data()
    
if __name__ == "__main__":
    main()

