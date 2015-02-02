from django.contrib import admin
from django import forms
from .models import Mage, Spell, Skill, Attribute, Arcana


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 9
    max_num = 9
    can_delete = False

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 24
    max_num = 24
    can_delete = False

class ArcanaInline(admin.TabularInline):
    model = Arcana

class SpellInline(admin.TabularInline):
    model = Spell.mage.through  
    
class MageAdmin(admin.ModelAdmin):
    inlines = [AttributeInline, SkillInline, ArcanaInline, SpellInline]

class SpellAdmin(admin.ModelAdmin):
    secondary_arcana = forms.ModelMultipleChoiceField(queryset=Arcana.objects.all(), required=False)
    optional_arcana = forms.ModelMultipleChoiceField(queryset=Arcana.objects.all(), required=False)
    class Meta:
        model = Spell
        fields = ('name', 'vulgar', 'primary_arcana', 'secondary_arcana', 'optional_arcana', 'rote_skill',
            'rote_attribute', 'mage', 'contested', 'contested_attribute', 'contested_skill', 'resisted',
            'resisted_by_attribute')

# Register your models here.
admin.site.register(Mage, MageAdmin)
admin.site.register(Skill)
admin.site.register(Attribute)
admin.site.register(Arcana)
admin.site.register(Spell, SpellAdmin)
