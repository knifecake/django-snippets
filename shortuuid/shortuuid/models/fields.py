import base58
import uuid
from django.db import models


def _gen_short_uuid():
    return base58.b58encode(uuid.uuid4().bytes).decode('ascii').zfill(22)


class ShortUUIDField(models.CharField):
    """
    A base58-encoded uuid4 as the primary key.

    Generated IDs are 22 characters long and suitable for URLs.

    The likelihood of a collision is effectively zero, so this field doesn't
    check for them. Keep this in mind if you decide to shorten the length of the
    field, which might increase the likelihood and break this assumption.
    """

    def __init__(self, *args, **kwargs):
        defaults = {
            'max_length': 22,
            'verbose_name': 'ID',
            'editable': False,
            'default': _gen_short_uuid,
        }
        defaults.update(kwargs)

        return super().__init__(*args, **defaults)
