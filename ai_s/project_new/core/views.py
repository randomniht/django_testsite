from django.shortcuts import render, get_object_or_404
from .models import Promt
# Create your views here.

def main(request):
    promts = Promt.objects.all()
    context = {'promts':promts}
    return render(request, 'main.html', context=context)

def promt_detail(request,promt_id):
    promt = get_object_or_404(Promt, id = promt_id)
    context = {'promt': promt}
    return render(request, 'promt_detail.html', context)
