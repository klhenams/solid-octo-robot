# Generated by Django 4.0.8 on 2023-02-05 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0003_alter_tag_options_alter_tag_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator('csv', 'xls', 'xlsx')])),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
