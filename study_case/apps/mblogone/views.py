from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from study_case.apps.mblogone.models import Article, Comment


def index(request):
    latest_articles_list = Article.objects.order_by('-date_of_publication')[:5]
    return render(request, 'mblogone/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'mblogone/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found")
    print(request.POST['name'])
    a.comment_set.create(author_of_comment=request.POST['name'], text_of_comment=request.POST['text'])

    return HttpResponseRedirect(reverse('mblogone:detail', args=(a.id,)))
