
	After installation,

	* Set your username and e-mail address. This is important because every Git commit uses this information.
	* Enter your shell (Terminal or Git Bash) and enter the following with your information:

	git config --global user.name "Your Name"
	git config --global user.email your_name@example.com

	* You can verify that Git stored your settings by passing git config the --list parameter:

	git config --global --list

	GIT COMMANDS -

	git init - initialize the repository.
	git add . - add all the files that were changed since the last back up to the staging area.
	git status - shows you all the files that were changed since the last backup and which ones are already added to the staging area.
	git commit -m "..." - commits the changes to the repository.
	git checkout ____ - switches to the branch name provided in your git repository. This will create a new branch if the name provided doesn't exist.
	git branch - shows all of your git branches and marks the one you are currently on.
	git log - shows all the backups created in the repository.
	git blame ____ - shows who wrote which line of code or in other words who is to be blamed for that particular line of code.
	git remote add origin ____ - tells git to add a remote place called 'origin' to a remote URL ___.
	git push - pushes the changes in your local repository to the remote repository.
	git pull - pulls the changes in a remote repository to your own local repository.
	git clone ___ - clones a remote repository in ___ to your own local folder.

	CREATING REPOSITORY(VIA TERMINAL)
	* To create a repository, all we need to do is type:

	git init

	* Now create a file in that directory called aboutMe.txt with your name, a project goal you wish to accomplish, and your favorite TV show. Ours looked like this: 

	Name: Kari Ekenes
	Project Goal: Master Git!
	Favorite TV Show: Game of Thrones

	The current state of aboutMe.txt is modified. You can see the current state by running:
	git status

	* To change the state to staged (which means ready to be committed), we tell Git to add the file to its index.
	git add aboutMe.txt

	Now to take a snapshot of the current state of all the staged files, we run:
	git commit -m "aboutMe.txt added"

	Now to see the list of your commits, you can run the command
	git log