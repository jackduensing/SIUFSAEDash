# SIUFSAEDash

Files/docs pertaining to the 2026 Saluki Formula Racing FSAE Dashboard system with RF LoRa telemetry by Jack Duensing

Note: As of May 2026 the LoRa is not implemented, steps taken to implement will be included but have not been tested.

## Abstract

The goal of this group is to create a system that takes in CANBUS data from the vehicle and displays the most relevant information to the driver. 
The onboard display is easily readable to persons outside of the project. This information is very valuable for testing of the car and understanding its status. 
Validation is a large part of the Formula SAE competition; this system provides an easy way to understand the status of the car and aids in troubleshooting.
A second page of the GUI enabled through the touchscreen dispay allows for instantaneous readouts of all dashboard collected data in one place for a "one stop shop" for the car's status 
Thorough documentation allows for ease of knowledge transfer to future members of the team. The new dashboard system allows for an enhanced, personalized, driving experience.

## Features

- Dashboard GUI
    - Simple, easy to read dispay makes understanding the car's status intuitive 
    - The RPM overrev warning turns a portion of the screen red for an easy cue to the driver that the car is nearing redline
    - The second page of the display shows all dash read data points for a more desciptive view
    - The second page is accessed with and up and down swipe to mitigate accidental swiping while driving
- CAN frame reading
    - CAN frame reading code is simple, compact, and stable
- Modular code design
    - Code was designed with modularity in mind
    - Allows easy addition of new fields read from the CANBUS into the system
    - GUI code written with QML provides stable and easily interpretable GUIs specifically designed for this usecase 

# Documentation

Below is the documentation/installation guide, it is specific to my setup, but is widely applicable.

Please feel free to build off of this system, and I encourage customization

## Grocery List

- Testing computer
    - All development was done on Kubuntu 24.04
- Raspberry Pi 4B 2GB RAM
    - Most likely overkill for this application, however future proofing and screen compatibility was desired
- Micro SD card for Pi storage
- CAN Module
    - I am using the MCP2515_CAN, very standard module
- LoRa USB Reciever
- LoRa Transmitter
- SMA Antenna Adapter
- Antenna correctly tuned for the band of LoRa using
    - Check your region's frequency band for this, mine is in the 915MHz
