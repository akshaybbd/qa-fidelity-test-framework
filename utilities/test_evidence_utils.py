# created by Abhijeet Thorat at 2023-06-13 17:47.
#

import datetime
from pathlib import Path
import logging
import os
import shutil
import glob
import warnings
from utilities.path_configs import PathConfigs
from utilities.pulse_logger import get_logger

warnings.simplefilter('always', DeprecationWarning)
logger = get_logger(logger_name=__name__)

os.listdir()
logger = logging.Logger('catch_all')

warnings.warn(f"{__name__} will be deprecated", DeprecationWarning)

class TestEvidence:
    warnings.warn("Class will be deprecated", DeprecationWarning)

    def __init_subclass__(cls, **kwargs):
        """This throws a deprecation warning on subclassing."""
        warnings.warn(f'{cls.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)
        super().__init_subclass__(**kwargs)

    def __init__(self, *args, **kwargs):
        """This throws a deprecation warning on initialization."""
        warnings.warn(f'{self.__class__.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)
        super().__init__(*args, **kwargs)


    @staticmethod
    def moveFileToTestEvidenceFolder(pathToFileForMove, pathToTestEvidenceFolder, fileExtension):
        warnings.warn("Function will be deprecated", DeprecationWarning)

        try:
            for i in range(100):  # Number of files to be collected
                pathToFileLst = glob.glob(pathToFileForMove + fileExtension)
                if len(pathToFileLst)==0:
                    pass
                else:
                    pathToFile = glob.glob(pathToFileForMove + fileExtension)[0]
                    shutil.move(pathToFile, pathToTestEvidenceFolder)
        except Exception as e:
            logger.error(str(e), exc_info=True)


    @staticmethod
    def folderCount(path):
        count1 = 0
        for root, dirs, files in os.walk(path):
            count1 += len(dirs)
        return count1


    @staticmethod
    def createPath(pathToTestEvidenceFolder,cycleName,issueKey):
        warnings.warn("Function will be deprecated", DeprecationWarning)

        mydate = datetime.datetime.now()
        month = mydate.strftime("%B")
        day = datetime.datetime.today().day
        subfolder = str(day) + "-" + str(month)
        now = datetime.datetime.now()
        timestr = now.strftime('%Y-%m-%d %H-%M-%S-%f')
        newpath = os.path.join(pathToTestEvidenceFolder, subfolder,issueKey)# specify filename if its a file
        count = TestEvidence.folderCount(newpath)

        final_path= newpath =os.path.join(pathToTestEvidenceFolder, subfolder,issueKey,'TestRun_'+timestr)
        #print('final_path',final_path)

        #final_path = pathToTestEvidenceFolder + "/" + subfolder + "/" + issueKey + "/" +"TestRun"+str(count+1)+"/" # specify filename if its a file
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        return final_path


    @staticmethod
    def moveFiles(cycleName,issueKey):
        warnings.warn("Function will be deprecated", DeprecationWarning)

        try:
            """"Source Files - moving files"""
            sourcePathToFileForMove = PathConfigs.sourceDataPath
            pathToTestEvidenceFolder = PathConfigs.path_to_test_evidence
            pathToConfirmOfferForMove = PathConfigs.confirmOfferLogsPath

            testEvidenceDirectory = TestEvidence.createPath(pathToTestEvidenceFolder,cycleName,issueKey)
            excelfileExtension = "/*.xlsx"
            xmlFileExt = "/*.xml"
            txtFileExt = "/*.txt"
            jsonFileExt = "/*.json"
            pngFileExt = "/*.png"
            pdfFileExt = "/*.pdf"

            TestEvidence.moveFileToTestEvidenceFolder(sourcePathToFileForMove, testEvidenceDirectory, xmlFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(sourcePathToFileForMove, testEvidenceDirectory, txtFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(sourcePathToFileForMove, testEvidenceDirectory, excelfileExtension)
            TestEvidence.moveFileToTestEvidenceFolder(sourcePathToFileForMove, testEvidenceDirectory, jsonFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(sourcePathToFileForMove, testEvidenceDirectory, pngFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(sourcePathToFileForMove, testEvidenceDirectory, pdfFileExt)

            TestEvidence.moveFileToTestEvidenceFolder(pathToConfirmOfferForMove, testEvidenceDirectory, xmlFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(pathToConfirmOfferForMove, testEvidenceDirectory, txtFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(pathToConfirmOfferForMove, testEvidenceDirectory, excelfileExtension)

            """"Target Files - moving ibm files"""
            # parentDir = Path(__file__).parent.parent  # get parent directory
            targetPathToFileForMove = PathConfigs.tagetFolderPath
            excelfileExtension = "/*.xlsx"
            xmlFileExt = "/*.xml"
            txtFileExt = "/*.txt"
            pngFileExt = "/*.png"
            TestEvidence.moveFileToTestEvidenceFolder(targetPathToFileForMove, testEvidenceDirectory, xmlFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(targetPathToFileForMove, testEvidenceDirectory, txtFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(targetPathToFileForMove, testEvidenceDirectory, excelfileExtension)
            TestEvidence.moveFileToTestEvidenceFolder(targetPathToFileForMove, testEvidenceDirectory, jsonFileExt)
            TestEvidence.moveFileToTestEvidenceFolder(targetPathToFileForMove, testEvidenceDirectory, pngFileExt)
            print('Test Evidence Files Collected')
        except Exception as e:
            logger.error(str(e), exc_info=True)
            print('No files to collect')