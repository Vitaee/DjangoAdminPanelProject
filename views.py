from django.shortcuts import render, redirect
import pyrebase
from django.contrib.auth.decorators import login_required
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from firebase_admin import auth
import time 
import datetime

# Create your views here.
config = {
    'apiKey': "AIzaSyDALI2hXwfRjid4XmE3cZ2UxcvOcgxwVNg",
    'authDomain': "djangofire-e1a17.firebaseapp.com",
    'databaseURL': "https://djangofire-e1a17.firebaseio.com",
    'projectId': "djangofire-e1a17",
    'storageBucket': "djangofire-e1a17.appspot.com",
    'messagingSenderId': "442705561874",
    'appId': "1:442705561874:web:b5c121f9bf934658954bcb",
    'measurementId': "G-M3JMB2VCBJ"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
cred = credentials.Certificate('firestore/djangofire-e1a17-296743f53e56.json')
firebase_admin.initialize_app(cred)


def home(request):
    email = request.POST.get('email')
    password = request.POST.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return render(request, 'templates/welcome.html', {"e": email})
    except:
        message = "Kullanıcı bilgileri yanlış!"
        return render(request, 'templates/login.html', {"msg": message})

    


def loginPage(request):

    return render(request, 'templates/login.html')


def yaziEkle(request):
    return render(request, 'templates/yazi.html')


def yaziGonder(request):
    db = firestore.client()

    baslik = request.POST.get('baslik')
    icerik = request.POST.get('icerik')

    doc_ref = db.collection(baslik).document(baslik)
    doc_ref.set({
        "Baslık": baslik,
        "Icerik": icerik,
        "Tarih": firestore.SERVER_TIMESTAMP,
        
    })

    return render(request, 'templates/yazi.html')


def yazilar(request):
    db = firestore.client()

    docs = db.collection(u'Yazı Deneme Part 5').stream()
    for doc in docs:
        values1 = doc.to_dict()
    baslik1 = values1.get('Baslık')
    icerik1 = values1.get('Icerik')
  
    a = (f"{time.strftime('%X')}")

    doc_ref = db.collection(u'FireStore Yazı').stream()
    for doc in doc_ref:
        values = doc.to_dict()

    baslik = values.get('Baslık')
    icerik = values.get('Icerik')


    doc_ref = db.collection(u'Yazı Deneme 7').stream()
    for doc in doc_ref:
        values2 = doc.to_dict()
    
    baslik2 = values2.get('Baslık')
    icerik2 = values2.get('Icerik')

    context = {"a": a, "baslik":baslik,"icerik":icerik,"baslik1":baslik1,"baslik2":baslik2,
    "icerik1":icerik1, "icerik2":icerik2}

    return render(request, 'templates/yazılar.html', context)
