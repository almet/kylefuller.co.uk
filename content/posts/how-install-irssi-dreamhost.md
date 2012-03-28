Title: How to install irssi on Dreamhost
Date: 2009-02-24
Tags: dreamhost
Slug: how-install-irssi-dreamhost

This was a useful guide I wrote back on my old website. I was trying to install irssi, and I couldn't remember how I installed it last time. Luckily it was available on archive.org's [WayBackMachine](http://www.archive.org/web/web.php). I have updated this guide to glib-2.19.8 and irssi-0.8.15.

To install irssi, you can eigher follow the next 7 steps and install from source.

Every command on this page should be entered into a SSH Prompt on DreamHost

### SSH into your Dreamhost server (for me, this is titan.dreamhost.com, you can find your server inside [panel](https://panel.dreamhost.com/))
### Create the necessary directories:

    :::bash
    mkdir -p bin lib tmp
    chmod 700 bin lib tmp

### Adding lines to your ~/.bash_profile

    :::bash
    echo "export PATH=$PATH:$HOME/bin" >> ~/.bash_profile
    echo "export PKG_CONFIG_PATH=$HOME/lib/pkgconfig" >> ~/.bash_profile
    echo "export LD_LIBRARY_PATH=$HOME/lib:/usr/local/lib:$LD_LIBRARY_PATH" >> ~/.bash_profile

### Activate the new changes

    :::bash
    source ~/.bash_profile

### Download, untar, and install glib

    :::bash
    cd ~/tmp
    wget ftp://ftp.gtk.org/pub/glib/2.19/glib-2.19.8.tar.gz
    tar -xvzf glib-2.19.8.tar.gz
    cd glib-2.19.8
    ./configure --prefix=$HOME
    make
    make install

### Download and install irssi

    :::bash
    cd ~/tmp
    wget http://irssi.org/files/irssi-0.8.15.tar.gz
    tar -xvvzf irssi-0.8.15.tar.gz
    cd irssi-0.8.15
    ./configure --prefix=$HOME
    make
    make install

### Clean up

    :::bash
    rm -rf ~/tmp/glib-2.19.8.tar.gz ~/tmp/glib-2.19.8 ~/tmp/irssi-0.8.15.tar.gz ~/tmp/irssi-0.8.15

Once you have installed it, simply type ``irssi`` to run it.

I asked Dreamhost if they would allow the use of a terminal application running
all the time. Here is their response:

> You won’t be in “trouble” for running an irc program (no servers) on our
> servers. However if the system becomes unstable, it would likely be one of
> the first processes killed by our admins as our servers are meant for hosting
> web pages only. In general , we just don’t want users running bots or their
> own server daemons on our servers.”
