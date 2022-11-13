# Generated by Django 3.2.8 on 2022-11-13 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20221112_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='is_paid',
            new_name='is_valid',
        ),
        migrations.AddField(
            model_name='seat',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seat',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Time'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Time'),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('is_paid', models.BooleanField(default=False)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]