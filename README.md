# homedir

Store all the things I want in a linux home dir. Inspired from a [Hacker News thread][1]

## Use

Use the `hgit` alias to work with this repo once installed

## Installation

To setup homedir on a new machine, do this:

    cd ~
    git clone --bare git@github.com:stevearm/homedir.git .homegit
    git --git-dir=.homegit --work-tree=~ checkout -f    # Overwrite existing files
    echo '*' >> .homegit/info/exclude

[1]: https://news.ycombinator.com/item?id=8488463
