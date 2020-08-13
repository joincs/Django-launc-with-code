from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .forms import EmailForm
from .models import Join
import uuid
from lwc.middleware import ReferMiddleware
# Create your views here.

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

def get_ref_id():
    ref_id =  str(uuid.uuid4())[:11].replace('-','').lower()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id


def share(request,ref_id):
    join_obj = get_object_or_404(Join,ref_id=ref_id)
    count = join_obj.referral.all().count()
    ref_url = "http://127.0.0.1:8000/?ref={}".format(join_obj.ref_id)
    context = {
        'ref_id':join_obj.ref_id,
        'count':count,
        'ref_url':ref_url
    }
    temaplate = 'share.html'
    return render(request,temaplate,context)


def home(request):
    try:
        join_id = request.session['join_id_ref']
        obj = Join.objects.get(id=join_id)
    except:
        obj = None

    form = EmailForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data.get('email')
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            if not obj == None:
                new_join_old.firend = obj
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
        return HttpResponseRedirect('/{ref_id}'.format(ref_id=new_join_old.ref_id))
    else:
        form = EmailForm()
    context = {
        'form':form
    }
    return render(request,'index.html',context)
