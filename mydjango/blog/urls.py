from django.urls import path
from . import views
urlpatterns = [
    path('content/',views.article_content),
    path('index/',views.get_index_page),
    path('detail/<int:id>',views.get_article_detail),
]