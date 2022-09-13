# Transform raster dataset from one from one coordinate system to another
import datetime
import os
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True
# Edited : 9/12/22

#Pass in the message you want to print with the current time as str
def printTime(str):
    print(str, datetime.datetime.now().strftime("%A, %B %d %Y %I:%M:%S%p"))
# Pass in the workspace as path, this method will set that workspace as environment
def getPath(path):
    arcpy.env.workspace = path
arcpy.CheckOutExtension("Spatial")
#This takes in in_raster TIF file
# The raster dataset with new projection tat will bre created, feel free to give any name to the file but specify PNG, TIF, JPG etc type
# Out_coor system is taken from any .PRJ file. Make sure, the file is prj
def projectRaster(in_raster, out_raster, out_coor_sys):
    arcpy.ProjectRaster_management(in_raster, out_raster, out_coor_sys)

printTime("Our process stats now: ")
getPath("E:\\Dr. Koch\\Dr. Koch Data\\Texasdata\\CDL_2020_48")
projectRaster("CDL_2020_48.tif", "reproject.png", "huc8.prj")
printTime("Our process finishes now: ")
