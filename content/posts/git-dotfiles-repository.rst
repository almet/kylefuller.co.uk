Organising dotfiles in a git repository
#######################################

:tags: dotfiles, git
:github: kylef/dotfiles

Organising dotfiles can be done in numerous ways. Many dotfile repositories
often have their own clunky script to copy or symbolically link their dotfiles
in place. I feel this is a dirty approach and I prefer my files to be easily
manageable via the git command. I don't want to have to copy a file every time
I change it.

.. image:: /static/images/dotfiles.png
    :width: 589px
    :height: 276px
    :align: center

Another approach I have seen done, is making your whole home directory a git
repository. Unfortunately after using this solution you will come across a
number of flaws, any repository in your home directory will now follow your
`~/.gitignore`. I also came into many problems when I was using Xcode which
will try to git add projects into your dotfiles repository. Like symbolic
linking all my dotfiles into place, this solution also felt clunky.

Git allows you to seperate the work tree and the git dir via environment
variables or arguments to the git command. This allows us to store the bare git
dir in `~/.files.git` while still keeping our entire home directory as the work
tree for git.

I settled for using a simple alias in my `.zshrc` which allows me to easily use
git to manage my dotfiles. But, it is imporant to remember that the home
directory will not be seen as a git repository unless you use this alias. You
won't be able to accidentally use git commands thinking you were in another
repo, (or accidentally git add a bunch of things in a mercurial repository).

Here is the alias I use:

.. code-block:: bash

    $ alias home=git --work-tree=$HOME --git-dir=$HOME/.files.git

You can use this alias just as you would use the normal git command, this
allows you to clone and init a repo. To clone a dotfiles repo, you can do:

.. code-block:: bash

    $ home clone git://github.com/kylef/dotfiles.git

