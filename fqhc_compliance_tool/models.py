import os
from django.db import models
from django.conf import settings
from .choices import CREDENTIALS
from multiselectfield import MultiSelectField
from s3direct.fields import S3DirectField


class TimeStampedModel(models.Model):
    """An abstract base class model that provides
    fields `created` and `modified`"""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FQHC(TimeStampedModel):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.name)

class UserProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    full_name = models.CharField(max_length=100)
    fqhc = models.ForeignKey(FQHC)
    # http://www.centracare.com/providers/definitions-of-health-care-provider-credentials/
    credentials = MultiSelectField(
        choices=CREDENTIALS, default=["None"])


class Requirement(TimeStampedModel):
    step = models.IntegerField(unique=True)
    name = models.CharField(max_length=500)
    text = models.TextField()

    class Meta:
        ordering = ['step']

    def __str__(self):
        return 'Req '+str(self.step)+': '+str(self.name)


class SubRequirement(TimeStampedModel):
    requirement = models.ForeignKey(Requirement)
    step = models.IntegerField()
    name = models.CharField(max_length=500)
    text = models.TextField()

    class Meta:
        order_with_respect_to = 'requirement'

    def __str__(self):
        return 'SubReq '+str(self.step)+': '+str(self.name)


class Response(TimeStampedModel):
    fqhc = models.ForeignKey(FQHC)
    subrequirement = models.ForeignKey(SubRequirement)
    response = models.NullBooleanField()
    pdf = S3DirectField(dest=os.environ.get('AWS_STORAGE_BUCKET_NAME'))
    expiration = models.DateField()
    signed = models.DateField()
