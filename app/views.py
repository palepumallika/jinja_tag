from django.shortcuts import render

# Create your views here.
def jinja_tag(request):
    d={'name':'malli','age':20}
    return render(request,'jinja_tag.html',d)