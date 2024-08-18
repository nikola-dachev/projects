from django.shortcuts import render, redirect

from Fruitipedia1.fruits.forms import CategoryCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm
from Fruitipedia1.fruits.models import Fruit


# Create your views here.


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
    }
    return render(request, 'common/dashboard.html',context)


def create_fruit(request):
    if request.method == "GET":
        form = FruitCreateForm()

    elif request.method == "POST":
        form = FruitCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)


def create_category(request):
    if request.method == 'GET':
        form = CategoryCreateForm()

    elif request.method == "POST":
        form = CategoryCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'categories/create-category.html',context)


def details_fruit(request,pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit
    }
    return render(request, 'fruits/details-fruit.html',context)


def edit_fruit(request,pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)

    elif request.method == "POST":
        form = FruitEditForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request,pk):
    fruit = Fruit.objects.filter(pk= pk).get()

    if request.mehtod == "GET":
        form = FruitDeleteForm(instance=fruit)

    elif request.method == "POST":
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form':form
    }
    return render(request, 'fruits/delete-fruit.html', context)
