import graphene
from graphene_django import DjangoObjectType
from .models import Books


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id', 'title', 'excerpt')

"""type Books {
    id: id
    title: String
    excerpt: String
}
"""
class Query(graphene.ObjectType):

    all_books = graphene.List(BooksType)

    @graphene.resolve_only_args
    def resolve_all_books(self):
        return Books.objects.all()


schema = graphene.Schema(query=Query)
