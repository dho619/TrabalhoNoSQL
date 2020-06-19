import pandas as pd
from dbMysql import Base, engine, session, Apps, CategoryType, Comments

#se passar o parametro create_db, cria o banco
def insertDbMysql(create_db = False):
    if create_db:#se veio com o parametro de criar o banco, dropa tudo e cria novo
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    apps = pd.read_csv('apks.csv')#ler csv dos aplicativos
    comments = pd.read_csv('comentarios.csv')#ler csv dos comentarios

    apps = apps.fillna(-1) #substitui tds NaN por -1, para eu poder saber aonde era NaN
    comments = comments.fillna('') #substitui tds NaN por ''

    categoryTypes = set(apps['Category'].values)# pega valores unicos da coluna de categoria

    for category in categoryTypes:
        existe = session.query(CategoryType).filter_by(description=category[:100]).first() #verifica se categoria ja existe
        if existe: #se existe continua para o proximo do loop
            continue
        newCategory = CategoryType(description=category[:100])
        session.add(newCategory)
        session.commit()


    for app in apps.itertuples():
        existe = session.query(Apps).filter_by(name=app.App).first() #verifica se app ja existe
        if existe:#se existe continua para o proximo do loop
            continue
        #pega a categoria para adicionar ao App
        category = session.query(CategoryType).filter_by(description=app.Category).first()

        num_installs = int(app.Installs.replace(',','')) if app.Installs.isnumeric() else int(app.Installs.replace(',','')[:-1])

        newApp = Apps(name=app.App[:100], rating= app.Rating, reviews=int(app.Reviews), num_installs=num_installs, paid= app.Type == 'Paid')
        newApp.categoryType = category
        session.add(newApp)
        session.commit()

    for comment in comments.itertuples():
        #pega a App para adicionar ao Comentario
        app = session.query(Apps).filter_by(name=comment.App).first()
        newComment = Comments(description=comment.Translated_Review[:3000])
        newComment.app = app
        session.add(newComment)
        session.commit()
