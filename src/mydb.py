from firebase import firebase
# pip install firebase
# pip install python_jwt
# pip install gcloud
# pip install sseclient
# pip install Crypto
class MyDb:
    def get_user(id):
        fb = firebase.FirebaseApplication('https://sandbox-dannel.firebaseio.com', None)
        result = fb.get('/users', id)
        return result