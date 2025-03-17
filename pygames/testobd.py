import serial

# Configura a conexão serial com o ELM327
try:
    elm327 = serial.Serial('/dev/rfcomm0', baudrate=115200, timeout=1)
    print("Conectado ao ELM327!")
    
    # Envia um comando OBD-II para testar (Ex: "ATI" para identificar o dispositivo)
    elm327.write(b'ATI\r')
    
    # Lê a resposta
    response = elm327.readlines()
    for line in response:
        print(line.decode().strip())
        
    elm327.close()
except Exception as e:
    print(f"Erro ao conectar ao ELM327: {e}")

