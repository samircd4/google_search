from django.shortcuts import render
from core.models import Directory
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        res = Q(Q(title__icontains=search) | Q(s_link__icontains=search) | Q(desc__icontains=search))
        results = Directory.objects.filter(res)
        contex = {
            'results': results,
            'search': search
        }
        return render(request, 'search.html', contex)
    return render(request, 'search.html')
