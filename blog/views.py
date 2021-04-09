from django.shortcuts import render
from django.http import HttpResponse

posts=[
{
    'author': 'Anvesh',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 10,2021'
},
{
    
    'author': 'Ramu',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 11,2021'
}
]

def home(request):
    context={
        'posts':posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request,'blog/home.html', context)
def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html')