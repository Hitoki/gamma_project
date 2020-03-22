from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_pics')
    likes = models.IntegerField(verbose_name='like', default=0)
    dislikes = models.IntegerField(verbose_name='dislike', default=0)
    users_likes_list = models.ManyToManyField(User, related_name="userslikeslist", blank=True)
    epoch = models.ForeignKey("Epoch", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Epoch(models.Model):
    ALL = "ALL"
    ROMANESQUE = "RNSQ"
    GOTHIC = "GTC"
    RENAISSANCE = "RNSC"
    BAROQUE = "BRQ"
    ROCOCO = "RCC"
    CLASSICISM = "CLSM"
    ROMANTICISM = "RMCM"
    ECLECTICISM = "ELCM"
    MODERNISM = "MDRSM"
    EPOCH_CHOICES = (
        (ALL, "ALL"),
        (ROMANESQUE, "Romanesque"),
        (GOTHIC, "Gothic"),
        (RENAISSANCE, "Renaissance"),
        (BAROQUE, "Baroque"),
        (ROCOCO, "Rococo"),
        (CLASSICISM, "Classicism"),
        (ROMANTICISM, "Romanticism"),
        (ECLECTICISM, "Eclecticism"),
        (MODERNISM, "Modernism")
    )
    name = models.CharField(max_length=5, choices=EPOCH_CHOICES, default=ALL)
    data = models.DateTimeField()

    def __str__(self):
        return self.name
