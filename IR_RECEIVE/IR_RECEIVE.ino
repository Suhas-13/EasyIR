#include <IRLibRecvPCI.h> 
#include <IRremote.h> 
#include <LinkedList.h>
LinkedList<int> irSignal;

void(* resetFunc) (void) = 0;

int IncomingByte = 0;

IRrecvPCI myReceiver(2);
IRsend irsend;

void setup() {
  Serial.begin(9600);
  delay(2000); while (!Serial); 
  myReceiver.enableIRIn();
  pinMode(LED_BUILTIN, OUTPUT); 
}

void loop() {
  
  static char buffer[256];
  static size_t pos;              // position of next write
  while (Serial.available() && pos < sizeof buffer - 1) {
    // Read incoming byte.
    char c = Serial.read();
    buffer[pos++] = c;

    // Echo received message.
    if (c == '\n') {   
      irSignal.add(atoi(buffer)); // \n means "end of message"
      buffer[pos] = '\0'; // terminate the buffer
      //Serial.print(buffer);   // send echo
      delay(10);
      pos = 0;                // reset to start of buffer
     }
   }
   unsigned int i [irSignal.size()] = {};
   for (int n = 0; n < irSignal.size(); n++){
      i[n] = irSignal.get(n);
      }
   
   int khz = 38;
   irsend.sendRaw(i, 100, khz);
   if (atoi(buffer)==11111){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    irSignal.clear();
    resetFunc();  
   }
   
  
  if (Serial.available() < 1){
    if (myReceiver.getResults()) { 
      for(bufIndex_t i=1;i<recvGlobal.recvLength;i++) {
        Serial.print(recvGlobal.recvBuffer[i],DEC);
        Serial.print(F(", "));
      }
      Serial.println(F("1000"));//Add arbitrary trailing space
      myReceiver.enableIRIn();      //Restart receiver
    }
  }


  
}
