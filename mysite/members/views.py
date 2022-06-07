from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())

    # members = Members.objects.all().values()
    # output = ""

    # for member in members:
    #     output += member["firstName"]
    
    # return HttpResponse(output)
    
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))