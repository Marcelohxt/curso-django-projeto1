from django.urls import path

from recipes.views import home, contato , sobre

# Esse codigo eu deixei apenas como refencia antes da importação 


urlpatterns =[

    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]