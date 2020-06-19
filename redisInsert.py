from dbRedis import db
from dbMysql import session, engine, Apps, CategoryType, Comments

def insertDRedis():
    categorys = session.query(CategoryType).join(CategoryType.apps).all()

    mapReduceInstalls = {}
    mapReduceRating = {}
    mapReduceReviews = {}
    mapReduceCount = {}
    #aplicando a ideia de map reduce
    for category in categorys:
        installs = 0
        rating = 0
        reviews = 0
        count = 0
        for app in category.apps:
            if app.num_installs != -1:#se for menos um e que era NaN anteriormente
                installs += app.num_installs
            if app.rating != -1 and app.reviews != -1:#se qualquer dos dois era NaN, nao preenche nenhum
                rating += app.rating
                reviews += app.reviews
            count += 1

        key = category.description
        mapReduceInstalls[key] = installs
        mapReduceRating[key] = rating
        mapReduceReviews[key] = reviews
        mapReduceCount[key] = count

    db.flushall()#limpar td o banco


    #adicionando no banco
    for keyDict, value in mapReduceCount.items():
        key = 'trabalhoNoSQL:Count:'+ keyDict
        db.set(key, value)

    for keyDict, value in mapReduceInstalls.items():
        key = 'trabalhoNoSQL:Installs:'+ keyDict
        db.set(key, value)

    for keyDict, value in mapReduceReviews.items():
        key = 'trabalhoNoSQL:Reviews:'+ keyDict
        db.set(key, value)

    for keyDict, value in mapReduceRating.items():
        key = 'trabalhoNoSQL:Rating:'+ keyDict
        db.set(key, value)


#pegar todos os apps de cada categoria e retirar:
#um tipo de aplicativo: tem qts downloads? qual a media de nota? qual a media de downloads?
