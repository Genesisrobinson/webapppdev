# Generated by Django 2.0.7 on 2018-08-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='endpointavgtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=300)),
                ('time', models.FloatField(default=0.0)),
            ],
        ),
    ]
