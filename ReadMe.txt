About 

1. As the program is executed, the player is asked to input their name in the shell
and that value is stored in a variable called 'name', that is later used to display
the result of the game.
2. tkinter module is used to display a message box that has the details and
information of the game for a first-time player.
3. After this, our game window opens. I have used 4 modules for making
Happyman! (pygame, tkinter, random, math)
i. I installed pygame in the directory where python 3.9 was installed by
opening the command prompt and typing:
&gt;&gt;&gt; pip install pygame
ii. The pygame module is designed for writing video games and I used its
computer graphics libraries to program this game with the Python
programming language.
iii. One of the most important parts of this game is displaying images at the
right co-ordinate.
i. display.set_mode() method creates a display surface object.
ii. image.load() method creates an image surface object i.e, an
area where we load images.
iii. blit() method copies the image surface object to the display
surface object.
iv. display.update() method shows the display surface object on
the pygame window.
v. time.delay() method has been used to specify the time for
which the message (name, 'You have won/lost!') will appear on the
screen.
vi. draw.circle() has been used to draw the circles on the
window in which the letters are displayed.

4. The random module was used here. a list called 'words'; was created that had
multiple words that were to be used for playing the game. using random.choice()
the program picks a word at random from the list and happyman! has an element
of surprise even for the coder.
5. 3 functions: draw(), main(), and display_message() have been defined to simplify
the program.
6. Nested for loop has been used in that part of the code where we append the
guessed letters in the 'guessed'; list.


How to run the game?

1. Open the zip file uploaded on the Google Classroom.
2. Run the happygirl.py file from the folder as it needs the Happygirl images
to run properly.