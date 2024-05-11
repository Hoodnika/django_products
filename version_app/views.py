from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.forms import VersionForm
from version_app.models import Version


def control(request):
    context = {

    }
    return render(request, 'future_new_base_for_version.html', context)


class VersionListView(ListView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('version:version_list')


class VersionDetailView(DetailView):
    model = Version


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('version:version_detail', kwargs={'pk': self.object.pk})


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('version:version_list')
