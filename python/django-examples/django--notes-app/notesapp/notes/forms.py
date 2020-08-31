from django.forms import Form, ChoiceField, CharField, DateField


class SearchForm(Form):
    SEARCH_BY = (("includes", "includes"), ("starts with", "starts with"), ("exact match", "exact match"))
    title = CharField(label="Note title")
    title_search_by = ChoiceField(label="Search title by", choices=SEARCH_BY, initial="includes")
    body = CharField(label="Note body")
    body_search_by = ChoiceField(label="Search body by", choices=SEARCH_BY, initial="includes")
    time = DateField(label="date published")
