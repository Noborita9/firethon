from firethon import Firebase

config = {
    "apiKey": "AIzaSyAJf9h2Iy9OTE_BspDdIeCG2ueIvJ24Q-0",
    "authDomain": "firethon-36e33.firebaseapp.com",
    "projectId": "firethon-36e33",
    "storageBucket": "firethon-36e33.appspot.com",
    "messagingSenderId": "103545605403",
    "appId": "1:103545605403:web:e09ad31c223a001776d7be",
    "measurementId": "G-1FN2WX8WBK",
    "databaseURL": ""
}

app = Firebase(config)
auth = app.auth()
login = auth.sign_in_with_email_and_password("nahuel123@gmail.com", "coolpass123")

