from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from .forms import GuestbookForm
from .models import Guestbook


class GuestbookView(ListView):
    model = Guestbook
    context_object_name = 'guestbook_entries'

class GuestbookCreateView(CreateView):
    model = Guestbook
    form_class = GuestbookForm
    context_object_name = 'guestbook_entry'
    success_url = reverse_lazy('guestbook:index')

class GuestbookDeleteView(DeleteView):
    model = Guestbook
    context_object_name = 'guestbook_entry'
    success_url = reverse_lazy('guestbook:index')
