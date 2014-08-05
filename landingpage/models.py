from django.db import models
from mezzanine.forms.models import Form
from mezzanine.pages.models import Page, RichText
from portfolio.models import PortfolioItem


class ContactLandingPage(Page, RichText):
    """
    Landng Page Model
    """
    tracking_code = models.TextField(verbose_name="Tracking Code Snippet.")
    contact_form = models.ForeignKey(Form, verbose_name="Contact Form.")
    portfolio_item = models.ManyToManyField(PortfolioItem, null=True, verbose_name="Portfolio Item")
    # TODO Set clean to stop anything over 3.