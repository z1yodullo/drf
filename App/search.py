from django.db.models import Q

def search_filter(queryset, params):

    query = params.get('search')
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return queryset
