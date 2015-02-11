from django.contrib import admin
from django.contrib.contenttypes import admin as generic_admin
from .models import CharacterAttributeLink, CharacterSkillLink, BookReference, SkillAbility, AttributeAbility
from .mage.models import Mage, Spell, ArcanumAbility, CharacterArcanumLink, SpellArcanumLink, SpellAttributeLink, SpellSkillLink


class AttributeInline(generic_admin.GenericTabularInline):
    model = CharacterAttributeLink
    extra = 9
    max_num = 9
    can_delete = False


class SkillInline(generic_admin.GenericTabularInline):
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
    extra = 10
    max_num = 10


class ExtraSpellArcanaInline(admin.TabularInline):
    model = SpellArcanumLink
    extra = 1


class BookReferenceInline(generic_admin.GenericStackedInline):
    model = BookReference
    max_num = 1


class SpellInline(admin.TabularInline):
    model = Spell.mage.through


class MageAdmin(admin.ModelAdmin):
    inlines = [ArcanaInline, SkillInline, AttributeInline]


class SpellAdmin(admin.ModelAdmin):
    inlines = [ExtraAttributeInline, ExtraSkillInline,
               ExtraSpellArcanaInline, BookReferenceInline]

# Register your models here.
admin.site.register(Mage, MageAdmin)
admin.site.register(ArcanumAbility)
admin.site.register(Spell, SpellAdmin)
admin.site.register(SkillAbility)
admin.site.register(AttributeAbility)
