# Ship-sank!
<br>
Ship-sank is a battleship game that is played in a Python terminal.
It runs in Heroku!
<br>
<br>
The user will try to find and sink the 5 ships that are randomly placed on the board.
Each ship takes up one cell of the board.
<br>
<br>

Here you can try out the game [Ship sank](https://ship-sank.herokuapp.com/).
<br>
<br>

![Screenshot of Am I Responsive page.](/img/amIresponsive.png)
<br>
<br>
<br>

## The rules of the game!
<br>
<br>
When the game starts it will show a text with short explenation about the game.
The user will then be prompted to add a user name.
After the user chooses a name the game will start.
In the start of the game the user will see a board that looks empty.
That is because the boats are hidden.
Now the user will have 7 tries to hit 5 ships.
The user will have a choice of 00 - 99.
If the user puts in 1 or 01 will be the same up until 9 (09).
As there is 100 places the ships can be at that means that the user
will get 100 choices to find the ships.
<br>
<br>
<br>

### The game!
<br>
<br>
When the game starts and this is what you would see!
<br>

![Screenshot of start-page.](/img/start.png)
<br>
<br>
Enter user name!
<br>

![Please enter your name here.](/img/name.png)
<br>
<br>
Welcome messege!
<br>

![Welcome...](/img/welcome.png)
<br>
<br>
Enter your guess!
<br>

![Please enter guess.](/img/guess.png)
<br>
<br>
Wrong Entry!
<br>

![If you enter other then a numbers.](/img/wrongentry.png)
<br>
<br>
If you enter invalid number!
<br>

![Wrong number entry.](/img/wrongnumber.png)
<br>
<br>
If you miss your target!
<br>

![If you miss the target.](/img/missed.png)
<br>
<br>
When you hit your target!
<br>

![Bullzeye](/img/bullzeye.png)
<br>
<br>
If you already tryed that cell!
<br>

![Already tryed that.](/img/already.png)
<br>
<br>
When you hit or miss it will be shown at the board!
<br>

![The choosen cells will be marked.](/img/hitmiss.png)
<br>
<br>
When the game is over this will be shown!
<br>

![Game over.](/img/gameover.png)
<br>
<br>
<br>

### Issues!
<br>
<br>

I had a lot of issues with Code Anywhere from the start of this Project.<br>
I sent a ticket to support in Code Anywhere and told them about what problems I got.<br>
Because of those issues delaying the project for me I had to shorten the code!<br>
<br><br>
The Plan from the beginning was that I would have had two boards.<br>
One for the user and one for the computer. So that the game would be player vs computer.<br>
But as the problems with Code Anywhere took alot of my time and put some pressuar on me.<br>
I had to change alot of structures that I had planned from the start.<br>
<br><br>
So if I would have had time.<br>
The plan was to have two boards and ships in 2-3 cells. Hit Miss Sank that was why the name was choosen.
<br>
<br>
<br>

### Testing!
<br>
<br>

I used [PEP](https://pep8ci.herokuapp.com//) testing and changed what needed to change.<br>
But there is one error thats still there and its in line 88 " E722 do not use bare 'except' "<br>
<br>
<br>
I have myself tested out the game and everything works as it should.
<br>
<br>

### Credits!
<br>
<br>

I got help from:
    - [Stack Overflow](https://stackoverflow.com/)
    - [w3schools](https://www.w3schools.com/)
    - [Tutors](https://learn.codeinstitute.net/)
<br>
<br>

### Deployment!
<br>
<br>

##### This project was deployed using Heroku terminal.

###### Steps to deploy:
    1 Fork or clone this repository
    2 Creat a new Heroku app
    3 Set a buildbacks to Python and NodeJS in that order
    4 Link the Heroku app to the repository
    5 Click to Deploy
