import imp
from django.shortcuts import render
from piyushhomepage.models import Userinfo

# Create your views here.
#MAIN/INDEX PAGE
def index_page(request):
    return render(request,template_name='index.html')


#GET DATA AND ADD TO DATABASE
def save_user_info(req):
    msg=''
    try:
        if req.method=='POST':
            formdata = req.POST

            if formdata:
                userinf=Userinfo(name=formdata.get('name'))
                userinf.save()
                msg='User record saved...'
        return render(req,template_name='add_user.html', context={"msg":msg})
    except:
        msg='SERVER SIDE ERROR'
        return render(req,template_name='add_user.html', context={"msg":msg})


#SHOW USER RECORDS FROM DATABASE
def show_users(req):
    msg=''
    try:
        userlist= Userinfo.objects.all()

        return render(req, template_name='show_user_record.html', context={"userdata":userlist})
    except:
        msg="SERVER SIDE ERROR"
        return render(req, template_name='show_user_record.html', context={"msg":msg})


#FOR TRIAL OF IMAGES ON HTML PAGES
def show_image(req): 
    msg=''
    return render(req,template_name='showimage.html')
