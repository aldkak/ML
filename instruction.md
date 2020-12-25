# set your linux os to work with ML 
setting you machine(laptop or PC) is the first step to start coding. in this file , how to set a machine with ubuntu operating system to work with machine learning and its various task such as 
computer vision, NLP, Stock Forecasting or an type of analysis,

## update the system
`sudo apt-get update`
`sudo apt-get upgrade`
## installing some packages
`sudo apt-get install build-essential cmake g++ gfortran`
`sudo apt-get install git pkg-config python-dev`
`sudo apt-get install software-properties-common wget`
`sudo apt-get install libhdf5`
`sudo pip3 install h5py`
`sudo apt-get autoremove`
`sudo rm -rf /var/lib/apt/lists/*`

## installing OpenCV dependencies
- [compiler ] 
`sudo apt-get install build-essential`
- [required ]
`sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev`
- [optional ]
`sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev`
`sudo apt-get install python2.7-dev python3.5-dev`
  
## it is better to install open cv on a virtual enviorment
`sudo pip install virtualenv virtualenvwrapper`
`sudo rm -rf ~/get-pip.py ~/.cache/pip `

Once we have _virtualenv_  and _virtualenvwrapper_  installed, we need to update our ~/.bashrc  file  to include the following lines at the bottom of the file

```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
## or by runing the following commands 
`echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc`
`echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc`
`echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc`
## then we source the .bashrc to apply the new changes 
`$source ~/.bashrc`
## create virtualenv 
*it is always recommended to create a virtualenv for each project, this will 
help you preventing damaging other project that depends on the same env*

Now that we have installed virtualenv  and virtualenvwrapper , 
the next step is to create the Python virtual environment for opencv 
and let call it cv (computer vision)
- **we do this using the mkvirtualenv  command.**
`mkvirtualenv cv -p python3`
- **to actually work with open cv you need to execute the following command every time you open the terminal this will activate the virtual environment cv**
`workon cv ` 

- **if you want to  to know what environment do you have just type``
`workon` then the tab button
- **to exit the environment type**
  `deactivate`

# build the opencv lib.
  at first we Install NumPy into the  Python virtual environment, which is
  a Python package used for numerical processing, keep in mind that we are
  installing this package inside the environment so you have to activate the
  environment before installing any packages
  `pip3 install numpy`

choose a directory to clone the opencv

  `cd ~/<my_working_directory>`
  `git clone https://github.com/opencv/opencv.git`
  `git clone https://github.com/opencv/opencv_contrib.git`
  `cd ~/opencv`
  `mkdir build`
  `cd build`
  `cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
      -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
      -D BUILD_EXAMPLES=ON ..`
      
 After executing  CMake command  without any errors, you can  compile OpenCV using :
    `make -j4`
 The last step is to actually install OpenCV 3 :
    `sudo make install`
    `sudo ldconfig`
  
 **to test if it works**
  
  `cd ~`
  `workon cv`
  `python -c "import cv; print(cv.__version__)"`

-------------------------------------------------------------------------------
***now let's install other packages to work with deep learning**
-------------------------------------------------------------------------------

`pip3 install tensorflow`
`pip3 install keras`

you can keep installing packages to this environment as you need
here is a list of packages that you may need:
  1. theano
  2. Scikit-learn
  3. matplotlib
  4. scipy
  5. pandas
  6. pytorch
  7. nltk
  8. TextBlob
  9. spacy
  10. CoreNLP
  11. Gensim
  12. PyNLPI
  13. Pattern
  14. Polyglot
  and many others , but those are the famouse one
  
  and you can install them  using pip3

**enjoy**
@Msaif
