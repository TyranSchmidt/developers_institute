from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import ForumForm, CommentForm
from .models import Forum, Comment

# Create your views here.

def forum(request):
    all_items = Forum.objects.all()
    return render(request, 'Forum/Forum.html', {'items':all_items})

@login_required
def add_forum(request):
    form = ForumForm
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user
            forum.save()
            return redirect('forum')
    return render(request, 'Forum/Add_Forum.html', {'form':form})

def forum_post(request, post_id):
    forum = Forum.objects.get(id=post_id)
    if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.forum = forum
                comment.save()
    form = CommentForm
    return render(request, 'Forum/Post_Forum.html', {'post':forum, 'form':form})

def comment_delete(request,post_id, msg_id):
    del_comment = Comment.objects.get(id=msg_id)
    if del_comment.user == request.user:
        del_comment.delete()
    else:
        pass
        # flash message you are not authorized
    return redirect('forum_post', post_id)

#  comments = Comment.objects.filter(forum=forum)
#    print(comments)
#   comments = forum.comment_set.all()
#   print(comments)