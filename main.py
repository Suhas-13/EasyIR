#Take flask input 
"""
EXAMPLE:

run lightsOn 1000 
wait 1000

"""
import os
from flask import Flask, request #import main Flask class and request object
import time
import sys 

app = Flask(__name__) #create the Flask app
@app.route('/endpoint')
def startRecording(name):
    #RUN START RECORDING CODE WITH NAME
    
    print("Started Recording")   

def stopRecording():
    #RUN STOP RECORDING CODE
    print("Stopped Recording") 
def runCode(code):
    codeList=code.split("\n")
    for i in codeList:
        if i.split(" ")[0].lower() == "run":
            #RUN CODE WITH NAME
            if i.split(" ")[1].lower() == "0":
                #RUN CODE ONCE

            else:
                futureTime=time.time()+int(i.split(" ")[2].lower())
                while futureTime > time.time():
                    #runcode with name 
            print("Code to run is " + i.split(" ")[1].lower())
        elif i.split(" ")[0].lower() == "wait":
            time.sleep(int(i.split(" ")[1].lower()))

        elif i.split(" ")[1].lower()=="repeat":
            count=0
            while count < int(i.split(" ")[2].lower()):
                for i in code.split("\n")[0:len(code.split("\n"))-1]:
                    if i.split(" ")[0].lower() == "run":
                            #RUN CODE WITH NAME
                        if i.split(" ")[1].lower() == "0":
                            #RUN CODE ONCE

                        else:
                            futureTime=time.time()+int(i.split(" ")[2].lower())
                            while futureTime > time.time():
                                #runcode with name 
                        print("Code to run is " + i.split(" ")[1].lower())
                    elif i.split(" ")[0].lower() == "wait":
                        time.sleep(int(i.split(" ")[1].lower()))

                count+=1

                    
                    
                
            
        

    if request.args.get("record") == "start":
        return("Starting...")
        startRecording(request.args.get("name"))
    elif request.args.get("record") == "stop":
        return("Stopping...")
        stopRecording()
    
    elif request.args.get("record")=="run":
        return("Running Code")
        runCode(requests.args.get("code"))
