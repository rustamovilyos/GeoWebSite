from django.db import models

from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    capital = models.CharField(max_length=50, null=True, blank=True)  # poytaxti
    internal_division = models.CharField(max_length=300, null=True, blank=True)  # ichki bo'linishi
    square = models.FloatField(null=True, blank=True)
    climate = models.CharField(max_length=200, null=True, blank=True)  # havosi
    official_language = models.CharField(max_length=100, null=True, blank=True)
    population = models.FloatField(null=True, blank=True)  # aholisi
    religion = models.CharField(max_length=50, null=True, blank=True)  # dini
    phone_code = models.CharField(max_length=5, null=True, blank=True)
    flag = models.ImageField(null=True, blank=True)
    coat_of_arms = models.ImageField(null=True, blank=True)  # gerbi
    currency = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Rivers(models.Model):
    title = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    river_length = models.FloatField(max_length=5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Река'
        verbose_name_plural = 'Реки'


class Oceans(models.Model):
    title = models.CharField(max_length=30)
    square = models.FloatField()
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Океан'
        verbose_name_plural = 'Океаны'


class Mountains(models.Model):
    title = models.CharField(max_length=25)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    mountain_height = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гора'
        verbose_name_plural = 'Горы'
