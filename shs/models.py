from django.db import models


class fertilizer(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='Biofertilizer id')
    name = models.CharField(max_length=80, verbose_name='BioFertilizer Name')
    cost = models.CharField(max_length=80, verbose_name='Cost of Fertizers')

    def __str__(self):
        return self.name


class Biopesticide(models.Model):
    id = models.BigAutoField(primary_key=True ,serialize=False,verbose_name='Biopesticide id' )
    name = models.CharField(max_length = 80, verbose_name='Biopesticide Name')
    cost = models.CharField(max_length = 80 , verbose_name = 'Cost of Biopersticde')

    def __str__(self):
        return self.name


class Herbicide(models.Model):
    id = models.BigAutoField(primary_key=True  ,serialize=False,verbose_name='Herbicide id' )
    name = models.CharField(max_length = 80, verbose_name='Herbicide Name')
    cost = models.CharField(max_length = 80 , verbose_name = 'Cost of Herbicide')
    
    def __str__(self):
        return self.name



class crop(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='crop id')
    name = models.CharField(max_length=80, verbose_name='Crop Name')
    disc = models.CharField(max_length=200, verbose_name='Description')
    fertilizer = models.ForeignKey(fertilizer, verbose_name='Fertilizer', on_delete=models.CASCADE, related_name='fertilizer_crops', null= True,blank=True)
    Biopesticide = models.ForeignKey(Biopesticide, verbose_name='Biopesticide', on_delete=models.CASCADE, related_name='biopesticide_crops' , null=True,blank=True)
    Herbicide = models.ForeignKey(Herbicide, verbose_name='Herbicide',  null=True, on_delete=models.CASCADE, related_name='herbicide_crops',blank=True)


    def __str__(self):
        return self.name

class Openprice(models.Model):
    id = models.BigAutoField(primary_key=True  ,serialize=False,verbose_name='Open Price id' )
    openprice = models.IntegerField( verbose_name = 'Open price')
    name = models.ForeignKey(crop, verbose_name='Crop', blank=True, null=True, on_delete=models.CASCADE, related_name='opencost_crops')


class Govprice(models.Model):
    id = models.BigAutoField(primary_key=True ,serialize=False,verbose_name='Gov Price id' )
    openprice = models.IntegerField( verbose_name = 'Gov price')
    name = models.ForeignKey(crop, verbose_name='Crop name', blank=True, null=True, on_delete=models.CASCADE, related_name='govprice_crops')


class states(models.Model):
    id = models.BigAutoField(primary_key=True ,serialize=False,verbose_name='state id' )
    name = models.CharField(max_length = 80, verbose_name='State Name', blank= True , null = True)
    
    crop_id = models.ManyToManyField(crop)

    def __str__(self):
        return self.name

