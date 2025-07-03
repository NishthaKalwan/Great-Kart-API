'''
    A context processor is a small function that automatically adds data to the context of all templates
    in your Django project, and you can use that context data in any HTML template
    it takes request and return dictionary of context data. so have to add his method into templates in settings.py
'''

from .models import Category

def menu_links(request):
    links= Category.objects.all()
    return dict(links=links)