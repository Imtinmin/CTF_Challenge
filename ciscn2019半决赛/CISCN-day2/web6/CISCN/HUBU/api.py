from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from models import paper
from selenium import webdriver
import re
import random
class check_admin(object):
    def process_request(self, request):
        if 'admin/ueditor/' in request.path:
             if not request.user.is_authenticated():
                return JsonResponse({'403': 'Your are Not Admin'})
				
def add_paper(requests):
    content = requests.POST.get("content")
    if not content:
       return JsonResponse({'error': 'No content type in, please check your input'})
    key = "".join([chr(random.randint(65,90)) for i in range(10)])
    if xss_check(content):
        return JsonResponse({'error': 'hackers, pls stop  try it!'})
    Paple = paper(content=content, key=key)
    Paple.save()
    return JsonResponse({'url': '/%s' % key})

def get_token_(requests):
    token = get_token(requests)
    return JsonResponse({'token': token})

def send_paper(requests):
    key = requests.POST.get('key')
    if not key:
        return JsonResponse({"error": "No key type in, please  check your input"})
    browser = webdriver.PhantomJS(executable_path = "/bin/phantomjs")
    browser.get("http://127.0.0.1:8000/admin/")
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    username.send_keys('HUBU2019')
    password.send_keys('MCy9Is1Hk8_aF91')
    submit = browser.find_element_by_xpath("//*[@type='submit']")
    submit.click()
    browser.get("http://127.0.0.1:8000/%s" % key)
    print browser.page_source
    return JsonResponse({'success': 'Your paper is very good!'})

def  xss_check(content):
    pattern = re.compile('(<script)|(on[a-zA-Z]*=)|(javascript:)|')
    return False