/*
    CODIGO PARA ARDUINO

*/
 
#define LED 13
 
int dato = 0; //variable para guardar el mensaje
  
void setup()
{
   pinMode(LED, OUTPUT); //establecemos el pin 13 como salida
   Serial.begin(9600); //inicializamos Serial
}
  
void loop()
{
   if (Serial.available() > 0)
   {
      dato= Serial.read(); //leemos el serial
  
      if(dato== 'e')
      {
         digitalWrite(13, HIGH); //si entra una 'e' encendemos el LED
      }
      else if(dato == 'a')
      {
         digitalWrite(13, LOW); //si entra una 'a' apagamos el LED
      }
   }
}
