from django.shortcuts import render
from categories.models import Category
from CatalogApp.forms import CategoryForm
from django.conf import settings
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})


def create(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = CategoryForm(request.POST, request.FILES)
        # check if it's valid:
        if form.is_valid():
            # emailAddress = form.cleaned_data['email']
            # process data, insert into DB, generate email,etc
            # redirect to a new url:

            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    save_uploaded_file_to_media_root(formfile)
            # Create a model Category instance
            category = Category(categoryName=form.cleaned_data['categoryName'])

            # Invoke the save() method to create/save the record
            # No record id reference, so a create operation is made and the reference is updated with id
            category.save()

            # Invoke the save() method to update/save the record
            # Record has id reference from prior save() call, so operation is update
            # store_corporate.save()

            return HttpResponseRedirect('/categories/index')
        else:
            pass

    else:
        # GET, generate blank form
        request.user.first_name = "zubair"
        request.user.email = "mzubairshakoor@hotmail.com"
        form = CategoryForm()
    return render(request, 'categories/create.html', {'form': form})

def edit(request, id):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            categoryToEdit = Category.objects.get(id=id)
            categoryToEdit.categoryName = form.cleaned_data['categoryName']
            categoryToEdit.save()
            # messages.add_message(request, messages.SUCCESS, 'Contact has updated successfully.')
            # return HttpResponseRedirect('/contact/contactconfirmation')
            return HttpResponseRedirect('/categories/index')
        else:
            pass
            return render(request, 'categories/edit.html', {'form': form})

    else:
        categoryToEdit = Category.objects.get(id=id)
        form = CategoryForm(initial={'categoryName': categoryToEdit.categoryName})
        return render(request, 'categories/edit.html', {'form': form})

def save_uploaded_file_to_media_root(f):
    with open('%s%s' % (settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)