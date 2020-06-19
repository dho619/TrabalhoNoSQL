import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a engine do MySQL usando o MySQL Connector/Python
engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://geovane:1.618_3,14@localhost:3306/trabalhoNoSQL',
    echo=False)

# Define e cria a tabela
Base = declarative_base()

class CategoryType(Base):
    __tablename__ = 'category_type'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    apps = sqlalchemy.orm.relationship("Apps", back_populates='categoryType')

    def __repr__(self):
        return "<CategoryType(description='{0}'>".format(self.description)


class Apps(Base):
    __tablename__ = 'apps'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    rating = sqlalchemy.Column(sqlalchemy.Float)
    reviews = sqlalchemy.Column(sqlalchemy.Integer)
    num_installs = sqlalchemy.Column(sqlalchemy.Integer)
    paid = sqlalchemy.Column(sqlalchemy.Boolean)
    category_type_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('category_type.id'))
    categoryType = sqlalchemy.orm.relationship("CategoryType", back_populates='apps')
    comments = sqlalchemy.orm.relationship("Comments", back_populates='app')

    def __repr__(self):
        return "<Apps(name='{0}', rating='{1}', reviews='{2}', num_installs='{3}', paid='{4}')>".format(
                            self.name, self.rating, self.reviews, self.num_installs, self.paid)


class Comments(Base):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.String(length=3000))
    app_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('apps.id'))
    app = sqlalchemy.orm.relationship("Apps", back_populates='comments')

    def __repr__(self):
        return "<Comments(description='{0}'>".format(self.description)

# Criando uma sessao no banco
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
