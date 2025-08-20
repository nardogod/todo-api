from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # data de criação
    updated_at = models.DateTimeField(auto_now=True)      # data de atualização

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
