from mezzanine.forms.page_processors import form_processor
from mezzanine.pages.page_processors import processor_for
from .models import ContactLandingPage

@processor_for(ContactLandingPage)
def contactlandingpage_form(request, page):
    """
    Use mezzanine builtin form_processor & processor for handling forms.
    """
    return form_processor(request, page.contactlandingpage.contact_form)
