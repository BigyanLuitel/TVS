"""
URL configuration for TVS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from students import views
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('delete_record/<int:id>/',views.delete_record,name='delete_record'),
    path('update_record/<int:id>/',views.update_record,name='update_record'),
    path('login_page/',views.login_page,name='login_page'),
    path('register_page/',views.register,name='register'),
    path('logout_page/',views.logout_page,name='logout_page'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
