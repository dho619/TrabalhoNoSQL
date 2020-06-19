import sys
from mysqlInsert import insertDbMysql
from redisInsert import insertDRedis

#esta comentado pq demora umas boas horas pra inserir tds commentarios
#insertDbMysql(len(sys.argv) > 1 and sys.argv[1].lower() == 'create_db')

insertDRedis()

print('..|End Aplication')
