from django.shortcuts import redirect, render
from .models import Students,Language,Emp,Student,Trainer,Customer,Vendor,Ceo,Address
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def home(request):
    st=Language.objects.all()
    #print(st)
    return render(request,'index.html',{'data':st})

def stud(request):
    sd=Students.objects.all()
    # if request.method=='POST':
    #     sd=Students()
    #     sd.roll=request.POST['roll']
    #     sd.name=request.POST['name']
    #     sd.dob=request.POST['dob']
    #     sd.gender=request.POST['gender']
    #     f=request.POST['fees']
    #     f=int(f)
    #     sd.fees=f
    #     sd.about=request.POST['about']
    #     sd.img=request.POST['img']
    #     sd.save()
    #     messages.success(request,"student added sucessfully")
    #     return redirect("/")
    # else:
    return render(request,'stud.html',{'data':sd})
def addlanguage(request):
    if request.method=='POST':
        l=Language()
        l.lname=request.POST['lname']
        f=request.POST['fees']
        f=int(f)
        l.fees=f
        l.duration=request.POST['duration']
        l.trainer=request.POST['trainer']
        l.save()
        messages.success(request,"language added sucessfully")
        return redirect("/")
    else:
        return render(request,'addlanguage.html')
def deletelanguage(request):
    if request.method=='POST':
        id=request.POST['id']
        Language.objects.filter(id=id).delete()
        return redirect("/")
    else:
        return render(request,'delete.html')

 #delete language option nearby update option.       
def deldata(request):
    lname=request.GET['lname']
    Language.objects.filter(lname=lname).delete()
    messages.info(request,"language deleted sucessfully")
    st=Language.objects.all()
    #print(st)
    return render(request,'index.html',{'data':st})
    
    #return render(request,'delete.html')
def updatelang(request):
    l=Language()
    l.id=request.POST['id']
    l.lname=request.POST['lname']
    f=request.POST['fees']
    f=int(f)
    l.fees=f
    l.duration=request.POST['duration']
    l.trainer=request.POST['trainer']
    l.save()
    st=Language.objects.all()
    #print(st)
    return render(request,'index.html',{'data':st})
def search(request):
    lname=request.POST['lname']
    st=Language.objects.filter(lname=lname).all()
    #print(st)
    return render(request,'index.html',{'data':st})
def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        rpassword=request.POST['rpwd']
        if User.objects.filter(username=uname).exists():
            messages.info(request,"username already exists")
            return redirect("/")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
            return redirect("/")
        elif password!=rpassword:
            messages.info(request,"password missmatched")
            return redirect("/")
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,
            password=password)
        user.save()
        messages.success(request,"signed up sucessfully")
        return redirect("/")
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    messages.info(request,'Logout successfully')
    return redirect("/")
def addemp(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        rpassword=request.POST['rpwd']
        mob=request.POST['mob']
        address=request.POST['address']
        if User.objects.filter(username=uname).exists():
            messages.info(request,"username already exists")
            return redirect("/")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
            return redirect("/")
        elif password!=rpassword:
            messages.info(request,"password missmatched")
            return redirect("/")
        else:
            user=Emp.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
        user.mob=mob
        user.address=address
        user.save()
        messages.success(request,"Employee added sucessfully")
        return redirect("/")
    else:
        return render(request,'addemp.html')
def showemp(request):
    data=Emp.objects.all()
    return render(request,'showemp.html',{'data':data})

def addtrainer(request):
    if request.method=='POST':
        t=Trainer()
        t.name=request.POST['name']
        t.qualification=request.POST['qualification']
        t.languages=request.POST['languages']
        t.save()
        messages.success(request,"trainer added sucessfully")
        return redirect("/")
    else:
        return render(request,'addtrainer.html')
def addstudent(request):
    if request.method=='POST':
        s=Student()
        s.sname=request.POST['sname']
        s.branch=request.POST['branch']
        s.year=request.POST['year']
        id=request.POST['trainer']
        t=Trainer.objects.filter(id=id).get()
        s.trainer=t
        s.save()
        messages.info(request,"student added sucessfully")
        return redirect("/")
    else:
        tr=Trainer.objects.all()
        return render(request,'addstudent.html',{'tr':tr})
def showstudent(request):
    st=Student.objects.all()
    tr=Trainer.objects.all()
    return render(request,'showstudent.html',{'st':st,'tr':tr})
def deletestudent(request):
    id=request.GET['id']
    Student.objects.filter(id=id).delete()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'showstudent.html',{'st':st,'tr':tr})
