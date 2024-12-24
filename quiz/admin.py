from django.contrib import admin
from . import models

# Base Custom Admin class for common functionality
class CustomAdmin(admin.ModelAdmin):
    actions = ['activate', 'deactivate']
    list_filter = ('status',)
    list_per_page = 10
    date_hierarchy = "date_add"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activée avec succès.')
    activate.short_description = "Activer les éléments sélectionnés"

    def deactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivée avec succès.')
    deactivate.short_description = "Désactiver les éléments sélectionnés"

# Question Admin
class QuestionAdmin(CustomAdmin):
    list_display = ('typequestion', 'point')
    list_display_links = ('typequestion',)
    search_fields = ('typequestion',)
    fieldsets = [
        ("Info Question", {"fields": ["typequestion", "point", "quiz", "question"]}),
        ("Standard", {"fields": ["status"]}),
    ]

# Reponse Admin
class ReponseAdmin(CustomAdmin):
    list_display = ('reponse', 'question', 'is_True', 'status')
    list_display_links = ('reponse',)
    search_fields = ('reponse',)
    fieldsets = [
        ("Info Réponse", {"fields": ["reponse", "question", "is_True"]}),
        ("Standard", {"fields": ["status"]}),
    ]

# Quiz Admin
class QuizAdmin(CustomAdmin):
    list_display = ('date', 'titre', 'temps', 'status')
    list_display_links = ('titre',)
    search_fields = ('titre',)
    fieldsets = [
        ("Info Quiz", {"fields": ["date", "titre", "cours", "temps"]}),
        ("Standard", {"fields": ["status"]}),
    ]

# Devoir Admin
class DevoirAdmin(CustomAdmin):
    list_display = ('dateDebut', 'dateFermeture', 'chapitre', 'coefficient', 'support', 'status')
    list_display_links = ('chapitre',)
    search_fields = ('chapitre',)
    fieldsets = [
        ("Info Devoir", {"fields": ["dateDebut", "dateFermeture", "chapitre", "support"]}),
        ("Standard", {"fields": ["status"]}),
    ]

# Function to register models and their corresponding admin classes
def _register(model, admin_class):
    admin.site.register(model, admin_class)

# Register models with their custom admin classes
_register(models.Question, QuestionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.Quiz, QuizAdmin)
_register(models.Devoir, DevoirAdmin)
