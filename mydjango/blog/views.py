from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator
#博客内容
def article_content(request):
    articles = Article.objects.all()
    article = articles[0]
    title = article.title
    summary = article.summary
    content = article.content
    publish_date = article.publish_date
    article_content = '标题：{:},摘要：{:},内容：{:}，发布时间：{:}'.format(title,summary,content,publish_date)
    return HttpResponse(article_content)

articles = Article.objects.all()
#博客列表
def get_index_page(request):
    #获取页码（前端传参）
    new_articles = Article.objects.order_by('-publish_date')[:2]
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    p = Paginator(articles,2)
    num_pages = p.num_pages
    cur_page_articles = p.page(page)
    if cur_page_articles.has_next():
        next_page = page + 1
    else:
        next_page = page
    if cur_page_articles.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request,'index.html',
                  {
                      'article_list':cur_page_articles,
                      'num_page':num_pages,
                      'num_pages':range(1, num_pages + 1),
                      'cur_page':page,
                      'previous_page':previous_page,
                      'next_page':next_page,
                      'new_articles':new_articles,
                  }
                  )
#博客详情
def get_article_detail(request,id):
    cur_article = None
    previous_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    for index,article in enumerate(articles):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(articles)-1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.id == id:
            cur_article = article
            previous_article = articles[previous_index]
            next_article = articles[next_index]
            break
    return render(request,'detail.html',
                  {
                      'cur_article':cur_article,
                      'previous_article':previous_article,
                      'next_article':next_article,
                  })
