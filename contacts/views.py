from django.shortcuts import render, redirect 
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.

def contact(request):
    if request.method == 'POST':
        
        listing_id = request.POST['listing_id'] 
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already an inquiry for this listing')
                return redirect('/listing/'+listing_id)


        contact = Contact(listing=listing, listing_id=listing_id,  name=name, email=email, 
        phone=phone, message=message, user_id=user_id )

        contact.save()

        #send mail
        """send_mail(
            'Property Listing Inquiry',
            'There are has been for'+ listing +'sign iin to admin panel for more info',
            'kittisitthichai30084@gmail.com',
            [realtor_email, 'kitti30084@gmail.com'],
            fail_silently=False,
        )"""

        messages.success(request, 'Your requset has been submit , wait Realtor Call back')
        return redirect('/listing/'+listing_id)


