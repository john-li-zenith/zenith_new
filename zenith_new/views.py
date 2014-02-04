from django.shortcuts import render
from zenith_new.form import ContactForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
    if request.method== 'POST':
       form = ContactForm(request.POST)

       if form.is_valid():
          return HttpResponseRedirect(reverse('home'))
    else:
       form=ContactForm(auto_id=False)
    return render(request,'index.html',{'form':form})
