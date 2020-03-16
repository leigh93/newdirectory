from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import alertletterForm

# from .models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('agency:index')
    else:
        form=UserCreationForm()
            
    return render(request, 'registration/signup.html', {'form':form})



# def AgencyAdminSgnupView(CreateView):
#     model = User
#     form = AgencyAdminSgnupForm
#     template = 'registration/register.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('agency:index')

#     pass

def sendalert(request):
    if request.method =='POST':
        form = alertletterForm(request.POST)
        if form.is_valid():
            print('valid')
        else:
            form = alertletterForm()
        return render(request, 'index.html', form)