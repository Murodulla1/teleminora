from django.db import models


class Telebashniya1(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    images = models.ImageField()

    def __str__(self):
        return self.title


class Foydalanuvchi(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(max_length=250)
    number = models.IntegerField()
    manzili = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Galereya(models.Model):
    name = models.CharField(max_length=250, blank=True, null=False)
    img_abaut = models.TextField(blank=False, null=False)
    text_abaot = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.img_abaut


class Restourant(models.Model):
    name = models.CharField(max_length=240, blank=False, null=False)
    telefon_raqam = models.IntegerField()
    odamlar_soni = models.TextField(blank=False, null=False)
    sana = models.DateField()


    def __str__(self):
        return self.telefon_raqam

class Foods(models.Model):
    foods = models.TextField(blank=False, null=False)
    Ichimliklar = models.TextField(blank=False, null=False)
    salatlar = models.TextField(blank=False, null=False)
    shirinliklar = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.foods


