from django.shortcuts import render

# Create your views here.
def about(request):
    about_content = {'about': 'Based in Chicago, Illinois, Little Lemon is a small business that specializes in creating handmade, all-natural bath and body products. Our products are made with the finest ingredients and are free of harsh chemicals, artificial fragrances, and synthetic preservatives. We believe that what you put on your body is just as important as what you put in it, which is why we are committed to creating products that are safe, effective, and good for you. Our mission is to provide our customers with high-quality, affordable products that promote health and well-being, while also being environmentally friendly and sustainable. We are passionate about what we do and are dedicated to making a positive impact on the world. Thank you for supporting our small business!'}
    return render(request, 'about.html', about_content)