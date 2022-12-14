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
            print(formdata.get('fname'))

            if formdata:
                if formdata.get('fname')=="" or formdata.get('lname')=="" or formdata.get('email')=="" or formdata.get('gender')=="selectgender":
                    msg="Enter all details properly"
                    return render(req,template_name='add_user.html', context={"errormsg":msg})
                else:    
                    userinf=Userinfo(fname=formdata.get('fname'), lname=formdata.get('lname'), email=formdata.get('email'), gender=formdata.get('gender'))
                    
                    userinf.save()
                    msg='THANK YOU FOR REGISTRSTION'
        return render(req,template_name='add_user.html', context={"msg":msg})
    except:
        msg='SERVER SIDE ERROR'
        return render(req,template_name='add_user.html', context={"msg":msg})


#SHOW USER RECORDS FROM DATABASE
def show_users(req):
    msg=''
    try:
        userlist= Userinfo.objects.values_list('id','fname','lname','gender')
        #print(userlist)
        """
        HTML CODE TO PRINT DJANGO QUERY SET
        {% for user in userdata %}
            <tr>
                {% for u in user %}
                <td>{{u}}</td>    
                {% endfor %}
            </tr>
            {% endfor %}
        """
        return render(req, template_name='show_user_record.html', context={"userdata":userlist})
    except:
        msg="SERVER SIDE ERROR"
        return render(req, template_name='show_user_record.html', context={"msg":msg})


#FOR TRIAL OF IMAGES ON HTML PAGES
def show_image(req): 
    msg=''
    return render(req,template_name='showimage.html')


#FOR TRIAL OF SEINDING EMAIL
from django.conf import settings
from django.core.mail import send_mail

def send_email(req):
    eml=""
    try:
        if req.method=="POST":
            formdata=req.POST
            if formdata:
                eml=formdata.get('emailid')
                subject = 'welcome to my Website (c)PiYUSH'
                message = 'Hi, thank you for registering in geeksforgeeks.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [eml]
                send_mail( subject, message, email_from, recipient_list )
                msg='Email Sent... Please check you inbox..'
                return render(req,template_name='send_email.html', context={"msg":msg})
            else:
                msg="Please Enter Vaild email"
                return render(req,template_name='send_email.html', context={"errormsg":msg})
        return render(req,template_name='send_email.html', context={"msg":msg})
    except:
        msg="server side error..."
        return render(req,template_name='send_email.html', context={"msg":msg})

