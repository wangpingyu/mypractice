from django.urls import path,include
from .import views

urlpatterns = [
    path('articles/',views.Articlelist.as_view()),
    path('detail/<int:id>',views.Articledetail.as_view())
]