from django.urls import path
from .views import liste_temperature


urlpatterns = [
    path('temp/', liste_temperature ),
    #path('details/',details_temp)
    

]