from django.views.generic import CreateView
from .models import User

class UserCreateView(CreateView):
    model = User
    template_name =  'login.html'
    fields = ('name', 'email',)
