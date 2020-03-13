import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Name of article', max_length=200)
    article_text = models.TextField('Content of article')
    date_of_publication = models.DateTimeField('Date of publishing')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.date_of_publication >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_of_comment = models.CharField('Author of comment', max_length=50)
    text_of_comment = models.CharField('Text of comment', max_length=200)

    def __str__(self):
        return self.author_of_comment
