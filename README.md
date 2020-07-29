# About
Pygame version of space invaders. I made this game to learn the basics of pygame.

# Game Play
Controls: Left & Right arrow keys for movement. Spacebar for shooting.
Score points by shooting alien ships. Game ends when alien ships reach your area.
Exit out and restart script.

# Trouble shooting
Older versions of python might crash playing sounds using the mixer.Sound() methods. update python to 3.7 or higher.

Another work around might be changing the mixer.Sound() methods to mixer.music() methods but this will sacrifice being able to play continuous background music 
and only the laser and collision sounds will play. 

see example below:

Change this

```
laser = mixer.Sound('laser.wav')
laser.play()

contact = mixer.Sound('explosion.wav')
contact.play()
```

To this

```
mixer.music.load('laser.wav')
mixer.music.play()

mixer.music.load('explosion.wav')
mixer.music.play()
```

And take out this, otherwise the background music will stop after the first shot is fired

```
mixer.music.load('background.wav')
mixer.music.play(-1)
```
The game should run smoothly after these fixes in python 3.6 and lower.
