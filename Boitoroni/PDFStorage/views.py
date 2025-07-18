from django.http import HttpResponse
from django.template import loader
from .models import PDFs

def PDFStorage(request):
  mypdfs = PDFs.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mypdfs': mypdfs,
  }
  return HttpResponse(template.render(context, request))