- Raspberry Pi Touch Display 2 (5" Portrait)
    - Could also use the 7" variant
- Dupont Connectors for prototyping
- Some permanent connection solution, many options exist for this
- Male USB to CAN Adapter
    - Used for sending test frames to the dash
- a USB drive for logging
    - size is not an issue, with the data being held in a CSV, 32Gb holds about 700 million rows of logging

## Installation

As of May 2026 the LoRa is not implemented, steps taken to implement will be included but have not been tested.

### Pi Side Hardware
We must install the CAN Module, the LoRa Module, and the Screen. Here is the pinout:

                                Raspberry Pi 4B
          LoRa Module VIN[] []3v3 Power   5V Power[] []Screen 5V
                            []GPIO2       5V Power[] []CAN Module VCC
                            []GPIO3            GND[] []Screen GND
                            []GPIO4         GPIO14[]
          LoRa Module GND[] []GND           GPIO15[]
                            []SPI1 CE1    SPI1 CE0[] []LoRa Module CS
                            []GPIO27           GND[] []CAN Module GND
                            []GPIO22        GPIO23[]
                            []3v3 Power     GPIO24[]
            CAN Module SI[] []SPI0 MOSI        GND[]
            CAN Module SO[] []SPI0 MISO     GPIO25[] []LoRa Module RST
           CAN Module SCK[] []SPI0 SCLK   SPI0 CE0[] []CAN Module CS
                            []GND         SPI0 CE1[]
                            []GPIO0         GPI0 1[]
           LoRa Module G0[] []GPIO5            GND[]
                            []GPIO6           PWM0[] []CAN Module INT
                            []PWM1             GND[]
           LoRa Module SO[] []SPI1 MISO   SPI1 CE2[]
                            []GPIO26     SPI1 MOSI[] []LoRa Module SI
                            []GND        SPI1 SCLK[] []LoRa Module SCK

        Screen Display In[] []Display out

CAN module set up
- Be sure to jump the 120 ohm terminating resistor
- From the car be sure to connect the CAN High and CAN Low along with a shared ground between the ECU and the CAN Module

### Test Computer Side Hardware/Config

When plugging in the USB to CAN, we must assure that it is configured correctly. Most will be automatically configured correctly but to check use usb-devices or lsusb -t. You're looking for something something gs_usb, this indicates it is set up with candlelight as can0. Example outputs shown below. For other issues canable.io may be able to help, chances are your USB to CAN adapter is very similar.

from usb-devices

```
    T:  Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#=  4 Spd=12   MxCh= 0
    D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
    P:  Vendor=1d50 ProdID=606f Rev=00.00
    S:  Manufacturer=canable.io
    S:  Product=canable gs_usb
    S:  SerialNumber=004F002D4E56511520363434
    C:  #Ifs= 2 Cfg#= 1 Atr=80 MxPwr=150mA
    I:  If#= 0 Alt= 0 #EPs= 2 Cls=ff(vend.) Sub=ff Prot=ff Driver=gs_usb
    E:  Ad=02(O) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    E:  Ad=81(I) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    I:  If#= 1 Alt= 0 #EPs= 0 Cls=fe(app. ) Sub=01 Prot=01 Driver=(none)
```

from lsusb -t

` |__ Port 001: Dev 004, If 0, Class=Vendor Specific Class, Driver= gs_usb, 12M `

Now we activate the can0 with

`sudo ip link set can0 up type can bitrate 500000`

this sets up can0 and sets the bitrate as 5Mb/s, this is the commonplace bit rate for standard CAN applications, note this will always default to off after reboot and is required to send or receive CAN packets

verify the bus is up with 

`ip -details link show can0`

### Pi Side Hardware Config

Multiple edits need to be made in the case of the actual hardware of the Pi. This is most easily done over SSH, but to start we need an OS. 

Install Raspberry Pi OS Lite 64bit, when setting up be sure to enable SSH, but this can be enabled after the fact. This OS will load with the UK Keyboard layout, this is simple to change in the locale settings.

Of course do not forget to update the system packages before and after, some dependencies may be missing or unable to be resolved with older system packages

Nextly, in the /boot/firmware/config.txt we must make many changes

- Uncomment the line `dtparam=spi=on` to enable SPI
- Add these lines under the uncommented line
    - `dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=12` for the CAN, specific to my install, oscillator frequency and interrupt pin may vary
    - `dtoverlay=spi-bcm2835` for the CAN
    - `dtoverlay=spi1-1cs` for the LoRa
- Add these lines in the `[all]` section
    - `dtoverlay=vc4-kms-v3d` for eglfs/the screen
    - `dtoverlay=vc4-kms-dsi-ili9881-5inch,swapxy,rotation=90` specifically for the 5" Raspberry Pi touch screen

Next enable SPI in the raspi-config menu with
- `sudo raspi-config` -> interfacting options -> SPI

Next in /boot/firmware/cmdline.txt, assuring everything stays in the same line, add:
- `logo.nologo loglevel=3 quiet vt.global_cursor_default=0` this disables the splash and suppresses the tty output on start up and also hides the cursor on the GUI

Next there are some system packages and config stuff to install

Run these lines in the terminal
- `sudo usermod -aG video,input,render $USER` adds the user to the necessary groups to enable eglfs usage
- `sudo apt install can-utils` installs the can-utilities needed for CAN testing
- `sudo apt install python3-dev` installs python3
- next we will need to install the pyqt6 dependencies for QML, the pip version is too generic for this hardware so the packages must be system wide
    - `sudo apt install python3-pyqt6 python3-pyqt6.qtqml python3-pyqt6.qtquick python3-pyqt6.sip qt6-qpa-plugins qml6-module-qtquick qml6-module-qtquick-controls qml6-module-qtquick-layouts qml6-module-qtquick-window qml6-module-qtquick-templates`

Next to mount the USB drive for logging

- plug in the USB drive and use `sudo blkid` to find the UUID and file system type
- create a directory in /mnt/ that the drive will always mount to, I named mine "usb", that is reflected below
- backup your fstab file with `sudo cp /etc/fstab /etc/fstab.bak`
- now make the following change adding the line below to the fstab file located at /etc/fstab
    - `UUID=YOURUUID /mnt/usb YOURFILESYSTEMTYPE nofail,noatime 0 0`

Reboot the pi to apply changes

That should be everything for the hardware config of the Pi itself, now onto software

### Software installation

Navigate to where you want the code to live, mine is just in the home directory, this will be reflected in my setup

Clone the repo, navigate into it


For setting up the virtual environment
- Create the venv with this flag to allow the virtual environment to see those pyqt6 packages
    - `python3 -m venv --system-site-packages .venv`
        - note that .venv is the virtual environment name, I just prefer it as a hidden directory with that name
- Activate the venv with
    - `source .venv/bin/activate`
- VERY IMPORTANT
    - Open requirements.txt with your tui text editor of choice and remove the lines
        - `PyQt6==6.11.0, PyQt6-Qt6==6.11.0, and PyQt6_sip==13.11.1`
    - These are the "too generic" pyqt6 dependencies that will cause issues with this hardware
    - However they are useful if you are attempting to modify the GUI on your main development computer, you will need them on there along with none of the system packages

Now that the virtual enviroment is set up the code is technically ready to run, run the code with eglfs using `QT_QPA_PLATFORM=eglfs python3 main.py`, if wanting to send data do not forget to enable the can0 interface as we did on the development machine 
- Other systems may be used such as an x11 server or running directly on the frame buffer but eglfs is the perfect middle ground of lightness that also utilizes hardware acceleration


For setting up the automatic at launch services:
- Note: the user of my Pi is sfr, change sfr wherever it sits with your Pi's user

First we create a script to start and load the software
- Place the script below in /usr/bin and name it startScript.sh
- Don't forget to set the script as executable after creation with
    - `sudo chmod +x startScript.sh`

```
#!/bin/bash

sudo ip link set can0 up type can bitrate 500000

cd /home/sfr/SIUFSAEDash

source .venv/bin/activate

QT_QPA_PLATFORM=eglfs python3 main.py
```

Assure this works and boots the program before moving on

Now we create the systemd service with
- `sudo nano /etc/systemd/system/dash.service`

```
[Unit]
Description=Starts FSAE Dash

[Service]
Type=simple
ExecStart=/bin/bash -c /usr/bin/startScript.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Then reload the service list with
- `sudo systemctl daemon-reload`

And enable the service with
- `sudo systemctl enable dash.service`

Now we create the splash service, I am using a simple ASCII art service, but there are methods to displaying pngs and even videos on startup

This simply uses cat on a txt file, replace `/home/sfr/splash.txt` with whatever you are using, I used an ASCII art maker [here](https://www.asciiart.eu/image-to-ascii), copy and paste this into your own splash.txt file 

Create another systemd service with
- `sudo nano /etc/systemd/system/splash.service`

```
[Unit]
Description=Splash Screen
DefaultDependencies=no
After=local-fs.target

[Service]
Type=oneshot
StandardOutput=tty
ExecStart=/bin/cat /home/sfr/splash.txt

[Install]
WantedBy=sysinit.target
```
Dont forget to reload the service list with
- `sudo systemctl daemon-reload`

And enable the service with
- `sudo systemctl enable dash.service`

Now on reboot you should have a fully functional system

### Troubleshooting

For system services issues you can view the logs with
- `sudo journalctl -u servicename.service`

For issues with the python itself, the code is set up to write all logs to the mounted USB, be sure to have that configured to read those logs

Any error message displaying something like "device or resource busy" is most likely the problem of enabling can0 twice, this has no bearing on the system, just a system notice.

There is a known issue with possible file corruption upon loss of power to the Pi. This is mitigated by turning on the overlay file system in `sudo raspi-config` -> Performance options -> Overlay File System (overlay for both)
- This enables, in essence, a read only file system
- All system writes are redirected to RAM, which is purged on loss of power
- This must be turned off before pulling from the repo or updating any files on the disc of the Pi

## Usage

After setting up of all the services, usage is basically turn on the power

However there are some useful notes
- The check for the logging drive occurs before start up of the GUI
    - Make sure it is plugged in before power on
- A second page exists to see all dash collected data in one place in real time as instantaneous values
    - Swiping UP and DOWN on the screen changes between these pages
    - This is a safety feature intended to mitigate the chance of swiping to the non critical page while driving 

Sending test frames to the system using the USB to CAN adapter that we set up before
- test.py within the repo is a dev program used to generate the bash command to send a frame
- It is most likely in a random state of generating an entire bash script used for testing

General workflow of test.py is as follows
- load the database file
- get a message object with the specific name of the data you want to send
    - best done by simply combing over the database file
- using the encode method of the message object, add data
    - all fields must be filled with some value for a valid frame
- create a message with the object and the data
- print the message and copy to the command line
- Note: there is most certainly a way to get this to run in the terminal directly, but my system was being finicky and I don't mind a good copy paste every once in a while

The included .dbc file (database file) is for the ECU the team is running currently
- MS3 Pro Evo+ HC

##