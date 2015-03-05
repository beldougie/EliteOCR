import sys
import random
from os import environ, name
from os.path import isdir, dirname, split, realpath
from PyQt4.QtCore import QSettings, QString
from PyQt4.QtGui import QMessageBox, QFileDialog


class Settings():
    PROFILE_KEY = 'HOME' if name == 'posix' else 'USERINFO'

    def __init__(self, parent=None):
        self.parent = parent
        self.app_path = self.getPathToSelf()
        self.values = {}
        self.reg = QSettings('seeebek', 'eliteOCR')
        if self.reg.contains('settings_version'):
            if float(self.reg.value('settings_version', type=QString)) < 1.2:
                self.cleanReg()
                self.setAllDefaults()
                self.reg.sync()
                self.values = self.loadSettings()
            if float(self.reg.value('settings_version', type=QString)) < 1.4:
                self.setDefaultLanguage()
                self.setDefaultDelete()
                self.setDefaultTranslateResults()
                self.setDefaultPause()
                self.setDefaultUpdatesCheck()
                self.setDefaultPublicMode()
                self.setDefaultNativeDialog()
                self.reg.setValue('settings_version', "1.4")
                self.reg.sync()
            else:
                self.values = self.loadSettings()
        else:
            self.cleanReg()
            self.setAllDefaults()
            self.reg.sync()
            self.values = self.loadSettings()
    
    def __getitem__(self, key):
        if key in self.values:
            return self.values[key]
        else:
            raise KeyError("Key "+unicode(key)+" not found in settings.")
            
    def setValue(self, key, value):
        self.reg.setValue(key, value)
        
    def sync(self):
        """Save changes and reload settings"""
        self.reg.sync()
        self.values = self.loadSettings()
        
    def cleanReg(self):
        """Clean all registry entries (for old version or version not set)"""
        keys = self.reg.allKeys()
        for key in keys:
            self.reg.remove(key)

    def loadSettings(self):
        """Load all settings to a dict"""
        set = {'screenshot_dir': self.reg.value('screenshot_dir', type=QString),
               'export_dir': self.reg.value('export_dir', type=QString),
               'horizontal_exp': self.reg.value('horizontal_exp', type=bool),
               'last_export_format': self.reg.value('last_export_format', type=QString),
               'log_dir': self.reg.value('log_dir', type=QString),
               'auto_fill': self.reg.value('auto_fill', type=bool),
               'remove_dupli': self.reg.value('remove_dupli', type=bool),
               'userID': self.reg.value('userID', type=QString),
               'ui_language': self.reg.value('ui_language', type=QString),
               'ocr_language': self.reg.value('ocr_language', type=QString),
               'delete_files': self.reg.value('delete_files', type=bool),
               'translate_results': self.reg.value('translate_results', type=bool),
               'pause_at_end': self.reg.value('pause_at_end', type=bool),
               'updates_check': self.reg.value('updates_check', type=bool),
               'public_mode': self.reg.value('public_mode', type=bool),
               'native_dialog': self.reg.value('native_dialog', type=bool),
               'create_nn_images': self.reg.value('create_nn_images', type=bool),
               'zoom_factor': self.reg.value('zoom_factor', 1.0, type=float),
               'info_accepted': self.reg.value('info_accepted', False, type=bool),}
        return set
        
    def setAllDefaults(self):
        """Set all settings to default values"""
        self.setDefaultAutoFill()
        self.setDefaultRemoveDupli()
        self.setDefaultCreateNNImg()
        self.setDefaultDelete()
        self.setDefaultTranslateResults()
        self.setDefaultPause()
        self.setDefaultUpdatesCheck()
        self.setDefaultPublicMode()
        self.setDefaultNativeDialog()
        self.setDefaultScreenshotDir()
        self.setDefaultLogDir()
        self.setDefaultExportDir()
        self.setDefaultLanguage()
        self.setUserID()
        self.setSettingsVersion()
        
    def setSettingsVersion(self):
        self.reg.setValue('settings_version', "1.2")
        
    def setUserID(self):
        self.reg.setValue('userID', "EO"+''.join(random.choice('0123456789abcdef') for i in range(8)))
        
    def setDefaultExportOptions(self):
        self.setValue('horizontal_exp', False)
        self.setValue('last_export_format', 'xlsx')
    
    def setDefaultAutoFill(self):
        self.reg.setValue('auto_fill', False)
        
    def setDefaultRemoveDupli(self):
        self.reg.setValue('remove_dupli', True)
    
    def setDefaultLanguage(self):
        self.reg.setValue('ui_language', "en")
        self.reg.setValue('ocr_language', "eng")
        
    def setDefaultCreateNNImg(self):
        self.reg.setValue('create_nn_images', False)
        
    def setDefaultDelete(self):
        self.reg.setValue('delete_files', False)
        
    def setDefaultUpdatesCheck(self):
        self.reg.setValue('updates_check', True)
        
    def setDefaultTranslateResults(self):
        self.reg.setValue('translate_results', False)
    
    def setDefaultPause(self):
        self.reg.setValue('pause_at_end', True)
        
    def setDefaultPublicMode(self):
        self.reg.setValue('public_mode', True)
    
    def setDefaultNativeDialog(self):
        self.reg.setValue('native_dialog', False)
        
    def setDefaultScreenshotDir(self):
        if isdir(environ[self.PROFILE_KEY]+'\\Pictures\\Frontier Developments\\Elite Dangerous'):
            dir = environ[self.PROFILE_KEY]+'\\Pictures\\Frontier Developments\\Elite Dangerous'
        else:
            dir = self.app_path
        self.reg.setValue('screenshot_dir', dir)
        
    def setDefaultLogDir(self):
        if isdir(environ[self.PROFILE_KEY]+'\\AppData\\Local\\Frontier_Developments\\Products\\FORC-FDEV-D-1002\\Logs'):
            logdir = environ[self.PROFILE_KEY]+'\\AppData\\Local\\Frontier_Developments\\Products\\FORC-FDEV-D-1002\\Logs'
            self.reg.setValue('log_dir', logdir)
        else:
            self.reg.setValue('log_dir', self.app_path)
                
    def setDefaultExportDir(self):
        self.reg.setValue('export_dir', self.app_path)
        
    def getPathToSelf(self):
        """Return the path to EliteOCR.py or EliteOCR.exe"""
        if getattr(sys, 'frozen', False):
            application_path = dirname(sys.executable)
        elif __file__:
            application_path = dirname(__file__)
        return application_path
        