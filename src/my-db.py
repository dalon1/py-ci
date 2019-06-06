from firebase import firebase
class MyDb:
    def get_user(id):
        fb = firebase.FirebaseApplication(dsn='https://sandbox-dannel.firebaseio.com', authentication=None)
        result = fb.get('/users', None)
        return result