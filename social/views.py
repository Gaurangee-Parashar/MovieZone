from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def chat(request, user_id):
    context = {'receiver_id' : user_id}
    return render(request, 'social/chat.html', context)