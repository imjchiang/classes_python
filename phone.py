class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))
    
    def text(self, other_number, msg):
        print("Sending text to {} from {}".format(other_number, self.number))
        print(msg)

    def open_app(self, app_name):
        print("Opening {} on device".format(app_name))

class IPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None
    
    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == None and self.fingerprint == None):
            print("Phone is unlocked because no fingerprint is currently set")
        if (fingerprint == self.fingerprint):
            print("Phone is unlocked")
        else: 
            print("Phone locked. Fingerprint does not match")

another_iphone = IPhone(1234567890)
print("The number of the iphone is {}".format(another_iphone.number))

another_iphone.set_fingerprint("password")

print(another_iphone.fingerprint)

another_iphone.unlock("password123")
another_iphone.unlock("password")

another_iphone.call(4692940693)

another_iphone.open_app("Instagram")


class Android(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.keyboard = "Default"

    def __str__(self):
        return "This phone is owned by {}".format(self.number)

    def set_keyboard(self, new_keyboard):
        self.keyboard = new_keyboard

Android.ORIGIN = Android()
josh_phone = Android(4859285734)
josh_phone.set_keyboard("Dvorak")
josh_phone.call(2495039682)
josh_phone.open_app("Google Play Store")

print(josh_phone)