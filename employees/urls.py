from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from employees.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
