# coding=utf-8
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def admin_edit(db_record):
    return reverse('admin:%s_%s_change' % (db_record._meta.app_label,
                                           db_record._meta.module_name),
                   args=(db_record.id,))
