# Generated by Django 5.1.5 on 2025-02-27 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='point',
            name='type_p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='points.typeofpoint'),
        ),
    ]
