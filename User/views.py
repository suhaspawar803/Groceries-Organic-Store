from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from random import randint
from .models import UserMaster, Customer,Seller

   
# IndexPage view using the common context
def IndexPage(request):
    context = Displayproductbycategory()  # Use the common function to get the context
    return render(request, 'index.html', context)



# Main register logic view
def RegisterPage(request):
    return render(request,"register.html")

# login page view 
def LoginPage(request):
    return render(request,"login.html")







from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import UserMaster, Customer
from random import randint
import json
def RegisterUser(request):
    if request.method == 'POST':
        role = 'Customer'
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        mobile_number = request.POST['mobile_number']
        email_otp = request.POST.get('otp')

        # Check if the user already exists
        if UserMaster.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('register')  # Redirect back to the registration page

        # Check if the passwords match
        if password != cpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')  # Redirect back to the registration page

        # If OTP is provided, verify it
        if email_otp:
            stored_otp = request.session.get('email_otp')
            if not stored_otp or int(email_otp) != stored_otp:
                messages.error(request, 'Invalid OTP.')
                return redirect('register')  # Redirect back if the OTP is incorrect

            # If OTP is correct, create the user
            new_user = UserMaster.objects.create(
                role=role,
                name=name,
                email=email,
                password=password,  # You might want to hash this password.
                mobile_number=mobile_number,
            )
            Customer.objects.create(user_id=new_user)

            # Clear session data after successful registration
            del request.session['email_otp']

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('loginpage')  # Redirect to the login page

        # If OTP is not provided, send an OTP
        else:
            otp = randint(100000, 999999)
            try:
                subject = 'OTP Verification'
                message = f'Your OTP is {otp}. Please enter this OTP to verify your account.'
                from_email = 'ajaysupekar76@gmail.com'  # Replace with your email
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)

                # Store the OTP in the session
                request.session['email_otp'] = otp

                messages.info(request, 'OTP has been sent to your email.')
                return redirect('register')  # Redirect back to the registration page to show the OTP field
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')
                return redirect('register')  # Redirect back if there's an email error
    return render(request, 'register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from .models import UserMaster, Seller
from random import randint
from django.http import JsonResponse

def SellerRegister(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('seller_name')
        shop_name = request.POST.get('shop_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        gst = request.POST.get('gst')  # GST is fetched correctly now
        email_otp = request.POST.get('otp')  # OTP entered by the user

        # Check if the user already exists
        if UserMaster.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('sellerregister')

        # Check if passwords match
        if password != cpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('sellerregister')

        # If OTP is provided, verify it
        if email_otp:
            stored_otp = request.session.get('email_otp')
            if not stored_otp or email_otp != str(stored_otp):
                messages.error(request, 'Invalid OTP. Please try again.')
                return redirect('sellerregister')

            # OTP is correct, create the seller
            new_user = UserMaster.objects.create(
                role='Seller',
                name=name,
                email=email,
                password=password,  # Hashing the password
            )
            Seller.objects.create(
                user_id=new_user,
                shop_name=shop_name,
                gst=gst
            )

            # Clear session data after successful registration
            if 'email_otp' in request.session:
                del request.session['email_otp']

            return redirect('loginpage')  # Redirect to login page

        # If OTP is not provided, send OTP
        else:
            otp = randint(100000, 999999)
            try:
                subject = 'OTP Verification'
                message = f'Your OTP is {otp}. Please enter this OTP to verify your account.'
                from_email = 'ajaysupekar76@gmail.com'  # Replace with your email
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)

                # Store the OTP in the session
                request.session['email_otp'] = otp

                # Inform the user that OTP was sent
                return redirect('sellerregister')  # Redirect back to the same page
            except Exception as e:
                messages.error(request, f'Error sending OTP email: {str(e)}')
                return redirect('sellerregister')

    return render(request, 'register.html')






from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Seller, Customer  # Import your custom models if you have them
import json
from random import randint

@csrf_exempt
def Send_Otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        
        # Check if email exists in User, Seller, or Customer models
        user_exists = UserMaster.objects.filter(email=email).exists()
       
        if user_exists:
            return JsonResponse({'success': False, 'message': 'User already exists with this email.'})
        otp = randint(100000, 999999)
        try:
            send_mail(
                'OTP Verification',
                f'Your OTP is {otp}',
                'ajaysupekar76@gmail.com',  # Replace with your email
                [email],
                fail_silently=False,
            )
            request.session['email_otp'] = otp
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


def verify_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email_otp = int(data.get('otp'))
        stored_otp = request.session.get('email_otp')

        if stored_otp and email_otp == stored_otp:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})




def ForgotPasswordPage(request):
    return render(request,"forgot.html")


## real
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserMaster, Customer, Seller

