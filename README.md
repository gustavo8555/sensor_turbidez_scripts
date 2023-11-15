# Sensor de turbidez com Arduino

Repositório contendo scripts e módulos para coletar e representar em um gráfico o NTU ao longo do tempo.

## Arquitetura de componentes
![image](https://github.com/gustavo8555/sensor_turbidez_scripts/assets/4447306/4bee0f93-0ae0-4e0e-9574-57541d153372)

*O endereço ip utilizado acima pode variar de acordo com a sua rede*

## Instalação

### Raspberry Pi e Arduino
#### Pré-requisitos 
- Uma conexão SSH (também é possível executar os comandos diretamente no raspberry-Pi)
- Ubuntu 20.04 LTS 
- Mosquitto server 
- Python 3.10
- Arduino configurado e conectado ao sensor
- Porta COM identificada 

#### Executando publisher

1. Clonar repositório

```bash
git clone git@github.com:gustavo8555/sensor_turbidez_scripts.git
```

2. Entre no diretório com o código do MQTT publisher desse projeto

```bash
cd sensor_turbidez_scripts/raspberry-sensor-pub/
```

Caso essa seja a primeira execução, o usuário deverá instalar as dependências do projeto com o comando a seguir. 

```bash
pip install -r ../requirements.txt
```

3. Execute o script principal (Caso você possua uma instalação extena de um broker MQTT modifique o parâmetro `localhost` para o seu endereço)

```bash
python3 main.py localhost
```

O script pode ser enviado ao background do bash com o comando abaixo:

```bash
nohup python3 main.py localhost &
```

Dessa forma o script permanecerá em execução mesmo que você se deslogue do servidor

### Executando o Client

Agora no computador que receberá os dados podemos executar o MQTT subscriber

1. Entre na pasta Client 

```bash
cd sensor_turbidez_scripts/client/
```

2. Instale as dependências localmente

```bash
pip install -r ../requirements.txt
```

3. Execute o script

```bash
python3 main.py 
```
