# coding: utf-8

from django import forms
from django.core.exceptions import ValidationError
import re
from django.utils.translation import ugettext_lazy as _

def validate_phonenumber(value):
    p = re.compile('^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$')
    if not p.match(value):
        raise ValidationError(_('%s is not a valid phone number') % value)

class ContactForm(forms.Form):
    name = forms.CharField(label=_("name"),max_length=100,widget=forms.TextInput(attrs={'tabindex':'4','id':'name','name':'name','type':'text','value':'','class':'span12','placeholder':'Name: ...'}))
    email = forms.EmailField(label=_("email"),widget=forms.EmailInput(attrs={'tabindex':'2','id':'email','name':'email','type':'text','value':'','class':'span12','placeholder':'Email: ...'}))
    phone = forms.CharField(label=_("phone"),validators=[validate_phonenumber],widget=forms.TextInput(attrs={'tabindex':'3','id':'www','name':'www','type':'text','value':'','class':'span12','placeholder':'Phone: 123-234-3434'}))
    message = forms.CharField(label=_("message"),widget=forms.Textarea(attrs={'tabindex':'3','id':'message','name':'body','rows':'7','class':'input-xlarge span12','placeholder':'Message: ...'}))


