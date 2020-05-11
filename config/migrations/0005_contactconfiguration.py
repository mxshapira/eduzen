# Generated by Django 1.10.6 on 2017-05-27 21:42
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("config", "0004_bioconfiguration")]

    operations = [
        migrations.CreateModel(
            name="ContactConfiguration",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default=b"Contacto", max_length=255)),
                ("subtitle", models.CharField(blank=True, max_length=255, null=True)),
                ("body", ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={"verbose_name": "Contact configuration"},
        )
    ]
