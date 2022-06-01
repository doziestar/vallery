from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from vallery.utils.block import generate_blockchain_address


class User(AbstractUser):
    """
    Default custom user model for vallery.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    id: str = models.CharField(max_length=255, unique=True, primary_key=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def generate_address(self):
        """Generate a blockchain address for the user.

        Returns:
            str: A blockchain address.

        """
        return generate_blockchain_address()


class BlockChainAddress(models.Model):
    """Store User BlockChain Wallet"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    address = models.CharField(max_length=255, unique=True, primary_key=True)
    private_key = models.CharField(max_length=255, unique=True)

    def generate_address(self):
        """Generate a blockchain address for the user.

        Returns:
            str: A blockchain address.

        """
        self.address, self.private_key = self.generate_private_key()
        self.save()


class Profile(models.Model):
    """User Profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_purchase = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_sold = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    number_of_collections = models.IntegerField(default=0)
    number_of_available_collections = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username

    @property
    def sold(self):
        return self.total_sold

    @property
    def collections(self):
        return self.number_of_collections

    @property
    def available(self):
        return self.number_of_available_collections
