from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('intro', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='profile_images/default.jpg', null=True, upload_to='profile_images')),
                ('social_github', models.CharField(blank=True, max_length=100, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('social_website', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
