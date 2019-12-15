from django.urls import path
from . import views
# multiple liberary of views that why we use from.import views ass compare to the import views
# /product(root)
urlpatterns =[
    path('', views.index),

]