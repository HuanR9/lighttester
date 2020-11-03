import requests


def Loginxc():
    url = "http://xcds.test.17zuoye.net/pc/index.html"

    session = requests.session()
    cookies = requests.cookies.RequestsCookieJar()
    cookies.set('xc_token', '0tCt6Zpj.4zuul+G3rj6l3RBaNlX8U/np1ksWxKYM')
    cookies.set('xc_auth','0tCt6Zpj.4zuul+G3rj6l3RBaNlX8U/np1ksWxKYM')
    session.cookies.update(cookies)
    return session