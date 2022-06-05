from typing import Literal, Optional, Union

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from vallery.collection.models import Nft


class CreateNft(LoginRequiredMixin, CreateView):
    model = Nft
    template_name = "collection/create_nft.html"
    fields: Optional[Union[list[str], Literal["__all__"]]] = [
        "name",
        "description",
        "image",
        "collection",
        "price",
        "bid_duration",
        "minimum_bid",
    ]
    success_url: Optional[str] = "/collection/"

    def form_valid(self, form: any) -> any:
        form = form.save(commit=False)
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form: any) -> any:
        return super().form_invalid(form)


class ListNFTs(ListView):
    model = Nft
    template_name = "collection/list_nfts.html"
    context_object_name: Optional[str] = "nfts"
    paginate_by: int = 6


class NftDetails(DetailView):
    model = Nft
    template_name = "collection/nft_details.html"
    context_object_name: Optional[str] = "nft"


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Nft
    template_name = "collection/delete_nft.html"
    success_url: Optional[str] = "/collection/"
