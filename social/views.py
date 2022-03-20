from http.client import HTTPResponse
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
import uuid

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

def new_review(request):
    if request.method == 'POST':
        review = Review.objects.create(
            user = request.user,
            movie_id = request.POST.get('movie_id'),
            id=str(uuid.uuid4()),
            body = request.POST.get('body')
        )
    
        data = model_to_dict(review)
        return JsonResponse(data)    