# map_app/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django import forms
from .models import Place, Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class ImageInline(admin.TabularInline):
    model = Image
    form = ImageForm
    extra = 0
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                obj.image.url
            )
        return "Нет изображения"

    image_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']
    list_filter = ['title']
    search_fields = ['title', 'description_short']
    inlines = [ImageInline]
    fieldsets = [
        (None, {
            'fields': ['title', 'description_short', 'description_long']
        }),
        ('Координаты', {
            'fields': ['lng', 'lat']
        }),
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'position', 'image_preview']
    list_editable = ['position']
    list_filter = ['place']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.image.url
            )
        return "Нет изображения"

    image_preview.short_description = 'Превью'
