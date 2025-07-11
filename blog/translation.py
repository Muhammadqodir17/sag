from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, SocialMediaIcon


class BlogTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


class SocialMediaIconTranslationOptions(TranslationOptions):
    fields = ['name']


translator.register(Blog, BlogTranslationOptions)
translator.register(SocialMediaIcon, SocialMediaIconTranslationOptions)

