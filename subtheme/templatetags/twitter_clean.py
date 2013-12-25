from django import template

register = template.Library()

@register.simple_tag()
def httpsize(twitter_url):
    try:
        if not twitter_url.index('http:'):
            twitter_url_https = twitter_url[:4] + 's' + twitter_url[4:]
            return twitter_url_https
        else:
            raise ValueError
    except ValueError:
        return twitter_url