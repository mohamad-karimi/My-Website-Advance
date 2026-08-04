from django.views.generic import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from website.forms import ContactForm

# Create your views here.
class ContactFormView(FormView):
    '''
    This class for contact form with specefic contact form
    '''
    form_class = ContactForm
    template_name = 'website/contact.html'
    success_url = reverse_lazy('website:contact')

    '''
    Add a new fields to the contact(Full name of that user is login)
    '''
    # def get_initial(self):
    #     initial = super(ContactFormView, self).get_initial()
    #     if self.request.user.is_authenticated:
    #         initial.update({'name': self.request.user.get_full_name()})
    #     return initial
    
    '''
    Use that when you dont want to save the data into the DB 
    you want to send that contact to the admin email
    '''
    # def form_valid(self, form):

    #     name = form.cleaned_data["name"]
    #     email = form.cleaned_data["email"]
    #     message = form.cleaned_data["message"]

    #     send_mail(
    #         subject=f"New Contact from {name}",
    #         message=message,
    #         from_email=email,
    #         recipient_list=["admin@example.com"],
    #     )

    #     return super().form_valid(form)

    '''
    Use that when you want to save the data into the DB
    and send that contact to the admin email
    '''
    def form_valid(self, form):
        contact = form.save()

        # send_mail( 
        #     subject="New Contact",
        #     message=contact.message,
        #     from_email=contact.email,
        #     recipient_list=["admin@example.com"], 
        # ) 

        return super().form_valid(form)