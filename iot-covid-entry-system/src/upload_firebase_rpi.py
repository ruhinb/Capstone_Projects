import pyrebase

#Initialize Firebase
# The project settings live in config.py, which is not committed.
# Copy config.example.py to config.py and fill in your own Firebase project.
from config import firebaseConfig

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
