# Metafont

## Setting up and getting started

There is a [comprehensive guide](http://metafont.tutorial.free.fr/downloads/mftut.pdf) on Metafont by Christophe Grandsire. 

However, here is a quick start version:

- Download and install a TEX package i.e. [TEXlive](https://tug.org/texlive/acquire-netinstall.html) or, while you’re at it [MacTEX](https://www.tug.org/mactex/mactex-download.html) which also installs a bunch of useful apps like TEXShop to view your files. Careful, the latter tends to be heavy (~4GB)
- While you’re waiting write your first testfiles for Metafont (see tutorial above or get at [sample file](./metafont-samples) 
- Use your command line to navigate to your file (if you don’t know how to do that, see the [command line guides in this repo](../README.md#%EF%B8%8F-command-line) )
- Enter ```mf2pt1 --designsize=12 a.mf```(replace ```a.mf``` with your Metafont file name) We use mf2pt1 here so you get file output in .pfb format that are editable in font editors of your choice. For a full documentation of ```mf2pt``` and all parameters like ```--designsize=12``` and what they do [go here](https://packages.oth-regensburg.de/ctan/support/mf2pt1/mf2pt1.pdf)
- View your Output in a font editor of your choice and congrats your first Metafont letters are done.

## What is Metafont?

In short: a description language to describe fonts. 

For more in-depth reading I’ll send you to read Knuth’s [introduction of Metafont](https://archive.org/details/the-concept-of-metafont/mode/2up) in Visible Language or the respective [Wikipedia article](https://en.wikipedia.org/wiki/Metafont).

## Resources
- Donald Knuth’s [METAFONTbook](https://archive.org/details/metafontbook00knut/mode/2up)
- [TEX user group](https://www.tug.org/)
- [Metafont examples](https://www.win.tue.nl/~aeb/tex/mf/metafont.html) (Used in [sample files](./metafont-samples))


## Is Metafont still used?
Well, sometimes. But have a look at some projects for yourselves:

- [Subiaco by C-A-S-T](https://www.c-a-s-t.com/studies/subiaco/)
