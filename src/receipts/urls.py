from django.urls import path

from receipts import views

urlpatterns = [
    path("receipt_json/", views.receipt_json),
]
