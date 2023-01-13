import time
from django.db import models

class EpochField(models.BigIntegerField):
    null = False
    description = "Epoch with default value behavior for created/updated fields"

    def __init__(self, verbose_name=None, name=None, created_at=False, updated_at=False, **kwargs):
        self.created_at, self.updated_at = created_at, updated_at
        if created_at or updated_at:
            kwargs['editable'] = False
            kwargs['blank'] = True
        super(EpochField, self).__init__(verbose_name, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(EpochField, self).deconstruct()
        if self.created_at:
            kwargs['created_at'] = True
        if self.updated_at:
            kwargs['updated_at'] = True
        if self.created_at or self.updated_at:
            del kwargs['editable']
            del kwargs['blank']
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        if self.updated_at or (self.created_at and add):
            value = int(time.time())
        else:
            value = getattr(model_instance, self.attname)
        setattr(model_instance, self.attname, value)
        return value