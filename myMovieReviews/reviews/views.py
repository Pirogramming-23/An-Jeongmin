from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm  

# Create your views here.
def review_list(request):
    sort = request.GET.get('sort', 'rating') # 기본값: 별점순
    if sort == 'rating':
        reviews = Review.objects.all().order_by('-rating')
    elif sort == 'year':
        reviews = Review.objects.all().order_by('-release_year')
    else:
        reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'reviews/list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    hours = review.running_time // 60
    minutes = review.running_time % 60  
    
    return render(request, 'reviews/detail.html', {
        'review': review,
        'hours': hours,
        'minutes': minutes,
    })

def review_create(request): 
    if request.method == "POST" :
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/create.html', {"form": form})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/create.html', {"form": form})

def review_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()

    return redirect("/reviews/")


