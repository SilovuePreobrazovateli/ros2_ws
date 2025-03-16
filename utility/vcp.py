import serial

sp1 = serial.Serial('/dev/ttyACM0', 12000000, timeout=0)
sp2 = serial.Serial('/dev/ttyACM1', 12000000, timeout=0)

while True:
    msg = sp1.read()
    if msg:
        sp2.write(msg)
        print(msg)
