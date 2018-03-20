set your linux os to work with ML 
use the following command
# update the system
[in 1]
sudo apt-get update
sudo apt-get upgrade
# installing some packages
sudo apt-get install build-essential cmake g++ gfortran 
sudo apt-get install git pkg-config python-dev 
sudo apt-get install software-properties-common wget
sudo apt-get autoremove 
sudo rm -rf /var/lib/apt/lists/*

# installing OpenCV
[compiler] sudo apt-get install build-essential
[required] sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
[optional] sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev
                                libtiff-dev libjasper-dev libdc1394-22-dev

sudo apt-get install python2.7-dev python3.5-dev
# it is better to install open cv on a virtual enviorment
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

Once we have virtualenv  and virtualenvwrapper  installed, we need to update our ~/.bashrc  file 
to include the following lines at the bottom of the file
--------------------------------------------
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
--------------------------------------------
# or by runing the following commands 
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
------------------------------------------
# continue 
source ~/.bashrc

Now that we have installed virtualenv  and virtualenvwrapper , 
the next step is to create the Python virtual environment for opencv 
and let call it cv (computer vision)
# we do this using the mkvirtualenv  command.
mkvirtualenv cv -p python3
# to actualy work with open cv you need to execute the following command everytime you open the terminal 
workon cv 
3 if you want to  to know what enviorment do you have just type < workon >
# to exit the enviorment type deactivate

#you can either install open cv directly or build 


cd ~/<my_working_directory>
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
cd ~/opencv
mkdir build
cd build
