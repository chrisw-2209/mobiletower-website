from django.db import models

class Site(models.Model):
    site_num = models.IntegerField()
    site_name = models.CharField(max_length=200)
    address_street = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    address_zip = models.IntegerField()
    address_county = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    height = models.FloatField()
    structure = models.CharField(max_length=200)
    frn_num = models.IntegerField()
    faa_study_num = models.CharField(max_length=200)

    def __str__(self):
        return self.site_name

class SitePhoto(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="tower_photos/")

    def __str__(self):
        return f"{self.site.site_name} photo"