from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Admission


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'class_name',
        'gender',
        'mobile',
        'created_at',
        'pdf_button',
    )

    list_filter = ('class_name', 'gender', 'created_at')
    search_fields = ('student_name', 'mobile')

    def pdf_button(self, obj):
        url = reverse('admission_pdf', args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank">Download PDF</a>',
            url
        )

    pdf_button.short_description = 'Admission PDF'