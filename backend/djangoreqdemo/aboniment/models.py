import django.core
import django.db.models
import django.contrib.auth


class Aboniment(
    django.db.models.Model,
):
    owner = django.db.models.ForeignKey(
        django.contrib.auth.get_user_model(),
        verbose_name="Владелец",
        on_delete=django.db.models.CASCADE,
        related_name="owner",
        related_query_name="aboniment_owner",
        default=None,
        help_text="Назначьте владельца",
    )
    
    title = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
        unique=True,
    )

    duration = django.db.models.PositiveIntegerField(
        "длительность ",
        default=0,
        help_text="срок действия в месяцах",
    )

    created = django.db.models.DateTimeField(
        "дата создания",
        auto_now_add=True,
        null=True,
    )

    updated = django.db.models.DateTimeField(
        "дата изменения",
        auto_now=True,
        null=True,
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "питательное вещество"
        verbose_name_plural = "питательные вещества"

    def __str__(self):
        return self.title
