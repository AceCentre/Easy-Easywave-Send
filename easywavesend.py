"""Easywave Easy Send

Usage:
  easywavesend.py 
  easywavesend.py [--tcode=<tc>] [--keycode=<kc>]
  easywavesend.py (-h | --help)
  easywavesend.py --version

Options:
  -h --help      Show this screen.
  --version      Show version.
  --tcode=<tc>   Transmission code [default: 01].
  --keycode=<kc> Keycode

"""

import serial
from serial.tools import list_ports
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='EasyWaveEasySend 1.0')
usb_port = list(list_ports.grep("Easywave"))[0]
port = usb_port.device
ser = serial.Serial(port, 57600)
ser.write(b'TXP,01,A')
ser.close()
