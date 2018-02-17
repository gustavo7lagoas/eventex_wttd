from django.contrib import admin

from eventex.core.models import Speaker


class SpeakerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'speaker_img', 'website_link')
    prepopulated_fields = {'slug': ('name',)}

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'Website'

    def speaker_img(self, obj):
        return '<img src="{}" width="32px" />'.format(obj.photo)

    speaker_img.allow_tags = True
    speaker_img.short_description = 'Foto'

admin.site.register(Speaker, SpeakerModelAdmin)

