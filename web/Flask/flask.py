from flask import Flask, session
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # Override method
    # Take secret_key instead of an instance of a Flask app
    def get_signing_serializer(self, secret_key):
        if not secret_key:
            return None
        signer_kwargs = dict(
            key_derivation=self.key_derivation,
            digest_method=self.digest_method
        )
        return URLSafeTimedSerializer(secret_key, salt=self.salt,
                                      serializer=self.serializer,
                                      signer_kwargs=signer_kwargs)

def encodeFlaskCookie(secret_key, cookieDict):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.dumps(cookieDict)

if __name__=='__main__':
    sk = 'a7a8342f9b41fcb062b13dd1167785f8'


    sessionDict={
    "_fresh": True,
    "_id": "8cdf51a2bfcd6edd19afc1fec39b39462f94eaa6500d3940a59b988f3e1713305e34de06f51020b42b2e915f872196dba806e2e2ea42bc2cfe373d490a9a74ca",
    "csrf_token": "f1e8fea3cd6b80336a7469776b83b99498ad8f1a",
    "user_id": "1"

    cookie = encodeFlaskCookie(sk, sessionDict)
    print(cookie)
    
