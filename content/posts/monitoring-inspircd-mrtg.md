Title: Monitoring InspIRCd with MRTG
Date: 2011-08-13
Tags: MRTG, InspIRCd
Slug: monitoring-inspircd-mrtg

This guide will show you how to configure MRTG to show statistics from an InspIRCd IRC server, this will include user counts and channel counts. This guide assumes you already have InspIRCd and MRTG setup and working. You can see an example of this working at [Sector 5D](http://hydra.sector5d.org/).

### InspIRCd config

First, you will need to configure InspIRCd to use the `m_http` and `m_http_stats` module. I configure InspIRCd to listen on localhost and port 8081 with SSL, but you could pick any port you want, just remember to change the `$address` variable inside `inspircd-stats.sh` later.

Note, the following config is for InspIRCd 2.0, if you use a older version you may need to change the bind line to a http line, please see the InspIRCd wiki for using a older version.

    ::xml
    <module name="m_httpd.so">
    <module name="m_httpd_stats.so">
    <bind address="localhost" port="8081" type="httpd" ssl="gnutls">

Once you have placed this in your InspIRCd config, you can rehash or reload InspIRCd and then you will be able to connect to it over http(s) to retrive stats. Such as at https://localhost:8081/stats

#### Creating a script to gather the user or channel count on InspIRCd

The following script queries the InspIRCd `m_httpd_stats` module for the user or channel count. This depends on [XMLStarlet](http://xmlstar.sourceforge.net/) ([Debian package](http://packages.debian.org/search?keywords=xmlstarlet), [Arch AUR Package](https://aur.archlinux.org/packages.php?ID=20101)), so please install this first.

    :::bash
    #!/bin/sh

    address="https://localhost:8081/stats"
    count_type=$1

    if [[ "$count_type" != "user"  && "$count_type" != "channel" ]]; then
      echo "Usage: $0 <user|channel>"
      exit 1
    elif

    count=$(wget -q -Y off -O - --no-check-certificate $address | xml sel -t -v "inspircdstats/general/${count_type}count")

    echo $count
    echo $count
    echo "IRC $count_type"

This script will need to be available from the user which you run MRTG as. I have placed mine in `/usr/local/bin/inspircd-stats.sh` but you could place it somewhere like `$HOME/bin/inspircd-stats.sh`.

To download and install this to /usr/local/bin run the following:

    :::bash
    sudo mkdir -p /usr/local/bin
    sudo wget https://raw.github.com/gist/1042604/b19a4cfd91b6956063d962c977f3d5f8e3318d7d/inspircd-stats.sh -O /usr/local/bin/inspircd-stats.sh
    sudo chmod+x /usr/local/bin/inspircd-stats.sh

Now you have this `inspircd-stats.sh` script, you can use it to get the user and channel count as follows:

    :::bash
    /usr/local/bin/inspircd-stats.sh user
    /usr/local/bin/inspircd-stats.sh channel

### MRTG Config

You will need to add the following to your mrtg config file, this could be located at `/etc/mrtg.cfg`, but this depends on how you setup mrtg.

    # For IRC Users:
    Target[irc.users]: `/usr/local/bin/inspircd-stats.sh user`
    Title[irc.users]: IRC Users
    PageTop[irc.users]: <h1>IRC Users</h1>
    MaxBytes[irc.users]: 10000000000
    ShortLegend[irc.users]: users
    YLegend[irc.users]: Users
    LegendI[irc.users]: Users
    LegendO[irc.users]:
    Legend1[irc.users]: Users
    Legend2[irc.users]:
    Options[irc.users]: growright,nopercent,gauge

    # For IRC Channels:
    Target[irc.channels]: `/usr/local/bin/inspircd-stats.sh channel`
    Title[irc.channels]: IRC Channels
    PageTop[irc.channels]: <h1>IRC Channels</h1>
    MaxBytes[irc.channels]: 10000000000
    ShortLegend[irc.channels]: channels
    YLegend[irc.channels]: Channels
    LegendI[irc.channels]: Channels
    LegendO[irc.channels]:
    Legend1[irc.channels]: Channels
    Legend2[irc.channels]:
    Options[irc.channels]: growright,nopercent,gauge

Now, you can run your MRTG command for your config or wait for the MRTG cron and it should show up your InspIRCd stats.
