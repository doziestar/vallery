from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from vallery.utils.block import generate_blockchain_address

User = get_user_model()


class Collection(models.Model):
    """Nft collections"""

    id = models.CharField(max_length=32, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nfts = models.ManyToManyField("Nft", blank=True)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number_of_nfts = models.IntegerField(default=0)
    image = models.ImageField(upload_to="collections", blank=True)

    def get_absolute_url(self):
        return reverse("collections:details", kwargs={"pk": self.pk})

    def generate_id(self):
        id, _ = generate_blockchain_address()
        self.id = id

    def __str__(self) -> str:
        return self.name


class Nft(models.Model):
    """Nft models"""

    id = models.CharField(
        max_length=32, primary_key=True, unique=True
    )  # blockchain address
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="nfts", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    is_bought = models.BooleanField(default=False)
    is_collected = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    bid_duration = models.DurationField(default=0)
    minimum_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def generate_id(self):
        id, _ = generate_blockchain_address()
        self.id = id

    def get_absolute_url(self):
        return reverse("nft:details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
