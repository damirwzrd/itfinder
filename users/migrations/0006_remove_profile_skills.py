from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
    ]
