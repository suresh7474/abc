from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apil/', views.EmployeeAPIView.as_view()),
    path('apic/', views.EmployeeCreateAPIView.as_view()),
    url(r'^apid/(?P<id>\d+)/$',views.EmployyeRetrievDestoyAPIView.as_view()),
    path('apiv/',include('testapp.urls'))
]
