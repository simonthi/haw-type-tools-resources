# Metafont

## Setting up and getting started

There is a [comprehensive guide](http://metafont.tutorial.free.fr/downloads/mftut.pdf) on Metafont by Christophe Grandsire. 

However, here is a quick start version:

- Download and install a TEX package i.e. [TEXlive](https://tug.org/texlive/acquire-netinstall.html) or, while you’re at it [MacTEX](https://www.tug.org/mactex/mactex-download.html) which also installs a bunch of useful apps like TEXShop to view your files. Careful, the latter tends to be heavy (~4GB)
- While you’re waiting write your first testfiles for Metafont (see tutorial above or get at [sample file](./metafont-samples) 
- Use your command line to navigate to your file (if you don’t know how to do that, see the [command line guides in this repo](../README.md#%EF%B8%8F-command-line) )
- Enter ```mf2pt1 --designsize 12 a.mf```(replace ```a.mf``` with your Metafont file name) We use mf2pt1 here so you get file output in .pfb format that are editable in font editors of your choice.
- View your Output in a font editor of your choice and congrats your first Metafont letters are done.

## Resources

- [TEX user group](https://www.tug.org/)
- [Metafont examples](https://www.win.tue.nl/~aeb/tex/mf/metafont.html) (Used in [sample files](./metafont-samples))
