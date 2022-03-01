from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad
from ads.serializers import CategorySerializer, AdSerializer


def index(request):

    return JsonResponse({"status": "ok"})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def list(self, request, *args, **kwargs):
        cat = request.GET.getlist("cat", None)
        text = request.GET.get("text", None)
        location = request.GET.get("location", None)
        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_to", None)

        cat_q = None
        for cat_id in cat:
            if not cat_q:
                cat_q = Q(category=cat_id)
            else:
                cat_q |= Q(category=cat_id)
        if cat_q:
            self.queryset = self.queryset.filter(cat_q)

        if text:
            self.queryset = self.queryset.filter(name__contains=text)
        if location:
            self.queryset = self.queryset.filter(user__locations__name__icontains=location)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "user_id": self.object.user_id,
            "image": self.object.image.url,
        })
