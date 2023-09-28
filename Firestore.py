config = {
    "apiKey": "AIzaSyA7d3pKelVlv1mSXMBmjm9m-ArdSOqhGTs",
    "authDomain": "imagecollection-5e899.firebaseapp.com",
    "projectId": "imagecollection-5e899",
    "databaseURL":"https://imagecollection-5e899.firebaseapp.com",
    "storageBucket": "imagecollection-5e899.appspot.com",
    "messagingSenderId": "914830407640",
    "appId": "1:914830407640:web:36de690242c456788324ad",
    "measurementId": "G-HZX49KG4YE"
}

import pyrebase


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
my_image = "received_dpfd.jpg"
my_image_cloud = 'image/received_dpfd.jpg'

# Upload Image
storage.child(my_image_cloud).put(my_image)
