from django.db import models
from django.utils import timezone
import datetime
import random
import string


class PostItem(models.Model):
    def magic_key(stringLength=6):
        magic_key = string.ascii_letters
        return ''.join(random.choice(magic_key) for i in range(stringLength))

    CHOICES = (
        ('roast', 'ROAST'),
        ('boast', 'BOAST'),
    )
    category_choice = models.CharField(
        choices=CHOICES,
        max_length=50
        )
    text = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0, editable=False)
    downvotes = models.IntegerField(default=0, editable=False)
    submission_time = models.DateTimeField(
        default=timezone.now,
        blank=True,
        editable=False
        )
    magic_key = models.CharField(
        max_length=6,
        editable=False,
        default=magic_key()
        )
    vote_score = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.category_choice
