from django.shortcuts import render

# Create your views here.
def index(request):
    heading = "Post 1"
    article = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam et magnam fugit fuga."
    res = {'heading':heading, 'article':article}

    return render(request, 'posts/home.html', {'res':res})