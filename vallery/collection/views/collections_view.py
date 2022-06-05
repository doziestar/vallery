from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from vallery.collection.models import Collection


class CollectionListView(ListView):
    model = Collection
    template_name = "collection/collection_list.html"
    context_object_name: Optional[str] = "collections"
    paginate_by: int = 6

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["collections_count"] = Collection.objects.count()
        # get the number of nfts in all collections
        context["nfts_count"] = Collection.objects.aggregate(nfts_count=Count("nfts"))[
            "nfts_count"
        ]
        # get number of unique users who have created collections
        context["users_count"] = Collection.objects.aggregate(
            users_count=Count("user")
        )["users_count"]
        return context


class CollectionDetailView(DetailView):
    model = Collection
    template_name = "collection/collection_detail.html"
    context_object_name: Optional[str] = "collection"


class CreateCollection(LoginRequiredMixin, CreateView):
    model = Collection
    template_name = "collection/create_collection.html"
    fields = ["name", "description", "image"]

    def form_valid(self, form: any) -> any:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["collections_count"] = Collection.objects.count()
        return context


class UpdateCollections(LoginRequiredMixin, UpdateView):
    model = Collection
    template_name = "collection/update_collection.html"
    fields = ["name", "description", "image"]

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["collections_count"] = Collection.objects.count()
        return context


class DeleteCollections(LoginRequiredMixin, DeleteView):
    model = Collection
    template_name = "collection/delete_collection.html"

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["collections_count"] = Collection.objects.count()
        return context
