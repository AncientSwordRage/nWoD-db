from django.db import models
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

def modify_fields(**kwargs):
    def wrap(cls):
        for field, prop_dict in list(kwargs.items()):
            for prop, val in list(prop_dict.items()):
                setattr(cls._meta.get_field(field), prop, val)
        return cls
    return wrap

def modify_verbose(name_dict):
    def wrap(cls):
        for field, val in list(name_dict.items()):
            setattr(cls._meta.get_field(field), 'verbose_name', val)
        return cls
    return wrap

def modify_choices(name_dict):
    def wrap(cls):
        for field, val in list(name_dict.items()):
            setattr(cls._meta.get_field(field), 'choices', val)
        return cls
    return wrap
