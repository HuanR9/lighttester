import requests
from core import method

urladd = 'https://xc.test.17zuoye.net/educational_admin/create_teacher'
data = {
    "name":"test",
    "phone":"18000000092"
}
a = method.Loginxc().post(url=urladd,data=data)
print(a.text)
