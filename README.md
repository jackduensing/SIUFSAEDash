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

T:  Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#=  4 Spd=12   MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=1d50 ProdID=606f Rev=00.00
S:  Manufacturer=canable.io
S:  Product= ==canable gs_usb==
S:  SerialNumber=004F002D4E56511520363434
C:  #Ifs= 2 Cfg#= 1 Atr=80 MxPwr=150mA
I:  If#= 0 Alt= 0 #EPs= 2 Cls=ff(vend.) Sub=ff Prot=ff Driver=gs_usb
E:  Ad=02(O) Atr=02(Bulk) MxPS=  32 Ivl=0ms
E:  Ad=81(I) Atr=02(Bulk) MxPS=  32 Ivl=0ms
I:  If#= 1 Alt= 0 #EPs= 0 Cls=fe(app. ) Sub=01 Prot=01 Driver=(none)

from lsusb -t

|__ Port 001: Dev 004, If 0, Class=Vendor Specific Class, Driver= ==gs_usb==, 12M

Now we activate the can0 with

sudo ip link set can0 up type can bitrate 500000

this sets up can0 and sets the bitrate as 5Mb/s, this is the commonplace bit rate for standard CAN applications

verify the bus is up with 

ip -details link show can0

### Pi Side Hardware Config


## Usage

##