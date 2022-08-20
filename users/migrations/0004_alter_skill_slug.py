from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_skill_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='slug',
            field=models.SlugField(),
        ),
    ]
