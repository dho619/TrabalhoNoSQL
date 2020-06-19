import redis

#conectando no banco
db = redis.Redis(host='localhost')#criando o ligamento com o banco REDIS

#pegar todos os apps de cada categoria e retirar:
#um tipo de aplicativo: tem qts downloads? qual a media de nota? qual a media de downloads?
