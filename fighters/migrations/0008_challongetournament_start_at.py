# Generated by Django 5.0.4 on 2024-09-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0007_challongetournament_sign_up_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='challongetournament',
            name='start_at',
            field=models.DateTimeField(null=True),
        ),
    ]
