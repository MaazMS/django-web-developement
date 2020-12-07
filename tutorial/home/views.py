from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all()
        return render(request, self.template_name , {'form': form, 'posts': posts})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)