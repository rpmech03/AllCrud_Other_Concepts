from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("addlanguage",views.addlanguage,name="addlanguage"),
    path("deletelanguage",views.deletelanguage,name="deletelanguage"),
    path("deldata",views.deldata,name="deldata"),
    path("updatelang",views.updatelang,name="updatelang"),
    path("search",views.search,name="search"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("addemp",views.addemp,name="addemp"),
    path("showemp",views.showemp,name="showemp"),
    path("addtrainer",views.addtrainer,name="addtrainer"),
    path("addstudent",views.addstudent,name="addstudent"),
    path("showstudent",views.showstudent,name="showstudent"),
    path("deletestudent",views.deletestudent,name="deletestudent"),
    path("updatestudent",views.updatestudent,name="updatestudent"),
    path("addcust",views.addcust,name="addcust"),
    path("showcust",views.showcust,name="showcust"),
    path("deletecust",views.deletecust,name="deletecust"),
    path("updatecust",views.updatecust,name="updatecust"),
    path("addaddress",views.addaddress,name="addaddress"),
    path("showaddress",views.showaddress,name="showaddress"),
    path("deleteaddress",views.deleteaddress,name="deleteaddress"),
    path("updateaddress",views.updateaddress,name="updateaddress"),
    path("stud",views.stud,name="stud"),
]