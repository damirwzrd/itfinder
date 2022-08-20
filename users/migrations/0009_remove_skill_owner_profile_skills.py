from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_skills_skill_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='owner',
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='users.skill'),
        ),
    ]
