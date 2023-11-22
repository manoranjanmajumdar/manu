from django.urls import path
from . import views
from django.apps import AppConfig


class servicesConfig(AppConfig):
    name = 'services'


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('add_aws_skills/', views.add_aws_skills, name='add_aws_skills'),
   # path('aws_service_data/', views.aws_service_data, name='aws_service_data'),
    path('login/', views.login, name='login'),
   # path('delete/<int:id>', views.delete, name='delete'),
   # path('add_services/', views.add_services, name='add_services'),
   # path('add/', views.Add, name='add'),
   # path('edit/', views.Edit, name='edit'),
   # path('update/<str:id>', views.Update, name='update'),
   # path('delete/<str:id>', views.Delete, name='delete')

]

#
# urlpatterns = {
#     path('', views.home, name='home'),
#     # path('login/', views.login, name='login'),
#     path('account_configuration/', views.account_configuration, name='account_configuration'),
#     # path('policies_required/', views.policies_required, name='policies_required'),
# }

