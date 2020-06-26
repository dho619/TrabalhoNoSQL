from json import loads
from dbMongo import dbMongo, cliente
from dbRedis import dbRedis
from dbMysql import session, CategoryType

def insertDbMongo():

    categorys = session.query(CategoryType).join(CategoryType.apps).all()#pega tds categorias e apps

    TipoAplicacao = dbMongo.TipoAplicacao#cria ligamento com o banco
    TipoAplicacao.drop() #limpa o banco
    for category in categorys:
        TipoApp = { #json de criacao
                      "description": category.description,
                      "num_comments": loads(dbRedis.get('trabalhoNoSQL:countComments:' + category.description)),
                      "num_installs": loads(dbRedis.get('trabalhoNoSQL:Installs:' + category.description)),
                      "reviews": loads(dbRedis.get('trabalhoNoSQL:Reviews:' + category.description)),
                      "rating": loads(dbRedis.get('trabalhoNoSQL:Rating:' + category.description))
        }
        apps = []
        #adiciona tds apps
        for app in category.apps:
            app ={
                "name": app.name,
                'num_comments': len(app.comments),
                'num_installs': app.num_installs,
                'reviews': app.reviews,
                "rating": app.rating,
                'paid': app.paid
            }
            apps.append(app)
        TipoApp['apps'] = apps
        id = TipoAplicacao.insert_one(TipoApp).inserted_id#insere no banco
        print(id)

    cliente.close
