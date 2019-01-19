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
  

def startRecording(name):
    #RUN START RECORDING CODE WITH NAME
    
    print("Started Recording " + name)   
    return("STARTED")
def stopRecording():
    #RUN STOP RECORDING CODE
    print("Stopped Recording") 
def runCode(code,request):
    codeList=code.split("\n")
    for i in codeList:
        if i.split(" ")[0] == "run":
            if i.split(" ")[2] == "0":
                #RUN ONCE 
                print(i.split(" ")[1].lower())

            else:
                futureTime=time.time()+int(i.split(" ")[2])
                while time.time() < futureTime:
                    #PRINT FOR AS LONG as it goes
                    print(i.split(" ")[1].lower())
        elif i.split(" ")[0] == "wait":
            time.sleep(int(i.split(" ")[1]))
        elif i.split(" ")[0] == "repeat":
            amtofrepeats=int(i.split(" ")[1])
            count=0
            codeList.pop()
            while count < amtofrepeats:
                
                for i in codeList:
                    if i.split(" ")[0] == "run":
                        if i.split(" ")[2] == "0":
                            #RUN ONCE 
                            print(i.split(" ")[1].lower())

                        else:
                            futureTime=time.time()+int(i.split(" ")[2])
                            while time.time() < futureTime:
                                #PRINT FOR AS LONG as it goes
                                print(i.split(" ")[1].lower())
                            print("done")
                    elif i.split(" ")[0] == "wait":
                        time.sleep(int(i.split(" ")[1]))
                count+=1
                    
                    
                
        
            
                

app = Flask(__name__) #create the Flask app
@app.route('/endpoint',methods = ['POST'])
def endpoint():
    
    
    print(str(request.form.get("name")))
    
    #print(request.get_json())
    
    if request.form.get("record") == "start":
        
        startRecording(request.form.get("name"))
        return("Starting...")
    elif request.form.get("record") == "stop":
        
        stopRecording()
        return("Stopping...")
    
    elif request.form.get("record")=="run":
        
        runCode(request.form.get("code"),request)
        return("Running Code...")
  
                    

    
    
                
            
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
