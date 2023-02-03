from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Sentiment(TextChoices):
    POSTIVE = "POS", _("Positive")
    NEGATIVE = "NEG", _("Negative")
    NEUTRAL = "NEU", _("Neutral")
