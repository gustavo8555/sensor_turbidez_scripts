double calc_NTU(double volt);
double NTU = 0.0;

int frequency = 1000; // frequencia em milisegundos
int turbiditySensor = A0;

int sensorValue;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(turbiditySensor);
  float voltage = sensorValue * (5.0 / 1024.0);

  NTU = calc_NTU(voltage);
  
  Serial.println(NTU);
  
  delay(frequency);
}

double calc_NTU(double volt){
  double NTU_val;
  // Função do segundo grau para cálculo do NTU
  NTU_val = -(1120.4*volt*volt)+(5742.3*volt) - 4352.9;

  return NTU_val;
}