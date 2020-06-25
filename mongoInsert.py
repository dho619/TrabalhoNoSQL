from json import loads
from dbMongo import dbMongo, cliente
from dbRedis import dbRedis
from dbMysql import session, CategoryType

def insertDbMongo():

    categorys = session.query(CategoryType).join(CategoryType.apps).all()

    TipoAplicacao = dbMongo.TipoAplicacao
    TipoAplicacao.drop()
    for category in categorys:
        TipoApp = {
                      "description": category.description,
                      "num_comments": loads(dbRedis.get('trabalhoNoSQL:countComments:' + category.description)),
                      "num_installs": loads(dbRedis.get('trabalhoNoSQL:Installs:' + category.description)),
                      "reviews": loads(dbRedis.get('trabalhoNoSQL:Reviews:' + category.description)),
                      "rating": loads(dbRedis.get('trabalhoNoSQL:Rating:' + category.description))
        }
        apps = []
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
        id = TipoAplicacao.insert_one(TipoApp).inserted_id
        print(id)

    cliente.close

# album = banco.album
# musica_id = album.insert_one(musica).inserted_id
