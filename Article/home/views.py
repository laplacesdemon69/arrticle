from django.shortcuts import render, redirect

# Create your views here.

from .form import *
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'articles': ArticleModel.objects.all()}
    return render(request, 'home.html', context)

def post(request):
    return render(request, 'post.html')


def login_view(request):
    return render(request, 'login.html')


def article_detail(request, slug):
    context = {}
    try:
        article_obj = ArticleModel.objects.filter(slug=slug).first()
        context['article_obj'] = article_obj
    except Exception as e:
        print(e)
    return render(request, 'article_detail.html', context)


def see_article(request):
    context = {}

    try:
        article_objs = ArticleModel.objects.filter(user=request.user)
        context['article_objs'] = article_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_article.html', context)


def add_article(request):
    context = {'form': ArticleForm}
    try:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            article_obj = ArticleModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(article_obj)
            return redirect('/add-article/')
    except Exception as e:
        print(e)

    return render(request, 'add_article.html', context)


def article_update(request, slug):
    context = {}
    try:

        article_obj = ArticleModel.objects.get(slug=slug)

        if article_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': article_obj.content}
        form = ArticleForm(initial=initial_dict)
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            article_obj = ArticleModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )

        context['article_obj'] = article_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_article.html', context)


def article_delete(request, id):
    try:
        article_obj = ArticleModel.objects.get(id=id)

        if article_obj.user == request.user:
            article_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-article/')


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')
