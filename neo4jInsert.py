from dbNeo4j import dbNeo4j
from dbMongo import dbMongo, cliente

def relacionaNumInstalls(num, category, auxInstall):
    if num < 100000000:
        category.relationships.create("Possui", auxInstall[0])
    elif num > 100000000 and num < 500000000:
        category.relationships.create("Possui", auxInstall[1])
    elif num > 500000000 and num < 1000000000:
        category.relationships.create("Possui", auxInstall[2])
    elif num > 1000000000 and num < 2000000000:
        category.relationships.create("Possui", auxInstall[3])
    elif num > 2000000000 and num < 3000000000:
        category.relationships.create("Possui", auxInstall[4])
    else:
        category.relationships.create("Possui", auxInstall[5])

def relacionaRating(num, category, auxRating):
    if num < 1:
        category.relationships.create("Possui", auxRating[0])
    elif num > 1 and num < 2:
        category.relationships.create("Possui", auxRating[1])
    elif num > 2 and num < 3:
        category.relationships.create("Possui", auxRating[2])
    elif num > 3 and num < 4:
        category.relationships.create("Possui", auxRating[3])
    else:
        category.relationships.create("Possui", auxRating[4])


def insertDbNeo4j():

    dbNeo4j.query('MATCH (n) DETACH DELETE n', returns=())#limpar banco

    ratings = dbNeo4j.labels.create("Ratings")
    reviews = dbNeo4j.labels.create("Reviews")
    installs = dbNeo4j.labels.create("Installs")
    comments = dbNeo4j.labels.create("Comments")
    categorys = dbNeo4j.labels.create("Category")

    auxInstall = []
    auxRating = []

    for i, valor in enumerate(['< 100M', '> 100M and < 500M', '> 500M and < 1B', '> 1B and < 2B', '> 2B and < 3B', '> 3B']):
        auxInstall.append(dbNeo4j.nodes.create(interval=valor))
        installs.add(auxInstall[i])

    for i, valor in enumerate(['Menor que 1', 'Entre 1 e 2', 'Entre 2 e 3', 'Entre 3 e 4', 'Maior que 4']):
        auxRating.append(dbNeo4j.nodes.create(Nota=valor))
        reviews.add(auxRating[i])


    listaTipoApp = dbMongo.TipoAplicacao.find()

    for TipoApp in listaTipoApp:
        category = dbNeo4j.nodes.create(description=TipoApp['description'], num_Apps=len(TipoApp['apps']), rating=TipoApp['rating'], review=TipoApp['reviews'], num_installs=TipoApp['num_installs'], num_comments=TipoApp['num_comments'])
        categorys.add(category)
        relacionaNumInstalls(TipoApp['num_installs'], category, auxInstall)
        relacionaRating(TipoApp['rating'], category, auxRating)



    cliente.close()
