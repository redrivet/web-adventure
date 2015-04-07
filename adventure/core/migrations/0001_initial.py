# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=1024, help_text='The description of the direction or method of the exit. ex. North, South, Trap Door')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=1024, help_text='Admin nickname for this puzzle.')),
                ('description', models.TextField(help_text='Description of the puzzle to be solved in order for the player to be able to use an exit. The puzzle should be solvable via clues in this description or the room description')),
                ('hint', models.CharField(blank=True, max_length=2056, help_text='A short hint to assist the player in solving the puzzle.')),
                ('solution', models.CharField(blank=True, max_length=2056, help_text='Puzzle solution. The submitted player solution must match this solution exactly.')),
                ('exit', models.OneToOneField(related_name='puzzle', to='core.Exit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('key', models.CharField(help_text='Unique identifier for the room', unique=True, max_length=1024)),
                ('display_title', models.CharField(max_length=256, help_text='The name of the room displayed to the player.')),
                ('display_description', models.TextField(help_text='The description of the room displayed to the player. This description may include clues to the attached puzzles.')),
                ('adjacent_rooms', models.ManyToManyField(to='core.Room', through='core.Exit', related_name='from_rooms', help_text='The list of rooms that this room connects to via exits.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exit',
            name='from_room',
            field=models.ForeignKey(related_name='exits', to='core.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exit',
            name='to_room',
            field=models.ForeignKey(related_name='entrances', to='core.Room'),
            preserve_default=True,
        ),
    ]
