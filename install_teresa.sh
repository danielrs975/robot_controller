#!/bin/bash

TERESA_WS=~/teresa_ws/
rm -rf $TERESA_WS

echo '---------------------Installing Teresa-----------------------------------------'
mkdir -p $TERESA_WS/src

echo '---------------------Copying necessary files to src/---------------------------'
cp -r ~/teresa-driver/ $TERESA_WS/src/
cp -r ~/teresa_gazebo/ $TERESA_WS/src/

cd $TERESA_WS/src
catkin_init_workspace
cd ../
catkin_make
echo 'INSTALLATION FINISHED SUCCESFULLY'