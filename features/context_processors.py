from .models import Snippet
def header_snippets(request):
    snippet = Snippet.objects.all()[0]
    context = {
        'snippet': snippet,
    }
    return context
