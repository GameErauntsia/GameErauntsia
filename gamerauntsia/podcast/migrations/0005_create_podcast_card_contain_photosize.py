from django.db import migrations


PHOTO_SIZE_NAME = "podcast_card_contain"


def create_podcast_card_contain(apps, schema_editor):
    PhotoSize = apps.get_model("photologue", "PhotoSize")
    PhotoSize.objects.get_or_create(
        name=PHOTO_SIZE_NAME,
        defaults={
            "width": 360,
            "height": 190,
            "crop": False,
            "upscale": False,
            "quality": 80,
            "pre_cache": False,
            "increment_count": False,
        },
    )


def keep_podcast_card_contain(apps, schema_editor):
    # A pre-existing PhotoSize is indistinguishable from one created here.
    # Keep it on rollback rather than risk deleting user-managed configuration.
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("photologue", "0013_alter_watermark_image"),
        ("podcast", "0004_podcastepisode_audio_duration_and_more"),
    ]

    operations = [
        migrations.RunPython(
            create_podcast_card_contain,
            keep_podcast_card_contain,
        ),
    ]
