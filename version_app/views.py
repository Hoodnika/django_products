from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.forms import VersionForm
from users.views import CustomLoginRequiredMixin
from version_app.models import Version


def control(request):
    context = {

    }
    return render(request, 'future_new_base_for_version.html', context)


class VersionListView(ListView):
    model = Version


class VersionCreateView(CustomLoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('version:version_list')
    permission_denied_message = 'Доступ запрещен для неавторизованных пользователей'


class VersionDetailView(DetailView):
    model = Version


class VersionUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('version:version_detail', kwargs={'pk': self.object.pk})


class VersionDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('version:version_list')
