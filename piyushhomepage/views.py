import imp
from django.shortcuts import render
from piyushhomepage.models import Userinfo

# Create your views here.
def index_page(request):
    return render(request,template_name='index.html')

def save_user_info(req):
    msg=''
    if req.method=='POST':
        formdata = req.POST

        if formdata:
            userinf=Userinfo(name=formdata.get('name'))
            userinf.save()
            msg='User record saved...'
    return render(req,template_name='add_user.html', context={"msg":msg})

def show_users(req):
    msg=''
    userlist= Userinfo.objects.all()

    return render(req, template_name='show_user_record.html', context={"userdata":userlist})

def show_image(req):
    msg=''
    return render(req,template_name='showimage.html')
    