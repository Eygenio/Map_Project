# map_app/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.http import JsonResponse
from django import forms
from .models import Place, Image


class ImageForm(forms.ModelForm):
    """Форма для модели Image со всеми полями"""

    class Meta:
        model = Image
        fields = "__all__"


class ImageInline(admin.TabularInline):
    """Inline форма для отображения изображений внутри формы места"""

    model = Image
    form = ImageForm
    extra = 0
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        """Генерирует HTML для превью изображения в админке"""

        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    image_preview.short_description = "Превью"

    class Media:
        """Подключение JavaScript и CSS для Drag & Drop сортировки"""

        js = (
            "https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js",
            "admin/js/image_sortable.js",
        )
        css = {"all": ("admin/css/image_sortable.css",)}


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Админка для модели Place с кастомными настройками"""

    list_display = ["title", "lng", "lat"]
    list_filter = ["title"]
    search_fields = ["title", "description_short"]
    inlines = [ImageInline]
    fieldsets = [
        (None, {"fields": ["title", "description_short", "description_long"]}),
        ("Координаты", {"fields": ["lng", "lat"]}),
    ]

    def get_urls(self):
        """Добавление кастомных URL для обработки сортировки"""

        urls = super().get_urls()
        custom_urls = [
            path(
                "update_image_order/",
                self.update_image_order,
                name="update_image_order",
            ),
        ]
        return custom_urls + urls

    def update_image_order(self, request):
        """Обработчик AJAX запроса для обновления порядка изображений"""

        if request.method == "POST":
            order_data = request.POST.getlist("order[]")
            for index, image_id in enumerate(order_data):
                Image.objects.filter(id=image_id).update(position=index)
            return JsonResponse({"status": "success"})
        return JsonResponse({"status": "error"})


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Админка для модели Image с превью изображений"""

    list_display = ["place", "position", "image_preview"]
    list_editable = ["position"]
    list_filter = ["place"]
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        """Генерирует HTML для превью изображения увеличенного размера"""

        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    image_preview.short_description = "Превью"
