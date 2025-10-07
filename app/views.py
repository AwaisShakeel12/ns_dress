from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dress, DressImage, Lace
from .forms import DressForm, LaceForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test


def home(request):
    dresses = Dress.objects.all()
    laces = Lace.objects.all()  # ← add this
    return render(request, 'home.html', {
        'dresses': dresses,
        'laces': laces  # ← pass to template
    })

def dress_list_all(request):
    dresses = Dress.objects.all()
    return render(request, 'dress_list_all.html', {'dresses': dresses})

# Full Lace List
def lace_list_all(request):
    laces = Lace.objects.all()
    return render(request, 'lace_list_all.html', {'laces': laces})

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


from django.shortcuts import render, get_object_or_404
from urllib.parse import quote

def dress_detail(request, id):
    dress = get_object_or_404(Dress, id=id)
    
    # Get the full URL of this dress page
    dress_url = request.build_absolute_uri()
    
    # Build WhatsApp message
    dress_name = f"{dress.brand_name} {dress.dress_type}"
    message = (
        f"Hi! I'm interested in this dress:\n\n"
        f"*{dress_name}*\n"
        f"Color: {dress.color}\n"
        f"Price: ${dress.price}\n"
        f"ID: {dress.id}\n"
        f"Link: {dress_url}\n\n"
        f"Please share more details."
    )
    
    encoded_message = quote(message)
    whatsapp_url = f"https://wa.me/923486439675?text={encoded_message}"
    
    return render(request, 'dress_detail.html', {
        'dress': dress,
        'whatsapp_url': whatsapp_url
    })




@superuser_required
def add_dress(request):
    if request.method == 'POST':
        form = DressForm(request.POST, request.FILES)
        if form.is_valid():
            dress = form.save()
            images = request.FILES.getlist('images')
            for img in images:
                dress.images.create(image=img)
            return redirect('dress_list_all')
    else:
        form = DressForm()
    return render(request, 'add_dress.html', {'form': form})

@superuser_required
def add_lace(request):
    if request.method == 'POST':
        form = LaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lace_list_all')
    else:
        form = LaceForm()
    return render(request, 'add_lace.html', {'form': form})




def lace_list(request):
    laces = Lace.objects.all()
    return render(request, 'lace_list.html', {'laces': laces})

def lace_detail(request, id):
    lace = get_object_or_404(Lace, id=id)
    return render(request, 'lace_detail.html', {'lace': lace})
