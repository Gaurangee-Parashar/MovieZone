from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review

# Create your views here.

@login_required(login_url='login')
def delete_review(request, id):

    review = Review.objects.get(id=id)

    if request.user != review.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        review.delete()
        return redirect('home')
    return render(request, 'social/delete.html', {'obj' : review})
