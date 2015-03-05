EliteOCR
==============
EliteOCR is a Python script that runs optical character recognition on screenshots
from Elite: Dangerous commodities market. 

Prerequisites
--------------
EliteOCR is capable of reading the entries in Elite: Dangerous markets screenshots.
Best results are achieved with screenshots of 3840 by 2160 pixel (4K) or more.
You can make screenshots in game by pressing F10. You find them usually in
C:\Users\USERNAME\Pictures\Frontier Developments\Elite Dangerous
Screenshots made with ALT+F10 have lower recognition rate!

Owners of Nvidia video cards can use DSR technology to increase the resolution 
for screenshots and revert it back to normal without leaving the game.

Usage
--------------
Run EliteOCR.exe
Click "+" and select your screenshots. Select multiple files by holding CTRL or add them one by one.
Select one file and click the OCR button. Check if the values have been recognised properly.
Optionally correct them or choose alternative from the drop down list. Click on "Add and Next"
to continue to next line. You can edit the values in the table by double clicking on the entry.

After processing one screenshot you can choose the next file in the list and click the ORC Button
again. Should there be a corrupted entry, you can click "Skip" to continue to next line without adding
current one to the list. Duplicate entries are by default filtered out. To change this behaviour
go to Settings.

When finished click on "Export" to save your results to a csv-file(separated by ; ). CSV can be
opened by most spreadsheet editors like Excel, LibreOffice Calc etc. or alternatively text editors.


Dependencies to run from source
--------------

### Requirements

##### Python 2.7 

[https://www.python.org/downloads/](https://www.python.org/downloads/)

##### Numpy 

    pip install numpy

##### OpenCV 

###### Windows

[http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.10/](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.10/) 

* Goto opencv/build/python/2.7 folder. 
* Copy cv2.pyd to C:/Python27/lib/site-packages.

###### Mac OSx

Install using [homebrew][1]

	brew tap homebrew/science
    brew install opencv
    cd /User/Library/2.7/site-packages 
    # make sure you adjust accordingly for virtualenv etc..
    ln -s /usr/local/Cellar/opencv/2.4.10.1/lib/python2.7/site-packages/cv.py cv.py
    ln -s /usr/local/Cellar/opencv/2.4.10.1/lib/python2.7/site-packages/cv2.so cv2.so

##### Python-Tesseract

###### Windows

Download the latest executable: [https://bitbucket.org/3togo/python-tesseract/downloads/](https://bitbucket.org/3togo/python-tesseract/downloads/)

###### Mac OSX
Download and install Tesseract using [homebrew][1]

	brew install Tesseract
	
Install the egg directly from the repository
	
	easy_install https://bitbucket.org/3togo/python-tesseract/downloads/python_tesseract-0.9.1-py2.7-macosx-10.10-x86_64.egg

##### PyQt4

###### Windows

Install the latest executable:
[http://www.riverbankcomputing.co.uk/software/pyqt/download](http://www.riverbankcomputing.co.uk/software/pyqt/download)

###### Mac OSX

* Download the latest 4.x version of QT and the debug libraries from the archive: [http://download.qt.io/archive/qt/4.8/4.8.6/](http://download.qt.io/archive/qt/4.8/4.8.6/). 
* Install QT and the optional debug libraries onto your system using the packages within the `dmg` images downloaded
* Download the latest version of SIP from [http://www.riverbankcomputing.com/software/sip/download](http://www.riverbankcomputing.com/software/sip/download)
* Unpack the downloaded tar
* Move to the `docs/` directory and open the `installation.html` file. Follow the instructions.
* Download the latest source code for Mac OS from [http://www.riverbankcomputing.co.uk/software/pyqt/download](http://www.riverbankcomputing.co.uk/software/pyqt/download)
* Unpack the downloaded tar
* Open the README and follow the installation instructions

##### qimage2ndarray 

	pip install qimage2ndarray 

[http://pypi.python.org/pypi/qimage2ndarray](http://pypi.python.org/pypi/qimage2ndarray)

##### Openpyxl 

	pip install openpyxl

[https://pypi.python.org/pypi/openpyxl](https://pypi.python.org/pypi/openpyxl)
    
##### Ezodf 

	pip install ezodf

[https://pypi.python.org/pypi/ezodf](https://pypi.python.org/pypi/ezodf)

##### Lxml

	pip install lxml

[https://pypi.python.org/pypi/lxml](https://pypi.python.org/pypi/lxml)

##### python-Levenshtein

	pip install python-Levenshtein

[https://pypi.python.org/pypi/python-Levenshtein/](https://pypi.python.org/pypi/python-Levenshtein/)

##### pytz

	pip install pytz

[https://pypi.python.org/pypi/pytz](https://pypi.python.org/pypi/pytz)

##### tzlocal

	pip install tzlocal

[https://pypi.python.org/pypi/tzlocal](https://pypi.python.org/pypi/tzlocal)

##### BeautifulSoup4

	pip install beautifulsoup4
	
[https://pypi.python.org/pypi/beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

##### SciPy

	pip install scipy

[https://pypi.python.org/pypi/scipy](https://pypi.python.org/pypi/scipy)

#####  Scikit-Learn

	pip install -U sckit-learn

[https://pypi.python.org/pypi/scikit-learn](https://pypi.python.org/pypi/scikit-learn)

##### requests

	pip install requests
	
[https://pypi.python.org/pypi/requests](https://pypi.python.org/pypi/requests)

###### wget

	pip install wget

[https://pypi.python.org/pypi/wget](https://pypi.python.org/pypi/wget)


Run EliteOCR.py

To create a standalone exe file
--------------

pip install pyinstaller

pyinstaller --onedir EliteOCR.py


[1]: http://brew.sh/
