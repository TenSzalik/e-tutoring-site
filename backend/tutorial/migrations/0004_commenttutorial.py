# Generated by Django 4.1.7 on 2023-03-15 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0003_basestar_delete_basestars"),
        ("tutorial", "0003_tutorial_people"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentTutorial",
            fields=[
                (
                    "basecomment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="common.basecomment",
                    ),
                ),
                (
                    "tutorial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tutorial.tutorial",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("common.basecomment",),
        ),
    ]
