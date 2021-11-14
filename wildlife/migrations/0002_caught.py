# Generated by Django 3.2.9 on 2021-11-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlife', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caught',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('ueid', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('item_type', models.CharField(choices=[('F', 'Fish'), ('B', 'Bug'), ('S', 'Sea'), ('K', 'Song'), ('F', 'Fossil'), ('A', 'Art'), ('G', 'Gyroid'), ('V', 'Villager'), ('R', 'Reaction')], max_length=2)),
            ],
        ),
    ]
