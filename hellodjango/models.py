import uuid
from django.core import serializers
from django.db import models
from .fields import EpochField

class Shares(models.Model):
    by_user = models.BigIntegerField(null=False, editable=False)
    for_user = models.BigIntegerField(null=False, editable=False)
    original_url = models.URLField(max_length=5000, null=False, editable=False)
    created_at = EpochField(created_at=True, editable=False)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return serializers.serialize('json', [self], fields=('by_user', 'for_user', 'original_url', 'created_at', 'viewed'))

class ShareRequest(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requesting_user = models.BigIntegerField(null=False, editable=False)
    share_target_user = models.BigIntegerField(null=False, editable=False)
    target_accepted_at = models.BigIntegerField(null=True)
    target_rejected_at = models.BigIntegerField(null=True)
    created_at = EpochField(created_at=True, editable=False)

    def __str__(self):
        return serializers.serialize('json', [self], fields=('requesting_user', 'share_target_user', 'created_at'))
