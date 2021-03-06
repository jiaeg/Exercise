from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='博客分类')
    object_id = models.PositiveIntegerField(verbose_name='博客ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, verbose_name='评论用户')  # 谁写的

    root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='parent_comment',  null=True, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User, related_name="replies", null=True, on_delete=models.CASCADE, verbose_name='回复用户')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['comment_time']
        verbose_name = '评论列表'
        verbose_name_plural = verbose_name