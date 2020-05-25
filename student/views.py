from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student


# Create your views here.

# def index(request):
#     # words = 'World!'
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = StudentForm()
#
#     context = {
#         'students': students,
#         'form': form,
#     }
#     return render(request, 'index.html', context=context)

class IndexView(View):
    template_name = 'index.html'

    def get_content(self):
        students = Student.get_all()
        context = {
            'student': students,
        }
        return context

    def get(self, request):
        context = self.get_content()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_content()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
