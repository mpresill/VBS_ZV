#! /bin/bash
tag=SR

rm -r /eos/user/m/mpresill/www/VBS/$tag

cd ..
cp -a $tag/ /eos/user/m/mpresill/www/VBS

cp /eos/user/m/mpresill/www/index.php /eos/user/m/mpresill/www/VBS/$tag
cp /eos/user/m/mpresill/www/index.php  /eos/user/m/mpresill/www/VBS/$tag/PlotsVBS_ZV