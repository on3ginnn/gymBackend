# Generated by Django 4.2 on 2024-12-08 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Aboniment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="max 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="срок действия в месяцах",
                        verbose_name="длительность ",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="дата изменения"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        default=None,
                        help_text="Назначьте владельца",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        related_query_name="aboniment_owner",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "питательное вещество",
                "verbose_name_plural": "питательные вещества",
                "ordering": ("-created",),
            },
        ),
    ]