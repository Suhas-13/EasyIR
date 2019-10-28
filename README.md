# EasyIR

EasyIR by Suhas Hariharan and Shourjo Chakravathy.

https://insertcustomname.github.io/EasyIR/ (Demo website, in order to use, you need to install and setup the flask server, host the HTML with updated endpoints and setup the arduino circuits.)

Controlling IR Appliances just got easier. 

Note: I will be uploading the schematic for the arduino circuit at a later time.

EasyIR allows individuals to take control of their IR controllable devices in new ways, with a programmable environment developed by us.

# How to use Easy IR

First record the IR Codes for the device you wish to use.
You can do this by pressing the "Start Recording" button found on our webpage, specify a name of your choice and then pointing the device's remote at the arduino board and repeatedly pressing the button for a period of ~12-15 seconds.

## Next once you have the file saved you will need to program and run Easy IR 

To do this you will need to use our "programming interface", the interface accepts several different commands to help make your life easier.

You broadcast the IR code itself with "run" followed by the filename you specified earlier, followed by a number, if this number is 0 the code's will be broadcasted once, if it is any more than 0 it will be broadcasted for however long is specified in seconds.

There are also some other useful features such as "wait" which allows the program to wait for x amount of seconds and can be specified as such "wait 5".

Finally there is the repeat command which repeats all above code x amount of times. This is run as "repeat 5".

All lines of code MUST be run on different individual lines where the command(run, repeat, wait) is the first word and is lowercase.

Code will look something like this:

wait 3                                                                                                                  
run lightsOn 3                                                    
repeat 3                                                                 

After you have written your program you can run it with the "Run Code" button. 

When the code is done running it will popup to alert you. 

### Thank you for reading this guide and we hope you found it useful.
