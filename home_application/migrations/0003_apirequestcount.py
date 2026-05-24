# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home_application", "0002_backuprecord"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApiRequestCount",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("api_category", models.CharField(max_length=255, verbose_name="API category")),
                ("api_name", models.CharField(max_length=255, verbose_name="API name")),
                ("request_count", models.IntegerField(default=0, verbose_name="request count")),
            ],
            options={
                "verbose_name": "API request count",
                "verbose_name_plural": "API request counts",
                "unique_together": {("api_category", "api_name")},
            },
        ),
    ]
