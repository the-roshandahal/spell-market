from .models import Snippet
def header_snippets(request):
    if Snippet.objects.exists():
        snippet = Snippet.objects.all()[0]
    else:
        snippet = None
    context = {
        'snippet': snippet,
    }
    return context
