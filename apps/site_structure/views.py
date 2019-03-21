from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    return render(request, "index.html", context)

def edit_show(request, id):
    context = {
        "this_show" : Show.objects.get(id = id)
    }
    return render(request, "edit_show.html", context)

def show_details(request, id):
    context = {
        "this_show" : Show.objects.get(id = id)
    }
    return render(request, "show_details.html", context)

def add_show(request):
    
    return render(request, "add_show.html")

def delete_show(request, id):
    a = Show.objects.get(id=id)
    a.delete()

    return redirect('/shows')

def process_form(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect('/shows')

def update_show_record(request):
    c = Show.objects.get(id=request.POST['id'])
    c.title = request.POST['title']
    c.network = request.POST['network']
    c.release_date = request.POST['release_date']
    c.description = request.POST['description']
    c.save()
    return redirect(f'/shows/{c.id}')