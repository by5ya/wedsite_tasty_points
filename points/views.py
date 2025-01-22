from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')  

def point_page(request):
    return render(request, 'points.html')

def contact_page(request):
    return render(request, 'contacts.html')