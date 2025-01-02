from django.shortcuts import render, redirect
from .models import Flower
from django.contrib import messages

# Home view
def home(request):
    if request.method == "POST":
        return render(request,'upload_flower.html')
    else:
        return render(request, 'home.html')


# Upload flower view
def upload_flower(request):
    if request.method == 'POST':
        print(request.POST)  # Debugging: Print POST data to terminal
        print(request.FILES)  # Debugging: Print FILES data to terminal

        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if name and description and image:
            flower = Flower(name=name, description=description, image=image)
            flower.save()
            messages.success(request, 'Flower uploaded successfully!')
            return redirect('flower_list')
        else:
            messages.error(request, 'All fields are required to upload a flower.')
    return render(request, 'upload_flower.html')


# Flower list view
def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flower_list.html', {'flowers': flowers})

def result_page(request):
    flower = None
    error_message = None

    if request.method == 'POST':
        flower_name = request.POST.get('flower_name')
        try:
            # Fetch the flower details by name
            flower = Flower.objects.get(name__iexact=flower_name)
        except Flower.DoesNotExist:
            # Handle the case where the flower is not found
            error_message = f"No details found for the flower: {flower_name}"

    return render(request, 'result.html', {'flower': flower, 'error_message': error_message})

