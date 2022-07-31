from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self, request):
        totalitem = 0
        masks = Product.objects.filter(category='M')
        first_aid = Product.objects.filter(category='FA')
        sanitizer_handwash = Product.objects.filter(category='SH')
        diabetes = Product.objects.filter(category='D')
        diabetes_supplements = Product.objects.filter(category='DS')
        boost_immuniity = Product.objects.filter(category='BYI')
        body_skin_care = Product.objects.filter(category='BSC')
        hair_scalp_care = Product.objects.filter(category='HSC')
        thermometers = Product.objects.filter(category='T')
        diabetes_monitoring = Product.objects.filter(category='DM')
        trending = Product.objects.filter(category='TT')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        # print('called')
        # print(first_aid)
        return render(request, 'app/home.html',{'masks':masks, 'first_aid':first_aid,'sanitizer_handwash':sanitizer_handwash, 'diabetes':diabetes, 'diabetes_supplements':diabetes_supplements, 'boost_immuniity':boost_immuniity, 'body_skin_care':body_skin_care,'hair_scalp_care':hair_scalp_care,'thermometers':thermometers,'diabetes_monitorin':diabetes_monitoring, 'trending':trending, 'totalitem':totalitem})


class ProductDetailView(View):
    def get(self, request, id):
        totalitem = 0
        product = Product.objects.get(id=id)
        item_already_in_cart = False 
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})

@login_required
def add_to_cart(request):
    user = request.user
    product_id =request.GET.get('prod_id')
    # size=request.GET.get('size')
    product = Product.objects.get(id=product_id)
    print(product , user)
    Cart(user=user, product=product).save()
        
    return redirect('/cart')

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount': amount, 'totalitem':totalitem})

        else:
            return render(request, 'app/emptycart.html')

def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary', 'totalitem':totalitem})

def masks(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    masks = Product.objects.filter(category='M')
    return render(request, 'app/masks.html', {'masks':masks, 'totalitem':totalitem})
 
def first_aid(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    first_aid = Product.objects.filter(category='FA')
    return render(request, 'app/first_aid.html', {'first_aid':first_aid, 'totalitem':totalitem})

def sanitizer_handwash(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    sanitizer_handwash = Product.objects.filter(category='SH')
    return render(request, 'app/sanitizer_handwash.html', {'sanitizer_handwash':sanitizer_handwash, 'totalitem':totalitem})

def diabetes(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    diabetes = Product.objects.filter(category='D')
    return render(request, 'app/diabetes.html', {'diabetes':diabetes, 'totalitem':totalitem})

def diabetes_supplements(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    diabetes_supplements = Product.objects.filter(category='DS')
    return render(request, 'app/diabetes_supplements.html', {'diabetes_supplements':diabetes_supplements, 'totalitem':totalitem})

def boost_your_immunity(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    boost_your_immunity = Product.objects.filter(category='BYI')
    return render(request, 'app/boost_your_immunity.html', {'boost_your_immunity':boost_your_immunity, 'totalitem':totalitem})

def body_skin_care(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    body_skin_care = Product.objects.filter(category='BSC')
    return render(request, 'app/body_skin_care.html', {'body_skin_care':body_skin_care, 'totalitem':totalitem})

def hair_scalp_care(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    hair_scalp_care = Product.objects.filter(category='HSC')
    return render(request, 'app/hair_scalp_care.html', {'hair_scalp_care':hair_scalp_care, 'totalitem':totalitem})

def thermometers(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    thermometers = Product.objects.filter(category='T')
    return render(request, 'app/thermometers.html', {'thermometers':thermometers, 'totalitem':totalitem})

def diabetes_monitoring(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    diabetes_monitoring = Product.objects.filter(category='DM')
    return render(request, 'app/diabetes_monitoring.html', {'diabetes_monitoring':diabetes_monitoring, 'totalitem':totalitem})

def login(request):
 return render(request, 'app/login.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form}) 

@login_required
def checkout(request):
    totalitem = 0
    if request.user.is_authenticated:
     totalitem = len(Cart.objects.filter(user=request.user))
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items, 'totalitem':totalitem})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product,  quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

@login_required
def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    op= OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op, 'totalitem':totalitem})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})
    
    def post(self, request):
        totalitem = 0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state'] 
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, phone=phone, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary', 'totalitem':totalitem})