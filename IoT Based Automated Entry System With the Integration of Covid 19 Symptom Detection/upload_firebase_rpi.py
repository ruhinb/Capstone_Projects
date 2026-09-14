import pyrebase
import firebase
from argparse import ArgumentParser

#Initialize Firebase
firebaseConfig={
  'apiKey': "AIzaSyCJ7v732hAQOmHs2CMx2E1U5D__fLdiPhE",
  'authDomain': "entry-system-e981c.firebaseapp.com",
  'databaseURL': "https://entry-system-e981c-default-rtdb.firebaseio.com",
  'projectId': "entry-system-e981c",
  'storageBucket': "entry-system-e981c.appspot.com",
  'messagingSenderId': "960985398700",
  'appId': "1:960985398700:web:f7dba44a44d95851a6ce09",
  'measurementId': "G-MHY9RV1941"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def upload_data(data):
  # push data
  vals = list(data.values())
  data.pop("ID")
  db.child("Users").child(vals[0]).push(data)

def main(data):
    upload_data(data)

if __name__ == '__main__':
    main()
