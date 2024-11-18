# Avoid the Colors!

# Description
  Avoid the Colors is a game where you use your mouse to move around the screen and avoid hitting the colors that will come from either horizontal, diagonol, or vertical direction. 
The goal of the game is to see how long the player can survive, which will give them a high score depending on how long they survived. This project utilizes multiple classes and 
functions that include particles/trails, player, collisions, and evena  game over screen. I had to use 3 different modules which include pygame, time, and random to be able to
make the game. 

# Areas to Imrpove
  Some parts I would improve would be the optimization of the code since I can't really tell what area of the code can save space without making the program crash (and it has
happened sometimes when something gets changed) so I wished I was a bit better at that. In the game itself as well, the trails go in the designated directions but seems to
run on forever and will slowly start to accumulate until the player has no room to escape. I think if I were able to spend a bit more time into it, I could be able to not
only have it dissappear after some time from the trail, but also decrease the speed of the trails as they do come out very fast. 

# Commit History Notice
  As of November 18th, 2024, for some reason upon opening it up the github was not allowing more commits for somereason even though a week ago I was able to get the commits to show
up so I'll mention a summary of it here. The first major commit was making the game restartable by pressing the space bar once the player reaches the game over screen. Previously,
whenever the player reaches the game over screen, it would give a few seconds of peace before forcefully putting the player back into the game, so I modified it to where hitting the
spacebar would let the player restart instead of it being a delayed restart. The 2nd major commit change would be the movment of the particles, as previously while the game ran, the 
particles would be spawned randomly across the screen but they would just be sitting in one place until the player collides and dies. After modifying the particle class, particle trails class, 
and main fucntion I was able to get them to move but it went from spawning randomly to spawning randomly from the edges and lasting a short time. The final major commit was making them move
until they hit at the edge of screen which is when it became to look so spammy afterwards.

# Links
YouTube: https://youtu.be/EKoTDHLRjwI

