from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    book_author = models.CharField(max_length=75)
    image = models.ImageField(default='default.jpg', upload_to='products_pics')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    ALL = "ALL"
    CLASSIC = "CLS"
    CRIME_AND_DETECTIVE = "CAD"
    DRAMA = "DRA"
    ROMANCE = "RMC"
    HORROR = "HRR"
    WARCRAFT = "WRC"
    CATEGORY_CHOICES = (
        (ALL, "All"),
        (CLASSIC, "Classic"),
        (CRIME_AND_DETECTIVE, "Crime and Detective"),
        (DRAMA, "Drama"),
        (ROMANCE, "Romance"),
        (HORROR, "Horror"),
        (WARCRAFT, "Warcraft")
    )
    name = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=ALL)

    def __str__(self):
        return self.name