def Login(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if role == "Customer":  # Handle Customer login
            try:
                user = UserMaster.objects.get(email=email, role=role)
                if user.password == password:
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['name'] = user.name
                    request.session['email'] = user.email
                    return redirect('userpage')
                else:
                    messages.error(request, 'Password does not match!')
                    return redirect('loginpage')
            except UserMaster.DoesNotExist:
                messages.error(request, 'User does not exist!')
                return redirect('loginpage')

        elif role == "Seller":  # Handle Seller login
            try:
                user = UserMaster.objects.get(email=email, role=role)
                if user.password == password:
                    # Check if a Seller object exists for this user
                    seller = Seller.objects.get(user_id=user)

                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['name'] = seller.seller_name  # Use the seller's name
                    request.session['email'] = user.email
                    return redirect('sellerpage')  # Redirect to the seller's page
                else:
                    messages.error(request, 'Password does not match!')
                    return redirect('loginpage')
            except UserMaster.DoesNotExist:
                messages.error(request, 'User does not exist!')
                return redirect('loginpage')
            except Seller.DoesNotExist:
                messages.error(request, 'Seller does not exist for this user!')
                return redirect('loginpage')
    
    return render(request, 'login.html')





from django.shortcuts import redirect
def ResetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')

        if new_password == confirm_password:
            try:
                user = UserMaster.objects.get(email=email)
                if len(new_password) <= 50:  # Ensure the password fits in the database field
                    user.password = new_password  # Directly assigning the password
                    user.save()
                    return redirect('loginpage')  # Redirect to login page after successful password reset
                else:
                    # Handle case where password is too long
                    return redirect('forgot_password')  # Optionally add a message to inform the user
            except UserMaster.DoesNotExist:
                # Handle case where user does not exist
                return redirect('forgot_password')  # Optionally add a message to inform the user
        else:
            # Handle password mismatch
            return redirect('forgot_password')  # Optionally add a message to inform the user

    return redirect('forgot_password')  # If request method is not POST, redirect to forgot password page





############################################# User View #########################################################
def  UserView(request):
    context = Displayproductbycategory()  # Use the common function to get the context
    return render(request,"user.html", context)


def  CartPage(request):
    return render(request,"cart.html")

from django.shortcuts import render, redirect, get_object_or_404
def ProfilePage(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)
    customer = get_object_or_404(Customer, user_id=user)
    return render(request, "profile.html", {'user': user, 'customer': customer})


def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Customer":
        can = Customer.objects.get(user_id=user)
        can.mobile_number = request.POST['mobile_number']
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.address= request.POST['address']
        can.dob = request.POST['dob']
        can.gender = request.POST['gender']
        can.landmark = request.POST['landmark']
        can.pincode = request.POST['pincode']
        can.gender = request.POST['gender']
        #can.profile_pic = request.FILES['profile_pic']
        can.save()
        url = f'/profilepage/{pk}'
        return redirect(url)



#######################  Seller   ##################

def SellerPage(request):
    return render(request,'seller/seller.html')

# def SellerProfile(request):
#     return render(request,'seller/Sellerprofile.html')



from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

def SellerProfile(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)
    seller = get_object_or_404(Seller, user_id=user)
    return render(request, "seller/Sellerprofile.html", {'user': user, 'seller': seller})

def UpdateSellerProfile(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)
    if user.role == "Seller":
        seller = get_object_or_404(Seller, user_id=user)

        if request.method == "POST":
            # Update the mobile number in the UserMaster model
            user.name = request.POST.get('name')
            user.mobile_number = request.POST.get('mobile_number')
            user.save()
            seller.seller_name = request.POST.get('name')
            seller.shop_name = request.POST.get('shopname')
            seller.seller_code = request.POST.get('SCode')
            seller.gst = request.POST.get('GST')
            seller.save()
            messages.success(request, "Profile updated successfully.")
            return redirect(f'/sellerprofile/{pk}')
        else:
            messages.error(request, "Invalid request method.")
            return redirect(f'/sellerprofile/{pk}')
    
    messages.error(request, "Invalid user role.")
    return redirect(f'/sellerprofile/{pk}')





def AddItemPage(request):
    return render(request,"seller/additem.html")


from .models import Item
def AddItem(request):
    if request.method == 'POST':
        item_images = request.FILES.getlist('itemImage[]')
        item_names = request.POST.getlist('itemName[]')
        item_categories = request.POST.getlist('itemCategory[]')
        item_subcategories = request.POST.getlist('itemSubCategory[]')
        item_typecategories = request.POST.getlist('itemTypeCategory[]')
        item_descriptions = request.POST.getlist('itemDescription[]')
        item_prices = request.POST.getlist('itemPrice[]')
        item_discounts = request.POST.getlist('itemDiscount[]')

        # Convert item_prices and item_discounts to floats or integers
        item_prices = [float(price) for price in item_prices]
        item_discounts = [float(discount) for discount in item_discounts]

        # Debugging: Print the request values
        print(item_images, item_names, item_categories)

        for i in range(len(item_images)):
            # Calculate the discounted price for each item
            if item_prices[i] and item_discounts[i]:
                discounted_price = int( item_prices[i] * (1 - (item_discounts[i] / 100)))
            else:
                discounted_price = int (item_prices[i] ) # No discount means original price

            # Create and save item in the database
            Item.objects.create(
                image=item_images[i],  # Django will handle saving the image
                name=item_names[i],
                category=item_categories[i],
                subcategory=item_subcategories[i],
                categorytype=item_typecategories[i],
                description=item_descriptions[i],
                price=item_prices[i],
                discount=item_discounts[i],
                discounted_price=discounted_price
            )
            messages.success(request, 'Item added successfully!')
    
    return redirect('sellerpage')


############################################# Display Product View #################################################

# def productdetailsPage(request, pk):
#     item = get_object_or_404(Item, id=pk)
#     return render(request, 'productdetails.html', {'item': item})
# from django.shortcuts import get_object_or_404, render
# from .models import UserMaster, Customer, Item

# def productdetailsPage(request, session_id, pk):
#     user = get_object_or_404(UserMaster, pk=session_id)
#     customer = get_object_or_404(Customer, user_id=user)
#     item = get_object_or_404(Item, id=pk)
#     return render(request, 'productdetails.html', {'item': item, 'customer': customer})
from django.shortcuts import get_object_or_404, render
from .models import Customer, Item

def productdetailsPage(request, session_id, pk):
    # Retrieve the customer based on the user's ID
    customer = get_object_or_404(Customer, user_id=request.user.id)
    item = get_object_or_404(Item, id=pk)
    
    return render(request, 'productdetails.html', {'item': item, 'customer': customer})



# from django.shortcuts import get_object_or_404, render
# from django.contrib.auth.decorators import login_required

# @login_required
# def productdetailsPage(request, pk):
#     # Fetch the item based on the product ID (pk)
#     item = get_object_or_404(Item, id=pk)

#     # Fetch the current user
#     user = request.user  # Get the logged-in user

#     # Assuming UserMaster is related to the user model
#     user_master = get_object_or_404(UserMaster, user=user)

#     # Assuming Customer is related to UserMaster
#     user_id = get_object_or_404(Customer, user_id=user_master)

#     return render(request, 'productdetails.html', {'item': item, 'user_id': user_id})


def Displayproductbycategory(category=None):
    if category:
        # Filter items by the selected category
        items = Item.objects.filter(category=category)

        # Group items by subcategory
        subcategories = items.values_list('subcategory', flat=True).distinct()
    else:
        # Show all items and subcategories if no category is selected
        items = Item.objects.all()
        subcategories = items.values_list('subcategory', flat=True).distinct()

    # Create a dictionary to hold subcategory-wise items
    items_by_subcategory = {}
    for subcategory in subcategories:
        items_by_subcategory[subcategory] = items.filter(subcategory=subcategory)

    return {
        'items_by_subcategory': items_by_subcategory,  # Pass the grouped items
        'category': category,
    }


def Displayproductbysubcategory(subcategory=None):
     # Filter items by the selected subcategory
    if subcategory:
        items = Item.objects.filter(subcategory=subcategory)
    else:
        items = Item.objects.all()  # Show all items if no subcategory is selected

    return {
        'items': items,
        'subcategory': subcategory,
    }

def DisplayproductPage(request, category):
    context = Displayproductbycategory(category) 
    return render(request, 'DisplayproductPage.html', context)

def SubDisplayproductPage(request, subcategory):
    context = Displayproductbysubcategory(subcategory) 
    return render(request, 'SubDisplayproductPage.html', context)

############################################# add to cart View #################################################

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cart, CartItem, Item  # Import your models

@login_required(login_url='/loginpage/')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        # Get the item to be added to the cart
        item = get_object_or_404(Item, id=product_id)

        # Get or create the cart for the authenticated user
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Get or create a cart item for the specific item
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        
        if not created:
            cart_item.quantity += 1  # Increase quantity if the item is already in the cart
        else:
            cart_item.quantity = 1  # Set initial quantity to 1 for new items
        
        cart_item.save()  # Save the cart item

        # Optionally, return a success response
        return JsonResponse({'message': 'Product added to cart successfully!', 'item_id': item.id})
    
    # If the request method is not POST, return an error response
    return JsonResponse({'error': 'Invalid request method'}, status=400)



def view_cart(request):
    cart = Cart.objects.get(user_id=request.user.id)  # Use user_id instead of user
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)
