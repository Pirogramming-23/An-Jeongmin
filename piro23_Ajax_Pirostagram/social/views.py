from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post, Comment

def home(request):
    posts = Post.objects.all() 
    return render(request, 'home.html',{
        'posts': posts, 'story_range': range(8), 'recommend_list': ['user1', 'user2', 'user3', 'user4']
    })

@csrf_exempt 
def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.like_count += 1
        post.save()
        return JsonResponse({'like_count': post.like_count})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')
        comment = Comment.objects.create(post=post, content=content)
        return JsonResponse({
            'id': comment.id,
            'content': comment.content,
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
