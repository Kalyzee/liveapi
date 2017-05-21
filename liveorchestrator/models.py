"""Import used for key generation (Event Model)
"""
import random
import string

from django.db import models
from django.utils import timezone

from django.utils.encoding import python_2_unicode_compatible


EVENT_KEY_RANDOM_COUNT = 30

@python_2_unicode_compatible
class Event(models.Model):
    """Event model represent a Live Channel or a Live Event, difference
    beetween them is simply the existance or not of a defined period.

    - Live Channel HAS no defined period
    - Live Event Has a defined period

    A period can be definied with begin (DateTimeField) and end (DateTimeField)
    attributes

    This model give you also possibilites to describe your live / channel event
    by setting a __name__ (CharField max=255) and a __description__ (TextField)

    A Live Channel is attributed to 2 Transcoder Service (One main transcoder
    and a fallback transcoder) and a set of Live Services.

    This event also contain live_key which is the key requested by live server
    to validate authenticity of the user who is publishing stream.

    """

    """This is simply Event / Channel name
    """
    name = models.CharField(max_length=255, null=True)

    """This is simply Event / Channel Description
    """
    description = models.CharField(max_length=255, null=True)

    """This is simply Event / Channel owner
    """
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)


    # Event Token

    """This is simply Event / Channel Description
    """
    key = models.CharField(max_length=255)

    """ Event end datetime, if null, this event is considered like
    a channel, in other words generated url is always available until
    a end date is defined OR deleted_at date is given.
    """
    begin = models.DateTimeField()

    """ Event end datetime, if null, this event is considered like
    a channel, in other words generated url is always available until
    a end date is defined OR deleted_at date is given.
    """
    end   = models.DateTimeField(null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


    def regenerate_key(self):
        """key regeneration
        """
        self.key = ''.join(
                    random.sample(string.ascii_lowercase + string.digits, EVENT_KEY_RANDOM_COUNT)
                )

    def save(self, *args, **kwargs):
        if (self.pk is None):
            self.regenerate_key()
            if (self.begin is None):
                self.begin = timezone.now()
        super(Event, self).save(*args,**kwargs)

    def __str__(self):
        return '%s (%s)' % (self.name, self.iso)
