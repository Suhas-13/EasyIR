import serial
import time
ser = serial.Serial('/dev/cu.usbmodem143401', 9600)
ans = input("DATA_NAME: ")
data = open(ans+".txt", "a+")
print("Hold the button letter 'A' appears. When the program ends, release the button.")
time.sleep(2)
print("A")
start = time.time()
while True:
	print (ser.readline())
	data.write(str(ser.readline()))
	data.write("\n")
	if start+10 < time.time():
		break
print("DONE")

data.close()

with open(ans+'.txt', 'r') as dat, open(ans+'_IR.txt','w') as format:
        for line in dat:
                line = line[:-6]
                line = line.replace("b'","")
                format.write(line)
                format.write("\n")
