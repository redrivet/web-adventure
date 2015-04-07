from django.db import models


class Room(models.Model):
    """ A specific room in the maze.  Each room has multiple exits that join
    it to additional rooms for players to progress through the game.
    """
    key = models.CharField(max_length=1024, unique=True,
        help_text='Unique identifier for the room')

    adjacent_rooms = models.ManyToManyField('self', through='Exit',
        symmetrical=False, related_name='from_rooms',
        help_text='The list of rooms that this room connects to via exits.')

    display_title = models.CharField(max_length=256,
        help_text='The name of the room displayed to the player.')
    display_description = models.TextField(
        help_text='The description of the room displayed to the player. This ' + \
            'description may include clues to the attached puzzles.')

    def __str__(self):
        return '{} "{}"'.format(self.key, self.display_title) 


class Exit(models.Model):
    from_room = models.ForeignKey(Room, related_name='exits')
    to_room = models.ForeignKey(Room, related_name='entrances')

    name = models.CharField(max_length=1024,
        help_text='The description of the direction or method of the exit. ' + \
            'ex. North, South, Trap Door')

    def __str__(self):
        return self.name


class Puzzle(models.Model):
    exit = models.OneToOneField(Exit, related_name='puzzle')

    name = models.CharField(max_length=1024,
        help_text='Admin nickname for this puzzle.')
    description = models.TextField(
        help_text='Description of the puzzle to be solved in order for the ' + \
            'player to be able to use an exit. The puzzle should be solvable ' + \
            'via clues in this description or the room description')
    hint = models.CharField(max_length=2056, blank=True,
        help_text='A short hint to assist the player in solving the puzzle.')

    solution = models.CharField(max_length=2056, blank=True,
        help_text='Puzzle solution. The submitted player solution must match this solution exactly.')

    def __str__(self):
        return self.name

