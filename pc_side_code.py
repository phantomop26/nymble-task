import serial
import time

BAUD_RATE = 2400
TEXT_TO_SEND = """
Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.

In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.
"""

def main():

    ser = serial.Serial('COM5', BAUD_RATE, timeout=1) 
    lastReceptionTime = time.time() 
   
    for char in TEXT_TO_SEND:
        ser.write(char.encode())  
    while True:
        data = ser.readline()
        if data:
            print(data.decode().strip()) 
            currentTime = time.time()
            if lastReceptionTime != currentTime:
                speed = len(data) * 8 / (currentTime - lastReceptionTime)  # Calculate speed in bits/second
                print("Receive speed:", speed, "bits/second")
            lastReceptionTime = currentTime

if __name__ == "__main__":
    main()