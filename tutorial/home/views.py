from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
        args = {'form': form , 'text' : text}
        return render(request, self.template_name, args)