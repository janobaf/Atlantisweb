# Generated by Django 3.2.19 on 2023-06-30 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Mesas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('platos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatoPedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('observacion', models.CharField(max_length=150, null=True)),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platos.platos')),
            ],
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('precio_total', models.FloatField(blank=True, default=0, null=True)),
                ('mesa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Mesas.mesa')),
                ('plato', models.ManyToManyField(blank=True, to='pedidos.PlatoPedidos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
