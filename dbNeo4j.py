from neo4jrestclient.client import GraphDatabase

# conecta ao banco
dbNeo4j = GraphDatabase("http://localhost:7474", username="neo4j", password="1.618_3,14")

dbNeo4j.query('MATCH (n) DETACH DELETE n', returns=())#limpar banco

people = dbNeo4j.labels.create("Person")
alice = dbNeo4j.nodes.create(name="Alice", age=30)
bob = dbNeo4j.nodes.create(name="Bob", age=30)
people.add(alice, bob)
alice.relationships.create("Conhece", bob, since=1980)
