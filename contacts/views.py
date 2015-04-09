from django.shortcuts import render
from django.http import HttpResponse
from contacts.models import Person


def index(request):
    context_dict={'persons' : [], 'error' : ''}
    try:
        persons = Person.objects.all()
        if persons:
            cont_p=[]
            for p in persons:
                cont_p.append([str(p.name), str(p.surname), str(p.dateOfBirth), 
                                str(p.bio), str(p.jabber), str(p.email), str(p.skype), str(p.otherContact)],)
            context_dict['persons']= cont_p
        else:
            context_dict['error'] = " There is no persons in DB"
    except:
        context_dict['error'] = " Cant load data from DB"
    return render(request, "contacts/index.html", context_dict)
