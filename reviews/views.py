import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from reviews.forms import ReviewForm
from .models import Review, Laptop


# Create your views here.

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {
        'latest_review_list': latest_review_list,
    }
    return render(request, 'review_list.html', context)


def review_detail(request, review_id=None):
    queryset = Review.objects.get(id=review_id)

    context = {
        'queryset': queryset,

    }
    return render(request, 'review_detail.html', context)


def laptop_list(request):
    laptop_list = Laptop.objects.order_by('-name')
    context = {
        'laptop_list': laptop_list,
    }
    return render(request, 'laptop_list.html', context)


def laptop_detail(request, laptop_id):
    queryset = get_object_or_404(Laptop, id=laptop_id)
    context = {
        'queryset': queryset,
    }
    return render(request, 'laptop_detail.html', context)


@login_required
def add_review(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        review = Review()
        review.laptop = laptop
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:review_detail', args=(review.id,)))

    return render(request, 'add_review.html', {'laptop': laptop, 'form': form})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list': latest_review_list, 'username': username}
    return render(request, 'user_review_list.html', context)
