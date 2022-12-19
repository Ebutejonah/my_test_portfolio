from django.shortcuts import render
from .forms import RawReviewForm
from .models import Home,Review


def home_view(request):
    obj=Home.objects.all()
    form=RawReviewForm() 
    if request.method=='POST':
        form=RawReviewForm(request.POST or None)
        if form.is_valid():
            Review.objects.create(**form.cleaned_data)
            form=RawReviewForm()
    context={'object':obj, 'form':form}
    return render(request,'home/home.html',context)

def portfolio_view(request):
    obj=Home.objects.get(id=3)
    context={'object':obj}
    return render(request,"home/portfolio.html",context)

def webdesign_view(request):
    obj=Home.objects.get(id=3)
    context={'object':obj}
    return render(request,"home/web_design.html",context)

def machinelearning_view(request):
    obj=Home.objects.get(id=3)
    context={'object':obj}
    return render(request,"home/machine_learn.html",context)

def appdev_view(request):
    obj=Home.objects.get(id=3)
    context={'object':obj}
    return render(request,"home/app_dev.html",context)
