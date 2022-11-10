from django.shortcuts import render

def indexfun(request):
    return render(request, 'index_templates/index.html')

def aboutfun(request):
    return render(request, 'index_templates/about.html')

def newsfun(request):
    return render(request, 'index_templates/news.html')

def workfun(request):
    return render(request, 'index_templates/work.html')

def academicsfun(request):
    return render(request, 'index_templates/academics.html')

def resourcesfun(request):
    return render(request, 'index_templates/resources.html')

def getinvolvedfun(request):
    return render(request, 'index_templates/getinvolved.html')   
    

# Create your views here.
