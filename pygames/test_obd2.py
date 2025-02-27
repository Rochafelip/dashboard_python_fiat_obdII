import obd

# Tenta conectar no primeiro dispositivo disponível
connection = obd.OBD()

if connection.is_connected():
    print("✅ Conectado ao OBD2 com sucesso!")
else:
    print("❌ Falha ao conectar ao OBD2.")

# Teste lendo o RPM do motor
cmd = obd.commands.RPM
response = connection.query(cmd)

if response.value is not None:
    print(f"RPM do motor: {response.value}")
else:
    print("Não foi possível obter os dados do RPM.")

connection.close()
