#author Moshi Musukwa
#used for rendering views
from django.core.mail import BadHeaderError, send_mail
#used for rendering views
from django.shortcuts import render
#used to handle requests
from django.http import HttpResponse
#used for redirects 
from django.http import HttpResponseRedirect
#imports pets model from model.py
from .models import Pets
#imports PetForm class from forms.py
from .forms  import PetForm,ContactForm



# Create your views here.

#method that pulls all/or in this case some of the lost but found pets
def index(request):
    #get the first 10 pet objects you can find
    

    if Pets.objects.count() > 0 :
             pets=Pets.objects.all()[:10]
             context={
                'pets':pets
             }
             render(request,'pets/index.html',context)
    else:

    	return HttpResponse('<p>There are currently no pets to view.</p>')




#method to store pet info
#wasn't going for the rhymes but kept running into them :-)
def set_pet(request):

# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a pet form instance and populate it with data from the request:
        form = PetForm(request.POST)
        # check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #get form data and commit to database
            obj = Pets() 
            obj.petname = form.cleaned_data['petname']
            obj.poster = form.cleaned_data['poster']
            obj.contact = form.cleaned_data['poster_contact']
            obj.description = form.cleaned_data['description']
            #finally save the object in db
            obj.save()
            messages.success(request, 'Your submission was Successfully Saved')

            # redirect to a new URL:
            return HttpResponseRedirect('pets')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PetForm()

        return render(request, 'pets/pet.html', {'form': form})


#method that shows the contact form
def contact(request):

	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a pet form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #get form data and commit to database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            message = form.cleaned_data['message']
            #finally send email using sendmail
            
            if name and message and email:
                try:
                     send_mail(name, message, email, ['admin@example.com'])
                except BadHeaderError:
                     return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/thanks/')
            else:
                # In reality we'd use a form class
                # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')

           

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

        return render(request, 'pets/contact.html', {'form': form})

   



#method that shows the about
def about(request):

    render(request,'pets/about.html')



