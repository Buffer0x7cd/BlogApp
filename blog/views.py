from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import login_required
from .models import Post, Feedback
from .forms import PostForm, FeedbackForm
from django.utils import timezone, http
from django.http import HttpResponse
# Create your views here.

def post_list(request):
    ''' Render the list of published post'''
    posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context )


@login_required
def post_new(request):
    ''' Create a new post'''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post  = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form =  PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_detail(request, pk):
    ''' Show full blog'''
    post =  get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


@login_required
def post_edit(request, pk):
    ''' Edit a post'''
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def sendfeedback(request):
    ''' Send feedback message to admin'''

    if request.method =="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data =  form.cleaned_data
            Feedback.objects.create(title=data['title'], message=data['message'], user=request.user)
            return render(request, 'blog/thanks.html')

    else:
        form = FeedbackForm()
        return render(request, 'blog/feedback.html', {'form':form})


@login_required
def drafts(request):
    ''' Render the list of unpublished posts'''
    posts =  Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/drafts.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post =  get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def delete(request, pk):
    ''' Delete a post'''
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
