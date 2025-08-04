#!/usr/bin/python3
# File name   : setup.py
# Author      : Adeept

import os
import time

curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

def replace_num(file,initial,new_num):  
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)

os.system("sudo apt-get update")
os.system("sudo apt-get -y upgrade")

os.system("sudo apt-get purge -y wolfram-engine")
os.system("sudo apt-get purge -y libreoffice*")
os.system("sudo apt-get -y clean")
os.system("sudo apt-get -y autoremove")

os.system("sudo pip3 install -U pip")

os.system("sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential")

os.system("sudo apt-get install -y swig")

os.system("sudo apt-get install -y flac")

os.system("sudo apt-get install -y bison libasound2-dev swig")

os.system("sudo -H pip3 install --upgrade luma.oled")

os.system("sudo apt-get install -y i2c-tools")

os.system("sudo apt-get install -y python3-opencv")

os.system("sudo pip3 install adafruit-pca9685")

os.system("sudo pip3 install rpi_ws281x")

os.system("sudo apt-get install -y python3-smbus")

os.system("sudo pip3 install mpu6050-raspberrypi")

os.system("sudo pip3 install flask")

os.system("sudo pip3 install flask_cors")

os.system("sudo pip3 install websockets")

try:
	replace_num("/boot/config.txt",'#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
except:
	print('try again')


os.system("sudo pip3 install numpy")


os.system("sudo apt-get -y install libqtgui4 libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqt4-test")

os.system("sudo pip3 install imutils zmq pybase64 psutil")

# os.system("sudo git clone https://github.com/oblique/create_ap")

# try:
# 	os.system("cd " + thisPath + "/create_ap && sudo make install")
# except:
# 	pass

# try:
# 	os.system("cd //home/pi/create_ap && sudo make install")
# except:
# 	pass

os.system("sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq")

try:
	os.system('sudo touch //home/pi/startup.sh')
	with open("//home/pi/startup.sh",'w') as file_to_write:
		#you can choose how to control the robot
		file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/webServer.py")
# 		file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/server.py")
except:
	pass

os.system('sudo chmod 777 //home/pi/startup.sh')

replace_num('/etc/rc.local','fi','fi\n//home/pi/startup.sh start')

try: #fix conflict with onboard Raspberry Pi audio
	os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
	with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
		file_to_write.write("blacklist snd_bcm2835")
except:
	pass

print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("sudo reboot")
