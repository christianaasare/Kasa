# Generated by Django 2.2.4 on 2019-09-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='category',
            field=models.CharField(default='Select', max_length=250),
        ),
    ]
