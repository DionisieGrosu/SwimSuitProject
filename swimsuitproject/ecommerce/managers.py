from django.db import models

class ProductManager(models.Manager):

    def active(self):
        return self.filter(active=True)



class OrderManager(models.Manager):

    def active(self):
        return self.filter(active=True)