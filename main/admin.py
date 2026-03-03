from django.contrib import admin
from .models import About, Skill, Project

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Show these columns in the list view
    list_display = ('__str__', 'name', 'role', 'email')
    
    def has_add_permission(self, request):
        # If one exists, don't allow adding another
        return not About.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent accidental deletion of your settings
        return False

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'link_live', 'link_github')
    list_editable = ('display_order',)
