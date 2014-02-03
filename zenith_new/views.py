from django.shortcuts import render
from zenith_new.form import ContactForm

def home(request):
    if request.method== 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
          pass
    else:
       form=ContactForm(auto_id=False)
    return render(request,'index.html',{'form':form,})
