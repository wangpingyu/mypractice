from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','summary','content','publish_date','create_id')
class DetailSerializer(serializers. ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','content')


