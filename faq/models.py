from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali

    def save(self, *args, **kwargs):
        translator = Translator()

        # Auto-translate if not provided
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
            'en': self.question,
        }
        translation = translations.get(lang, self.question)
        cache.set(cache_key, translation, timeout=3600)  # Cache for 1 hour
        return translation

    def __str__(self):
        return self.question
