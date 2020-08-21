from django.shortcuts import render, redirect, HttpResponseRedirect

from ghostpost_app.models import BoastsAndRoasts
from ghostpost_app.forms import BoastsAndRoastsForm

# Create your views here.
def index_view(request):
    posts = BoastsAndRoasts.objects.all().order_by('-submissiondate')
    return render(request, 'index.html', {"posts": posts})

def boasts_view(request):
    posts = BoastsAndRoasts.objects.filter(isroast=False).order_by('-submissiondate')
    return render(request, 'boasts.html', {"posts": posts})

def roasts_view(request):
    posts = BoastsAndRoasts.objects.filter(isroast=True).order_by('-submissiondate')
    return render(request, 'roasts.html', {"posts": posts})

def sort_view(request):
    posts = BoastsAndRoasts.objects.all()
    posts = list(posts)
    posts = sorted(posts, key=lambda z:z.total_votes, reverse=True)
    return render(request, 'sort.html', {"posts": posts})

def createpost_view(request):
    if request.method == "POST":
        form = BoastsAndRoastsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastsAndRoasts.objects.create(isroast = data.get('isroast'),
                                           post_content = data.get('post_content'))
            return redirect("/")
    form = BoastsAndRoastsForm()
    return render(request, 'createpost.html', {"form": form})

# def deletepost_view(request, post_id):
#     return redirect("/")

def upvotes_view(request, upvote_id):
    post = BoastsAndRoasts.objects.get(id=upvote_id)
    post.upvotes = post.upvotes + 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvotes_view(request, downvote_id):
    post = BoastsAndRoasts.objects.get(id=downvote_id)
    post.downvotes = post.downvotes - 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
