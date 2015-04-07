from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from .models import Room, Exit, Puzzle


class ExitInlineAdmin(admin.TabularInline):
    model = Exit
    fk_name = 'from_room'
    extra = 0
    fields = ('to_room', 'name', 'puzzle', 'edit')
    readonly_fields = ('puzzle', 'edit')

    def edit(self, instance):
        if instance.id:
            url = reverse('admin:%s_%s_change' % (instance._meta.app_label,
                instance._meta.module_name), args=(instance.id,))
            return format_html('<a href="{}">Edit -></a>', url)
        else:
            return format_html('(Save to Edit)')

class PuzzleInlineAdmin(admin.TabularInline):
    model = Puzzle
    extra = 0

class RoomAdmin(admin.ModelAdmin):
    list_display = ('key', 'display_title', 'number_of_exits', 'number_of_entrances')
    list_select_related = ('exits', 'entrances')

    inlines = [ExitInlineAdmin]

    def number_of_exits(self, instance):
        return instance.exits.count()

    def number_of_entrances(self, instance):
        return instance.entrances.count()


class ExitAdmin(admin.ModelAdmin):
    list_display = ('from_room', 'to_room', 'name')
    list_select_related = ('from_room', 'to_room')

    inlines = [PuzzleInlineAdmin]


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('name', 'hint', 'solution')



admin.site.register(Room, RoomAdmin)
admin.site.register(Exit, ExitAdmin)
admin.site.register(Puzzle, PuzzleAdmin)
