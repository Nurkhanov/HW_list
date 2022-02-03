from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView,FormView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.


@login_required(login_url = 'log_in')
def home(request):
    return render(request, template_name='index.html')


@login_required(login_url = 'log_in')
def log_out(request):
    logout(request)
    return redirect('log_in')


@login_required(login_url = 'log_in')
def show_hw(request):

    hw_objects = HW.objects.filter(HW_user = request.user)
    form = HW_input(user = request.user)

    for i in hw_objects:
        if i.HW_deadline == None:
            i.HW_deadline = 'No deadline'

    if request.method == 'POST':
        form = HW_input(request.POST, request.FILES)
        
        if form.is_valid():
            form.instance.HW_user = request.user
            form.save()

        return redirect('show_hw')

    context = {'hw_objects': hw_objects,
                'form': form}

    return render(request, 'show_hw.html',context)


@login_required(login_url = 'log_in')
def change_hw(request):
    
    return render(request, template_name='change_hw.html')


@login_required
def create_course(request):

    form = Course_input()
    course_objects = Course.objects.all()

    if request.method == 'POST':

        form = Course_input(request.POST, request.FILES or None)

        if form.is_valid():
            form.instance.course_user = request.user
            form.save()

        return redirect('create_course')

    context = {'course_objects':course_objects,'form': form}
    return render(request, 'create_course.html', context)


def user_registration(request):

    form = User_input()
    if request.method == 'POST':

        form = User_input(request.POST, request.FILES)
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

class User_profile():
    #Custom made profile to change information about user
    
    pass

class HwCreateView(FormView,LoginRequiredMixin):
    form_class = HW_input
    template_name = 'crud_base.html'
    success_url = reverse_lazy('show_hw')

    def form_valid(self,form):
        form.instance.HW_user = self.request.user
        form.save()
        return super(HwCreateView,self).form_valid(form)

class HwUpdateView(UpdateView,LoginRequiredMixin):
    model = HW
    template_name = 'crud_base.html'
    fields = ('HW_name','HW_info','HW_course','HW_deadline')
    success_url = reverse_lazy('show_hw')

class HwDeleteView(DeleteView,LoginRequiredMixin):
    model = HW
    template_name = 'crud_delete.html'
    success_url = reverse_lazy('show_hw')
