# coding=utf-8
from django import template

register = template.Library()


@register.simple_tag
def admin_edit(object):
    object_app = object._meta.app_label
    object_model = object._meta.module_name
    object_id = str(object.id)
    result_link = '/admin/'+object_app+'/'+object_model+'/'+object_id+'/'
    return result_link
