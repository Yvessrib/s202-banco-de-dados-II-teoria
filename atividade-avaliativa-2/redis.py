import redis

# Conectar ao Redis
client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Testar conexão
try:
    client.ping()
    print("Conexão com o Redis bem-sucedida!")
except redis.ConnectionError:
    print("Falha ao conectar ao Redis.")

# Inserir e recuperar dados
client.set('chave', 'valor')
print("Valor armazenado:", client.get('chave'))