from django.db import models

class Tarefa(models.Model):
    PRIORIDADES = [
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
    ]

    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADES,
        default="media",
    )
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
