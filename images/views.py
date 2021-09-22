from django.shortcuts import render,redirect
from .models import Upload
from .forms import EntryForm
from django.http import HttpResponse
from django.core.files.storage import default_storage
import pyrebase
import requests

# from google.cloud import storage as st


# # Create your views here.
config={
    'apiKey': "AIzaSyDnQIKQRYuORB7qlFVoOzBuVxn3sInuS-s",
    'authDomain': "logo-image-391ec.firebaseapp.com",
    'databaseURL':"https://logo-image-391ec-default-rtdb.firebaseio.com/",
    'projectId': "logo-image-391ec",
    'storageBucket': "logo-image-391ec.appspot.com",
    'messagingSenderId': "886005492994",
    'appId': "1:886005492994:web:c6fd651e71535b431ea61b",
    'measurementId': "G-FHHC18DP8Q",
    
}
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
# print(storage)

# def add(request):
#     if request.method=="POST":
#         if form.is_valid:
#             pngfile=request.FILES['png_image']
#             pngfile_save=default_storage.save(file.name,pngfile)
#             svgfile=request.FILES['svg_image']
#             svgfile_save=default_storage.save(file.name,svgfile)
#             storage.child("images/svg"+ svgfile.name).put("media/images/svg"+ svgfile.name)
#             storage.child("images/png"+ pngfile.name).put("media/images/png"+ pngfile.name)
#             form.save()
#             return redirect('Display_All')
#     else:
#         return render(request,"entry.html")
# client = st.Client()
# bucket = client.get_bucket("https://firebasestorage.googleapis.com/v0/b/logo-image-391ec.appspot.com")
# print(bucket)



list_url=[]
def Display_All(request):
    
    obj=Upload.objects.all().order_by('id')
    for i in obj:
        # print(i)
        url=storage.child(str(i.Image_png)).get_url(None)
        list_url.append(url)
    # print(obj[0].Image_png)
    # print(list_url)
    # print(list(zip(obj,list_url)))

    context={
        # 'obj':obj,
        # "url":list_url,
        'zipped':zip(obj,list_url),
    }

    return render(request,"index.html",context)

def Display_Images(request,slug):
    try:
        img=Upload.objects.filter(name=slug)
        # print(img[0].Image_png)
        url_png=storage.child(str(img[0].Image_png)).get_url(None)
        url_svg=storage.child(str(img[0].Image_svg)).get_url(None)
        # r = requests.get(url_png, stream=True)
        # print(r.status_code)
        # filename="hello.png"
        # if r.status_code==200:
        #     with open(filename, 'wb') as f:
        #         for chunk in r:
        #             f.write(chunk)



        context={
            'img':img[0],
            "url_png":url_png,
            'url_svg':url_svg,
        }
        return render(request,"imgview.html",context)
    except:
        return redirect("Display_All")
        

def about(request):
    obj=Upload.objects.all()
    context={
        'obj':obj,
    }
    return render(request,"about.html",context)
    # return redirect("Display_All")
def View_images(request):
    return redirect("Display_All")
def users(request):
    return redirect("Display_All")

def error_400(request, exception):
    return render(request,"error.html",{'error':"400 Bad Request","mesg":"Your browser sent a request that this server could not understand."})

def error_403(request, exception):
    return render(request,"error.html",{'error':'403 Forbidden',"mesg":" The page or resource you were trying to reach is absolutely forbidden for some reason."})

def error_404(request, exception):
    return render(request,"error.html",{'error':'404 Page Not Found',"mesg":"The requested URL was not found on this server."})

def error_500(request):
    return render(request,"error.html",{'error':'500 Server Error',"mesg":"The server encountered an internal error or misconfiguration and was unable to complete your request."})