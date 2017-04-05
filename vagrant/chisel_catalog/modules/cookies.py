#SECURITY
import hashlib
import hmac
import re

SECRET = 'imsosecret'

#Hash
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()
#Make Secure Cookie
def make_secure_val(uid):
    return "%s|%s" % (uid, hash_str(uid))
#Check Cookie
def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

# Create uid cookie on login
def create_uid_cookie(self, user_id):
    self.response.set_cookie(
                    'uid', make_secure_val(user_id))

# Delete uid cookie on logout
def delete_uid_cookie(self):
    self.response.set_cookie('uid', None)

# Get user from uid cookie
def user_from_cookie(self):
    uid_cookie = self.request.cookies.get('uid', '')
    if uid_cookie and security.check_secure_val(uid_cookie):
        uid = uid_cookie.split('|')[0]
        return uid