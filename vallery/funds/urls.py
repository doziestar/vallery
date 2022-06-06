from django.urls import path

from vallery.funds import views

app_name = "funds"
urlpatterns = [
    path("", views.home_view, name="payments-home"),
    path("success/", views.success_view, name="payments-success"),
    path("cancel/", views.cancel_view, name="payments-cancel"),
    path("webhook/", views.coinbase_webhook),
]
