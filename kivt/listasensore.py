import obd

# Tenta conectar na primeira porta disponível
connection = obd.OBD()

if connection.is_connected():
    print("Conectado ao OBD-II com sucesso!\n")
    
    # Lista de comandos suportados
    supported_commands = connection.supported_commands
    print("Sensores ativos detectados:\n")
    
    for cmd in supported_commands:
        response = connection.query(cmd)
        if response.value is not None:
            print(f"{cmd.name}: {response.value}")
        else:
            print(f"{cmd.name}: Não disponível")
else:
    print("Falha ao conectar ao OBD-II. Verifique a conexão.")

# Fecha a conexão ao final
connection.close()
