from django.http import HttpResponse
from models import paper

def show_paper(requests):
  key = requests.path.split("/")[-1]
  content = paper.objects.filter(key=key).values("content")
  if content:
      content = content[0]["content"]
  else:
      content = "No Found"
  return HttpResponse(content)

def index(requests):
  html = '''
  '''
  return HttpResponse(html)