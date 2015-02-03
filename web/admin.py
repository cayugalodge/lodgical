from django.contrib import admin
from models import NewsArticle, About, Contact, Alumni, Moseyer, MoseyEvent, MoseyerComment

class CommentInline(admin.StackedInline):
    model = MoseyerComment
    extra = 1

class MoseyerAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(NewsArticle)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Alumni)
admin.site.register(Moseyer, MoseyerAdmin)
admin.site.register(MoseyEvent)