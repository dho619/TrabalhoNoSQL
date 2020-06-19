import sys
from mysqlInsert import insertDbMysql


insertDbMysql(len(sys.argv) > 1 and sys.argv[1].lower() == 'create_db')



print('..|End Aplication')
