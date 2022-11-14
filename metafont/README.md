# Metafont

## Setting up and getting started

There is a [comprehensive guide](http://metafont.tutorial.free.fr/downloads/mftut.pdf) on Metafont by Christophe Grandsire. However, here a quick start version:

- Download and install a TEX package i.e. [TEXlive](https://tug.org/texlive/acquire-netinstall.html) or, while you’re at it [MacTEX](https://www.tug.org/mactex/mactex-download.html) which also installs a bunch of useful apps like TEXShop to view your files. Careful, the latter tends to be heavy (~4GB)
- While you’re waiting write your first testfiles for Metafont (see tutorial above or get at [sample file](/metafont-samples)) 
- Use your command line to navigate to your file (if you don’t know how to do that, see the [command line guides in this repo](../README.md#command-line))
- Enter ```mf-nowin beta.mf```(replace ```beta.mf``` with your Metafont file name)
- Enter ```gftodvi beta.2602gf```(replace ```beta.2602gf``` with your output file name which can be found in the same direcrtory as your base file)
- View your Output dvi and congrats your first Metafont letters are done.

## Resources

- [TEX user group](https://www.tug.org/)
