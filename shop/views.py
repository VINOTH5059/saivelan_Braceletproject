from django.shortcuts import render

def Home(request):
    # Just render home page (no model data)
    return render(request, 'shop/home.html')

def category(request):
    # Render category page without data
    return render(request, 'shop/category.html')

def product(request):
    # Render product page without data
    return render(request, 'shop/product.html')

def productDetails(request, id):
    # Render product details page without data
    return render(request, 'shop/product_details.html')
def cart(request):
    # your cart logic here
    return render(request, 'shop/cart.html')