def updatestudent(request):
    s=Student()
    s.id=request.POST['id']
    s.sname=request.POST['sname']
    s.branch=request.POST['branch']
    s.year=request.POST['year']
    id=request.POST['trainer']
    t=Trainer.objects.filter(id=id).get()
    s.trainer=t
    s.save()
    messages.info(request,"student updated sucessfully")
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'showstudent.html',{'st':st,'tr':tr})
def page_not_found(request,exception):
    return render(request,'pagenotfound.html')
def addcust(request):
    if request.method=='POST':
        c=Customer()
        c.cname=request.POST['cname']
        c.caddress=request.POST['caddress']
        c.save()
        data=request.POST.getlist('vendor')
        for i in data:
            t=Vendor.objects.filter(id=i).get()
            c.vendors.add(t)
        ven=Vendor.objects.all()
        return render(request,'addcust.html',{'ven':ven})
    else:
        ven=Vendor.objects.all()
        return render(request,'addcust.html',{'ven':ven})
def showcust(request):
    ven=Vendor.objects.all()
    cust=Customer.objects.all()
    return render(request,'showcust.html',{'ven':ven,'cust':cust})
def deletecust(request):
    id=request.GET['id']
    Customer.objects.filter(id=id).delete()
    ven=Vendor.objects.all()
    cust=Customer.objects.all()
    return render(request,'showcust.html',{'ven':ven,'cust':cust})
def updatecust(request):
    id=request.POST['id']
    c=Customer.objects.filter(id=id).get()
    c.cname=request.POST['cname']
    c.caddress=request.POST['caddress']
    c.save()
    data=request.POST.getlist('vendors')
    for i in data:
        t=Vendor.objects.filter(id=i).get()
        c.vendors.add(t)
    ven=Vendor.objects.all()
    cust=Customer.objects.all()
    return render(request,'showcust.html',{'ven':ven,'cust':cust})
    
def addaddress(request):
    if request.method=='POST':
        a=Address()
        cid=request.POST['ceo']
        a.ceo=Ceo.objects.filter(id=cid).get()
        a.street=request.POST['street']
        a.city=request.POST['city']
        a.state=request.POST['state']
        a.save()
        data=Ceo.objects.all()
        return render(request,'addaddress.html',{'data':data})
    else:
        data=Ceo.objects.all()
        return render(request,'addaddress.html',{'data':data})
def showaddress(request):
    data=Address.objects.all()
    return render(request,'showaddress.html',{'data':data})
def deleteaddress(request):
    id=request.GET['id']
    ceo=Ceo.objects.filter(id=id).get()
    Address.objects.filter(ceo=ceo).delete()
    data=Address.objects.all()
    ceo=Ceo.objects.all()
    return render(request,'showaddress.html',{'data':data,'ceo':ceo})
def updateaddress(request):
    id=request.POST['id']
    ceo=Ceo.objects.filter(id=id).get()
    ad=Address.objects.filter(ceo=ceo).get()
    ad.street=request.POST['street']
    ad.city=request.POST['city']
    ad.state=request.POST['state']
    ad.save()
    data=Address.objects.all()
    ceo=Ceo.objects.all()
    return render(request,'showaddress.html',{'data':data,'ceo':ceo})