# Generated by Django 2.2.2 on 2019-06-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0034_auto_20190627_1438")]

    operations = [
        migrations.AlterField(
            model_name="sitereport",
            name="created_on",
            field=models.DateTimeField(editable=False),
        )
    ]
