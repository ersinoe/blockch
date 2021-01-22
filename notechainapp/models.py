from django.db import models
from django.contrib.auth.models import User
from hashlib import sha256

class Note(models.Model):

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.CharField(max_length=20, default="0000-00-00 00:00:00")
    is_protected = models.BooleanField(default=False)
    date_protected = models.CharField(max_length=20, default="0000-00-00 00:00:00")
    previous_hash_code = models.CharField(max_length=64, default="")
    hash_code = models.CharField(max_length=64, default="")
    nonce = models.IntegerField(default=0)

    def calculateHash(self):
        hash_string = str(self.owner.username) + " " + str(self.title) + " " + str(self.description) + " " + str(self.nonce)
        return sha256(hash_string.encode("utf-8")).hexdigest()

    def mineNote(self, difficulty):
        while not str(self.hash_code).startswith("0"*difficulty):
            self.nonce += 1
            self.hash_code = self.calculateHash()

    def __str__(self):
        return str(self.title) + " created by " + str(self.owner) + " at " + str(self.date_created)


