from django.db import models

#创建文章模型
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
    #设置admin管理后台显示
    def __str__(self):
        return self.title