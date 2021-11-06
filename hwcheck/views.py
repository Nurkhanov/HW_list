from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


from .models import *
from .forms import *
# Create your views here.



# class CreateHW(CreateView):
# """ It is testing Class-based view for forms """
#     template_name = 'create_hw.html'
#     form_class = HW_input
#     success_url = '/'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['HW'] = HW.objects.all()
#         return context

#     def get(self,request):
#         hw_objects = HW.objects.all()
#         context = {'hw_objects': hw_objects,}
#         return render(request, 'show_hw.html',context)


def home(request):
    return render(request, template_name='index.html')


def change_hw(request):
    return render(request, template_name='change_hw.html')


def user_registration(request):

    form = UserCreationForm()
    if request.method == 'POST':

        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid:

            form.save()
        return redirect('log_in')

    context = {'form':form}

    return render(request,'registration.html', context)


def log_in(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            return redirect('home')

        else:

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
    

    return render(request, 'log_in.html')


@login_required(login_url = 'log_in')
def show_hw(request):

    form = HW_input()
    hw_objects = HW.objects.all()

    if request.method == 'POST':
        form = HW_input(request.POST, request.FILES)
        if form.is_valid():
            
            form.user = request.user
            form.save()

        return redirect('show_hw')

    context = {'hw_objects': hw_objects,'form': form}
    return render(request, 'show_hw.html',context)