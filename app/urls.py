from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordchangeForm, MyPasswordResetForm, MySetPasswordForm


admin.site.site_header = "PHARMACY"
admin.site.site_title = "PHARMACY"
admin.site.index_title = "PHARMACY"


urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),

    path('product-detail/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', views.show_cart, name='showcart'),

    path('pluscart/', views.plus_cart),

    path('minuscart/', views.minus_cart),

    path('removecart/', views.remove_cart),

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),

    path('masks/', views.masks, name='masks'),
    
    path('first_aid/', views.first_aid, name='first_aid'),

    path('sanitizer_handwash/', views.sanitizer_handwash, name='sanitizer_handwash'),

    path('diabetes/', views.diabetes, name='diabetes'),

    path('diabetes_supplements/', views.diabetes_supplements, name='diabetes_supplements'),

    path('boost_your_immunity/', views.boost_your_immunity, name='boost_your_immunity'),

    path('body_skin_care/', views.body_skin_care, name='body_skin_care'),

    path('hair_scalp_care/', views.hair_scalp_care, name='hair_scalp_care'),

    path('thermometers/', views.thermometers, name='thermometers'),

    path('diabetes_monitoring/', views.diabetes_monitoring, name='diabetes_monitoring'),

    path('checkout/', views.checkout, name='checkout'),

    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordchangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_confirm.html'), name='password_reset_confirm'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
