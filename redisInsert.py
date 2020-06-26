from dbRedis import dbRedis
from dbMysql import session, engine, Apps, CategoryType, Comments

def insertDbRedis():
    categorys = session.query(CategoryType).join(CategoryType.apps).all()

    mapReduceInstalls = {}
    mapReduceRating = {}
    mapReduceReviews = {}
    mapReduceCountComments = {}
    #aplicando a ideia de map reduce
    for category in categorys:
        installs = 0
        rating = 0
        reviews = 0
        count_comments = 0
        count_Rating = 0
        for app in category.apps:
            if app.num_installs != -1:#se for menos um e que era NaN anteriormente
                installs += app.num_installs
            if app.rating != -1 and app.reviews != -1:#se qualquer dos dois era NaN, nao preenche nenhum
                rating += app.rating
                reviews += app.reviews
                if app.rating > 0:
                    count_Rating += 1

            count_comments += len(app.comments)

        key = category.description
        mapReduceInstalls[key] = installs
        mapReduceRating[key] = rating/count_Rating
        mapReduceReviews[key] = reviews
        mapReduceCountComments[key] = count_comments

    dbRedis.flushall()#limpar td o banco


    #adicionando no banco
    for keyDict, value in mapReduceCountComments.items():
        key = 'trabalhoNoSQL:countComments:'+ keyDict
        dbRedis.set(key, value)

    for keyDict, value in mapReduceInstalls.items():
        key = 'trabalhoNoSQL:Installs:'+ keyDict
        dbRedis.set(key, value)

    for keyDict, value in mapReduceReviews.items():
        key = 'trabalhoNoSQL:Reviews:'+ keyDict
        dbRedis.set(key, value)

    for keyDict, value in mapReduceRating.items():
        key = 'trabalhoNoSQL:Rating:'+ keyDict
        dbRedis.set(key, value)


#pegar todos os apps de cada categoria e retirar:
#um tipo de aplicativo: tem qts downloads? qual a media de nota? qual a media de downloads?
