from django.db import models
from django.contrib.auth.models import User
from hashlib import sha256
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peers = models.ManyToManyField("Profile", related_name="network", symmetrical=False)
    secret_key = models.CharField(max_length=64, default="")
    secret_passcode = models.CharField(max_length=100, default="")
    trid = models.CharField(max_length=11, default="00000000000")
    father_name = models.CharField(max_length=50, default="")
    birth_date = models.CharField(max_length=10, default="")
    image = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return str(self.user.username) + "'s Profile"

    def generate_secret_key(self):
        hash_string = str(self.trid) + str(self.father_name) + str(self.birth_date)
        self.secret_key = sha256(hash_string.encode("utf-8")).hexdigest()
        self.secret_passcode = self.user.password

    def save(self, *args, **kwargs):
        self.generate_secret_key()
        super().save(*args, **kwargs)

        profile = Profile.objects.first()
        self.peers.add(profile)

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')
