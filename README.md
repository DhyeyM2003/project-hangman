# Project: Hangman

In groups of three or four, grab a whiteboard and come up with pseudocode for hangman.

## Setup and workflow
### 1. Fork and add collaborators
- One group member must Fork my [original repository](https://github.com/ICS3U-Gallo/project-hangman).
- That group member will go into the newly forked repo, in `Settings -> Collaborators and teams`, add your group members' GitHub usernames or associated email addresses. This will allow everyone to freely make changes on that forked repo.

### 2. Create a feature branch
Create a branch whose name is based on what game feature you will be working on. For example, if you are responsible for the code that checks if a guess is correct, call the branch `guess-checking` (or something). Every separate feature of the code must be in its own branch and have its own pull request.

### 3. Code!
Write your code **in the appropriate branch**. You will want to verify that your particular code works by coming up with test cases.

### 4. Submit pull request
When you have verified that your code works, submit a pull request. Note: make sure you are on YOUR fork, not my original repo. At the top of the repo should have `your-user-name/project-hangman`. **Your username!**
- In your repo, go into the `Pull requests` tab.
- Click the green `New pull request` button.
**PAY ATTENTION TO THE FOLLOWING STEPS**
- It will automatically select my *original* repository as the "base fork", which is good! **However**, the "base" needs to be the class you are in (`grade-11b, grade-11c, or grade-10`).
- Wrte a nice message including your group members and what the pull request is for (i.e., checking if a letter is in a word).

## Syncing your Fork
There will be times when your Fork (copy of my repo) will be out of date. There is an elegant CLI way ot do this. On GitHub.com, we need to do a reverse pull request. 
- Go to the *original* repo,
- Click the `Pull Requests` tab
- Click the `New Pull Request` button
- Click the link "you can also **Compare across forks**".
- The **right side** should be the *original* `ICS3U/project-hangman` with the branch `grade-##x`. (The branch for your specific class) This will be the class's official branch that will be more up-to-date than your fork.
- On the **left side** you will select *your repo*. You can select the `master` branch to pull the changes into.
- Confirm that you are (reading from left to right) taking the `grade-##x` brancho of *my* repo and putting the changes (check the arrow) into the `master` branch of *your* repo.
- Click the `Create pull request` button. Then again.
- You will see the created pull request saying `<your username> wants to merge 2 commits into <you>:master from ICS3U-Gallo:grade-##x`.
Confirm that this is the case.
- Click `Merge pull request`


## Need to learn
### if, elif, else
This is explained in Chapter 4 of Head First: Learn to Code, or you can check out [Snakify.org](https://snakify.org/en/lessons/if_then_else_conditions/).

### in
Learn about using python's `in` keyword to check if something is *in* some iterable/collection. Check out this [repl.it](https://repl.it/@DanielGallo/Python-IN)

### Functions
We will be breaking apart our game features with functions. Check out [Snakify.org - Functions](https://snakify.org/en/lessons/functions/).
Essentially a function takes arguments(*input*), does some *processing*, then **return**s a result(*output*).

Try this in repl.it
```python
def add(a, b):      # input
    total = a + b   # processing
    return total    # output
  
print(add(4, 6))  # you get 10
```
**Input**: Two numbers, `a` and `b`.

**Processing**: Adding the two numbers

**Output**: Returns the sum

### Strings
Checkout [Snakify - Strings](https://snakify.org/en/lessons/strings_str/). You will need to be aware of what you can do with strings.
