from rest_framework.filters import SearchFilter
from django.contrib.postgres.search import SearchQuery


class FullSearchFilter(SearchFilter):

    def filter_queryset(self, request, queryset, view):
        search_terms = self.get_search_terms(request)
        if search_terms:
            query = "|".join(search_terms)
            search_query = SearchQuery(query, search_type='raw', config='english')
            return queryset.filter(search_vector=search_query)
        return queryset
