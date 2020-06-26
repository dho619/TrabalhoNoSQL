from dbNeo4j import dbNeo4j
from dbMongo import dbMongo, cliente

def insertDbNeo4j():

    dbNeo4j.query('MATCH (n) DETACH DELETE n', returns=())#limpar banco

    listaTipoApp = dbMongo.TipoAplicacao.find()

    ratings = dbNeo4j.labels.create("Ratings")
    reviews = dbNeo4j.labels.create("Reviews")
    installs = dbNeo4j.labels.create("Installs")
    comments = dbNeo4j.labels.create("Comments")
    categorys = dbNeo4j.labels.create("Category")

    auxInstall = []

    for i, num in enumerate(['<10000', '>10000 and <50000', '>50000 and <100000', '>100000 and <500000', '>50000 and <1000000', '>1000000']):
        auxInstall.append(dbNeo4j.nodes.create(interval=num))
        installs.add(auxInstall[i])

    for TipoApp in listaTipoApp:
        category = dbNeo4j.nodes.create(description=TipoApp['description'], num_Apps=len(TipoApp['apps']), rating=TipoApp['rating'], review=TipoApp['reviews'], num_installs=TipoApp['num_installs'], num_comments=TipoApp['num_comments'])
        categorys.add(category)
        # alice.relationships.create("Conhece", bob, since=1980)

        if TipoApp['num_installs'] < 10000:
            category.relationships.create("Possui", auxInstall[0])
        elif TipoApp['num_installs'] > 10000 and TipoApp['num_installs'] < 50000:
            category.relationships.create("Possui", auxInstall[1])
        elif TipoApp['num_installs'] > 50000 and TipoApp['num_installs'] < 100000:
            category.relationships.create("Possui", auxInstall[2])
        elif TipoApp['num_installs'] > 100000 and TipoApp['num_installs'] < 500000:
            category.relationships.create("Possui", auxInstall[3])
        elif TipoApp['num_installs'] > 500000 and TipoApp['num_installs'] < 1000000:
            category.relationships.create("Possui", auxInstall[4])
        else:
            category.relationships.create("Possui", auxInstall[5])


    cliente.close()
