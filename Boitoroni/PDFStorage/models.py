from django.db import models

class PDFs(models.Model):
  PDFname = models.CharField(max_length=255)
  Authorname = models.CharField(max_length=255)
  Genre = models.CharField(max_length=255)
  Price = models.IntegerField(default = 0)