from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from User import views
from django.urls import path
from .views import add_to_cart, view_cart
urlpatterns = [
    path("",views.IndexPage,name="indexpage"),
    path("registerpage/",views.RegisterPage, name="registerpage"),
    path("register/",views.RegisterUser,name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),

    path("login/",views.Login,name="login"),


    path('register/', views.RegisterUser, name='register'),



    path("verify_otp/",views.verify_otp,name="verify_otp"),
    path('send_otp/', views.Send_Otp, name='send_otp'),

    path('forgotpasswordpage/', views.ForgotPasswordPage, name='forgotpasswordpage'),
    path('resetpassword/', views.ResetPassword, name='resetpassword'),


######################### USER URLS ####################################
    path('userpage/',views.UserView, name='userpage'),
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    # path('productdetailspage/<int:pk>/', views.productdetailsPage, name='productdetailspage'),
    path('productdetailspage/<str:session_id>/<int:pk>/', views.productdetailsPage, name='productdetailspage'),

    path('cartpage/',views.CartPage, name='cartpage'),


###################### Seller REgister ######################################
    path("sellerpage/",views.SellerPage,name="sellerpage"),
    path("sellerregister/",views.SellerRegister,name="sellerregister"),
    path("additempage/",views.AddItemPage,name="additempage"),
    path("addItem/",views.AddItem,name="addItem"),
    path('sellerprofile/<int:pk>',views.SellerProfile, name='sellerprofile'),
    path("updateSellerprofile/<int:pk>",views.UpdateSellerProfile,name="updateSellerprofile"),
###################### Display Product ######################################
    path("displayproductpage/<str:category>/", views.DisplayproductPage, name="displayproductpage"),
    path('subdisplayproductpage/<str:subcategory>/', views.SubDisplayproductPage, name='subdisplayproductpage'),

###################### Add to Cart  ######################################

    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),




]

if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)