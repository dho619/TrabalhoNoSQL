import redis

#conectando no banco
db = redis.Redis(host='localhost')#criando o ligamento com o banco REDIS
