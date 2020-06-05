#! /bin/bash
tag=SR

rm -r /eos/home-a/ahakimi/www/ZV_analysis/$tag

cd ..
cp -a $tag/ /eos/home-a/ahakimi/www/ZV_analysis

cp /afs/cern.ch/user/a/ahakimi/index.php /eos/home-a/ahakimi/www/ZV_analysis/$tag
cp /afs/cern.ch/user/a/ahakimi/index.php  /eos/home-a/ahakimi/www/ZV_analysis/$tag/PlotsVBS_ZV
