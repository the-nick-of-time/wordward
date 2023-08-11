# WORDWARD

This is a companion to the excellent little game [*WORDWARD DRAW*](https://managore.itch.io/wordward-draw), published
by [Daniel Linssen](https://twitter.com/managore) over at itch.io.
I made it because I saw the game, thought to myself *hmm, this seems like a problem that could be modeled by a graph*
and was promptly [nerd-sniped](https://xkcd.com/356/).

## Usage

This project requires [poetry](https://python-poetry.org/).

- Clone this repo and enter it on the command line.
- Create your environment with poetry: `poetry env use $(which python3)`
- Run the program: `./Taskfile run <start-word> <end-word>`

## TODO

Publish to PyPi or just as a wheel so that the entrypoint script is more accessible.
That'll require some mucking about with dumping my cache file somewhere better though.
