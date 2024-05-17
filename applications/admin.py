from django.contrib import admin
from .models import Articles
from django.contrib.auth.models import User
from django.urls import reverse
from . import views
from django.utils.html import format_html

class AppliAdmin(admin.ModelAdmin):
    model = User
    list_display = ('service', 'surname', 'address', 'date', 'status', 'export_buttons')
    ordering = ['-date']
    list_editable = ('status',)
    list_per_page = 10
    actions = ['set_done']

    @admin.action(description="Выполнить выбранные заявки")
    def set_done(self, request, queryset):
        count = queryset.update(status=Articles.Status.DONE)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Экспорт")
    def export_buttons(self, obj):
        Articles.id = obj.id
        word_url = reverse('appli-export', args=[Articles.id])
        excel_url = reverse('appli-export-excel', args=[Articles.id])
        return format_html(
            f'<a href="{word_url}"><button>Скачать Word</button></a>'
            f'<a href="{excel_url}"><button>Скачать Excel</button></a>'
        )


admin.site.register(Articles, AppliAdmin)
