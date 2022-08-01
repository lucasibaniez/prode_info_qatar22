# Generated by Django 4.0.6 on 2022-08-01 22:18

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
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_grupos', to=settings.AUTH_USER_MODEL)),
                ('participantes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'grupos',
            },
        ),
    ]
