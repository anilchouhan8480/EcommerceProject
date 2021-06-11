from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login_call),
    path('signup/', views.signup),
    # path('forgotpassword/', views.forgot),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name="passwordchange"),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),
        name="passwordchangedone"),
    path('reset/', views.reset_password),
    path('logout/',views.logout_call),
	path('seller/', include('seller.urls')),
    path('buyer/', include('buyer.urls')),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="passwordreset/password_reset.html",form_class=MyPasswordResetForm),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="passwordreset/password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="passwordreset/password_reset_confirm.html",form_class=MySetPasswordForm), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="passwordreset/password_reset_complete.html"), 
        name="password_reset_complete"),

    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)