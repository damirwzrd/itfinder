from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_skill_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='owner',
        ),
    ]
