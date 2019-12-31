from django.db import models

class Article(models.Model):
    # 文章id
    id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    summary = models.TextField()
    # 文章内容
    content = models.TextField()
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True)
    #创建人id
    create_id = models.IntegerField(default=None)
    class Meta:
        db_table = 'articles'
