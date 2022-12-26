#!/bin/bash

# From https://theowinter.ch/articles/Use-cgi-bin-to-automate-Jekyll/

#Script is executed by www-data user. It needs to have write-access to
#/var/www/2023 & /var/www/2023-passthesalt/
echo "Content-type: text/plain"
echo
echo "Checking for updates to 2023..."
exec 2>&1
cd /var/www/2023

#Check if there are changes
if git checkout main &&
    git fetch origin main &&
    [ `git rev-list HEAD...origin/main --count` != 0 ] &&
    git merge origin/main
then
    echo 'Changes found, syncing.'
    # sync Hugo generated content in public directory with the directory of the website already online
    rsync -av --delete /var/www/2023/public/ /var/www/2023-passthesalt/
else
    echo 'Not updated.'
fi
echo "Have a nice day!"
