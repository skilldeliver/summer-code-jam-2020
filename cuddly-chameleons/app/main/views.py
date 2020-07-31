from django.shortcuts import render

# View for the Homepage
def homepage_view(request) :
    context = {}
    return render(request,'index.html',context=context)
