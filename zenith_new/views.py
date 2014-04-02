from django.shortcuts import render
from zenith_new.form import ContactForm,LanguageForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail



def home(request):
    if request.method== 'POST':
       form = ContactForm(request.POST)
       lanform=LanguageForm(request.POST)

       if form.is_valid():
          cd = form.cleaned_data
          send_mail(cd['phone'],cd['message'],cd['name']+'<'+cd['email']+'>',[r'zenith.technology.llc@gmail.com'], fail_silently=False)  
          return HttpResponseRedirect(reverse('home'))
    else:
       form=ContactForm(auto_id=False)
       lanform=LanguageForm(auto_id=False)
    return render(request,'index.html',{'form':form,'lanform':lanform})
