from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DatasetsConfig(AppConfig):
    name = "app.datasets"
    verbose_name = _("Datasets")
