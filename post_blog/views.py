from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404

from datetime import datetime

from post_blog.models import Post, Comments, Categories, Feedback
from post_blog.forms import PostForm, CommentsForm

def post_list(request):
    post = Post.objects.all()
    categories = Categories.objects.all()
    return render(request,'post_blog/post_list.html',{'posts':post, 'categories':categories})

def categories(request, categories_pk):
    post = Post.objects.filter( categories = categories_pk)
    categories = Categories.objects.all()
    return render(request,'post_blog/post_list.html',{'posts':post, 'categories':categories})



def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.published_date = datetime.now()
            post.save()
            return redirect('post_list')
    else :
        form = PostForm()
        return render(request,'post_blog/createpost.html',{'forms':form})

def editpost(request,post_pk):
    post = get_object_or_404( Post, pk = post_pk )
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.published_date = datetime.now()
            post.save()
            return redirect('post_list', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_blog/editpost.html', {'forms': form})
    
def deletepost(request, post_pk):
    post = get_object_or_404(Post,pk = post_pk).delete()
    return redirect('post_list')

def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comments.objects.filter(post = post_pk)
    return render(request, 'post_blog/post_detail.html', {'post':post, 'comments':comments})


def feedback(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    fb = Feedback.objects.filter(post = post_pk)
    return render(request, 'post_blog/feedback.html', {'fb':fb})   



    
