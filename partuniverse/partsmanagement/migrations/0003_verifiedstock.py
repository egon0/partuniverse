# Generated by Django 2.1.1 on 2018-09-06 18:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("partsmanagement", "0002_auto_20180817_1801"),
    ]

    operations = [
        migrations.CreateModel(
            name="VerifiedStock",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=4,
                        help_text="The quantity at this very time.",
                        max_digits=10,
                        verbose_name="Amount",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        db_index=True,
                        default=datetime.datetime.now,
                        help_text="The date the verifiedcation was created.",
                        verbose_name="Verfication Date",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user which verified the stock.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "storage_item",
                    models.ForeignKey(
                        help_text="The part-storage relation the the stock was verified.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="partsmanagement.StorageItem",
                    ),
                ),
            ],
        )
    ]