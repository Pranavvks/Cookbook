import graphene 
from ingredients.schema import Query as PersonQuery

class Query(PersonQuery,graphene.ObjectType):
    pass 
schema = graphene.Schema(query=Query)