# Generated by Django 2.1.1 on 2018-09-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("partsmanagement", "0003_verifiedstock")]

    operations = [
        migrations.AddField(
            model_name="verifiedstock",
            name="comment",
            field=models.TextField(
                blank=True,
                help_text="A short conclusion.",
                max_length=200,
                null=True,
                verbose_name="Comment",
            ),
        )
    ]
