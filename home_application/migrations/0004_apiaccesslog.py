# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home_application", "0003_apirequestcount"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApiAccessLog",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("api_category", models.CharField(max_length=255, verbose_name="API category")),
                ("api_name", models.CharField(max_length=255, verbose_name="API name")),
                ("request_path", models.CharField(max_length=1024, verbose_name="request path")),
                ("request_method", models.CharField(max_length=16, verbose_name="request method")),
                ("username", models.CharField(blank=True, default="", max_length=64, verbose_name="username")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
            ],
            options={
                "verbose_name": "API access log",
                "verbose_name_plural": "API access logs",
            },
        ),
    ]
