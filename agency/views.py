from django.shortcuts import get_object_or_404, render
from .models import Agency, Agent
from django.http import HttpResponse,Http404
from .forms import AddAgencyForm
from django.shortcuts import redirect

app_name = 'agency'
# Create your views here.
def index(request):
    all_agencies = Agency.objects.all()
    # context = {'all_agencies':all_agencies}  
    return render(request, 'index.html', locals())

def agency_detail(request, agency_id):

    try:
        agency = Agency.objects.get(pk = agency_id)
    except Agency.DoesNotExist:
        raise Http404()
        # context = {'agency':agency}
    return render(request, 'agencies/agency.html',{'agency':agency,})

def search(request):
    if 'agency' in request.GET and request.GET["agency"]:
        search_term = request.GET.get('agency')
        searched_agencies = Agency.search_by_name(search_term)
        message = f'{ search_term}'
        return render(request, 'search.html',{"message":message,"agencies":searched_agencies})
    else:
        message = 'We can\'t find any results ${message}'
        return render(request, 'agencies/search.html', locals())

# @login_required
def agency_upload(request):
    if request.method == 'POST':
        form = AddAgencyForm(request.POST, request.FILES)
        if form.is_valid():
            # agencyname = form.cleaned_data['agency_name']
            # registration_no = form.cleaned_data['registration_no']
            # agency_image = form.cleaned_data['agency_image']
            form.save()
            return redirect('agency:index')
            print('valid')
    else:
        form = AddAgencyForm()
    return render(request, 'addagency.html',{'form': form})