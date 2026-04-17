# SIUFSAEDash
Files/docs pertaining to the 2026 SIU FSAE Dashboard system with RF LoRa telemetry 

## Grocery List

- Testing computer
    - All development was done on Kubuntu 24.04
- Raspberry Pi 4B 2GB RAM
    - Most likely overkill for this application, however future proofing and screen compatibility was desired
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

sudo ip link set can0 up type can bitrate 500000

this sets up can0 and sets the bitrate as 5Mb/s, this is the commonplace bit rate for standard CAN applications

verify the bus is up with 

ip -details link show can0

### Pi Side Hardware Config

Multiple edits need to be made in the case of the actual hardware of the Pi. This is most easily done over SSH, but to start we need an OS. 

Install Raspberry Pi OS Lite 64bit, when setting up be sure to enable SSH, but this can be enabled after the fact. THis OS will load with the UK Keyboard layout, this is simple to change in the locale settings.
Nextly, in the /boot/firmware/config.txt we must make many changes

Of course do not forget to update the system packages before and after, some dependencies may be missing or unable to be resolved with older system packages

- Uncomment the line `dtparam=spi=on` to enable SPI
- add these lines under the uncommented line
    - `dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=12` for the CAN, specific to my install, oscillator frequency and interrupt pin may vary
    - `dtoverlay=spi-bcm2835` for the CAN
    - `dtoverlay=spi1-1cs` for the LoRa
- add these lines in the all section
    - `dtoverlay=vc4-kms-v3d` for elgfs/the screen
    - `dtoverlay=vc4-kms-dsi-ili9881-5inch,swapxy,rotation=90` specifically for the 5" Raspberry Pi touch screen

Next in /boot/firmware/cmdline.txt, assuring everything stays in the same line add:
- `logo.nologo loglevel=3 quiet vt.global_cursor_default=0` this disables the splash and suppresses the tty output on start up and also hides the cursor on the GUI

Next there are some system packages and config stuff to install
run these lines in the terminal
- `sudo usermod -aG video,input,render $USER` adds the user to the necessary groups to enable elgfs usage
- `sudo apt install can-utils` installs the can-utilities needed for CAN testing
- `sudo apt install python3-dev` installs python3
- next we will need to install the pyqt6 dependencies for QML, the python pip version is too generic for this hardware so the packages must be system wide
    - `sudo apt install python3-pyqt6 python3-pyqt6.qtqml python3-pyqt6.qtquick python3-pyqt6.sip qt6-qpa-plugins qml6-module-qtquick qml6-module-qtquick-controls qml6-module-qtquick-layouts qml6-module-qtquick-window qml6-module-qtquick-templates`

That should be everything for the hardware config of the Pi itself, now onto software

### Software installation

Navigate to where you want the code to live, mine is just in the home directory, this will reflect in my setup

clone the repo, navigate into it


for setting up the virtual environment
- create the venv with this to allow the virtual environment to see those pyqt6 packages
    - `python3 -m venv --system-site-packages .venv`
        - note that .venv is the virtual environment name, I just prefer it as a hidden directory with that name
- activate the venv with
    - `source .venv/bin/activate`
- VERY IMPORTANT
    - open requirements.txt with your tui text editor of choice and remove the lines
        - `PyQt6==6.11.0, PyQt6-Qt6==6.11.0, and PyQt6_sip==13.11.1`
    - these are the "too generic" pyqt6 dependencies that will cause issues with this hardware
    - however they are useful if you are attempting to modify the GUI on your main development computer, you will need them on there along with none of the system packages

now that the virtual enviroment is set up the code is technically ready to run, run the code with eglfs using `QT_QPA_PLATFORM=eglfs python3 main.py`
- other systems may be used such as an x11 server or running directly on the frame buffer but eglfs is the perfect middle ground of lightness that also utilizes hardware acceleration


for setting up the automatic services:



## Usage

##