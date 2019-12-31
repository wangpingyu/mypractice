# from django.shortcuts import render
# from django.http import HttpResponse
# from articles.models import Article
# from articles.serializers import ArticleSerializer,DetailSerializer
# from rest_framework import status
# import json
#
# #获取所有的文章数据
# def articles(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         print(articles)
#         articleserializer = ArticleSerializer(articles,many=True)
#         print(articleserializer)
#         return HttpResponse(content=json.dumps(articleserializer.data),content_type='Application/Json',status=200)
#     else:
#         return HttpResponse(content='无此接口',content_type='Application/Json',status=400)
#
# #获取文章详情
# def article_detail(request,id):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         for article in articles:
#             if article.id == id:
#                 detailserializer = DetailSerializer(article)
#                 return HttpResponse(content=json.dumps(detailserializer.data), content_type='Application/Json',
#                                     status=status.HTTP_200_OK)
#                 break
#             else:
#                 return HttpResponse(content='该文章不存在', content_type='Application/Json',
#                                     status=status.HTTP_200_OK)
#     else:
#         return HttpResponse(content='无此接口111', content_type='Application/Json', status=status.HTTP_400_BAD_REQUEST)
#
# #发布文章
# def publish_article(request,title,summary,content,create_id):
#     if request.method == 'POST':
#         pass


'''
试用response及request
'''
# from rest_framework.response import Response
# from rest_framework import status
# from articles.serializers import ArticleSerializer
# from articles.models import Article
# from rest_framework.decorators import api_view
#
# #获取文章列表
# @api_view(['GET'])
# def articles(request):
#     articles = Article.objects.all()
#     articlesserializer = ArticleSerializer(articles,many=True)
#     return Response(data=articlesserializer.data,status=status.HTTP_200_OK)
#
# @api_view(['GET'])
# def article_detail(request,id):
#     articles = Article.objects.all()
#     for article in articles:
#         if id == article.id:
#             articlesserializer = ArticleSerializer(article)
#             return Response(data=articlesserializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(data='文章不存在，请重新确认',status=status.HTTP_200_OK)


'''
试用APIView
'''
from rest_framework.response import Response
from rest_framework import status
from articles.serializers import ArticleSerializer
from articles.models import Article
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

#获取文章列表及详情信息
class Articlelist(APIView):
    def get(self,request,format=None):
        articles = Article.objects.all()
        articlesserializer = ArticleSerializer(articles, many=True)
        return Response(data=articlesserializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        article = ArticleSerializer(data=request.data)
        if article.is_valid():
            article.save()
            return Response(data=article.data,status=status.HTTP_200_OK)
        else:
            return Response(data=article.errors,status=status.HTTP_400_BAD_REQUEST)


class Articledetail(APIView):
    def get(self,request,id,format=None):
        articles = Article.objects.all()
        for article in articles:
            if id == article.id:
                articlesserializer = ArticleSerializer(article)
                return Response(data=articlesserializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data='文章不存在，请重新确认',status=status.HTTP_200_OK)