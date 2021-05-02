from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField,EmailField
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for unguaAlert."""

    #: First and last name do not cover name patterns around the globe
    choice_gender = [('male',0),('female',1)]
    name = CharField(_("Name of User"), blank=True, max_length=255)
    gender = IntegerField(choices = choice_gender)
    state = CharField( max_length=15)
    lga = CharField(max_length=10)
    zone = IntegerField(help_text = "You can search your zone for your state in google")
    phone = PhoneNumberField()
    email = EmailField( max_length=100)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
