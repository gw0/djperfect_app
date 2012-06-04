# -*- coding: utf-8 -*-
"""
Views for {{ app_name|title }} Django application.
"""
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

from {{ app_name }} import models


# Replace the following example with your views.

def home(req):
    """View for `home` page."""
    {{ app_name }} = get_object_or_404(models.{{ app_name|title }}, name='home')
    return render_to_response('{{ app_name }}/home.html', {
        '{{ app_name }}': {{ app_name }},
    })

