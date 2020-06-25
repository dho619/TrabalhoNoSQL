import sys
from mysqlInsert import insertDbMysql
from redisInsert import insertDbRedis
from mongoInsert import insertDbMongo

#esta comentado pq demora umas boas horas pra inserir tds commentarios
#insertDbMysql(len(sys.argv) > 1 and sys.argv[1].lower() == 'create_db')

# insertDbRedis()
# insertDbMongo()

print('..|End Aplication')
