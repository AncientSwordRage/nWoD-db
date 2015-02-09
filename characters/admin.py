from django.contrib import admin
from django.contrib.contenttypes import admin as genericAdmin
from .models import CharacterAttributeLink, CharacterSkillLink, BookReference
from .mage.models import Mage, Spell, Arcana, CharacterArcanumLink, SpellArcanumLink, SpellAttributeLink, SpellSkillLink

class AttributeInline(genericAdmin.GenericTabularInline):
    model = CharacterAttributeLink
    extra = 9
    max_num = 9
    can_delete = False

class SkillInline(genericAdmin.GenericTabularInline):
    model = CharacterSkillLink
    extra = 24
    max_num = 24
    can_delete = False

class ExtraAttributeInline(admin.StackedInline):
    model = SpellAttributeLink
    extra = 1
    can_delete = False

class ExtraSkillInline(admin.StackedInline):
    model = SpellSkillLink
    extra = 1
    can_delete = False

class ArcanaInline(admin.TabularInline):
    model = CharacterArcanumLink

class ExtraSpellArcanaInline(admin.TabularInline):
    model = SpellArcanumLink
    extra = 1

class BookReferenceInline(genericAdmin.GenericStackedInline):
    model = BookReference
    max_num = 1

class SpellInline(admin.TabularInline):
    model = Spell.mage.through  
    
class MageAdmin(admin.ModelAdmin):
    inlines = [AttributeInline, SkillInline, ArcanaInline, SpellInline]

class SpellAdmin(admin.ModelAdmin):
    inlines = [ExtraAttributeInline, ExtraSkillInline, ExtraSpellArcanaInline, BookReferenceInline]

# Register your models here.
admin.site.register(Mage, MageAdmin)
admin.site.register(Arcana)
admin.site.register(Spell, SpellAdmin)
