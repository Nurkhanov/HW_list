from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
# Create your views here.



# class CreateHW(CreateView):

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

def show_hw(request):
    form = HW_input()
    hw_objects = HW.objects.all()

    if request.method == 'POST':
        form = HW_input(request.POST, request.FILES)
        print('check')
        if form.is_valid():
            form.save()

        return redirect('/show_hw')

    context = {'hw_objects': hw_objects,'form': form}
    return render(request, 'show_hw.html',context)