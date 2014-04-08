from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from dajaxice.utils import deserialize_form
from zenith_new.form import ContactForm
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = ContactForm(form)

    if form.is_valid():
        cd = form.cleaned_data
        send_mail(cd['phone'],cd['message'],cd['name']+'<'+cd['email']+'>',[r'zenith.technology.llc@gmail.com'], fail_silently=False)        
        dajax.alert(_("Thank you, we will contact you soon!"))
    else:
        error_list=form.errors.items() 
        dajax.alert(str(error_list))
    return dajax.json()

