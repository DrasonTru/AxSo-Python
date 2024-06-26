# Importing library
import cv2
from pyzbar.pyzbar import decode
import numpy as np


# Make one method to decode the barcode
def BarcodeReader(image):

      f =3D open("TEST4.txt", "a")  ### Write to file, append

      # read the image in numpy array using cv2
      img =3D cv2.imread(image)

      # Decode the barcode image
      detectedBarcodes =3D decode(img)

      # If not detected then print the message
      if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!=
")
      else:

            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes:

                  # Locate the barcode position in image
                  (x, y, w, h) =3D barcode.rect

                  # Put the rectangle in image using
                  # cv2 to highlight the barcode
                  cv2.rectangle(img, (x-10, y-10),
                                    (x + w+10, y + h+10),
                                    (255, 0, 0), 2)

                  if barcode.data!=3D"":

                  # Print the barcode data ###############################
                        print(barcode.data)
                        #print(barcode.type)
                        strNew =3D str(barcode.data)
                        strNewer =3D strNew[2:14]

                        #f.write(image) # WRITE RESULTS TO TEXT DOCUMENT
                        #f.write(" ")
                        #f.write(strNewer)
                        #f.write("\n")

      try:
            f.write(image) # WRITE RESULTS TO TEXT DOCUMENT
            f.write(" ")
            f.write(strNewer)
            f.write("\n")
      except:
            f.write(image)
            f.write("\n")
            x =3D 1

      f.close()


if __name__ =3D=3D "__main__":

      numInt =3D 1  ### Iterate through images, start with IMG #
      while numInt < 10000: #Final IMG #
            strNum =3D str(numInt)
            if len(strNum) =3D=3D 1:
                  numName =3D '000' + strNum
            elif len(strNum) =3D=3D 2:
                  numName =3D '00' + strNum
            elif len(strNum) =3D=3D 3:
                  numName =3D '0' + strNum
            else:
                  numName =3D strNum

            print(numName)
            image =3D "202303_a_RENAME/IMG_" + numName + ".jpg" ###

            try:
                  BarcodeReader(image)                  ###
            except:
                  x =3D 1 #Try to decode using barcode image, if IMG does n=
ot exist, skip

            numInt+=3D 1


##########################################################
#### NO LONGER EXCEL PRAC
#### Program 1 - REMOVE FOUND IMAGES FROM MASTER FOLDER
#### Program 2 - RENAME IMAGES IN FOLDER USING NAMING CONVENTION IMG_0000

import os
import glob

# Program 1
def remove_images_from_folder(folder_path, text_file_path):
    # Read the image names to be removed from the text file
    with open(text_file_path, 'r') as file:
        images_to_remove =3D [line.strip() for line in file.readlines()]

    # Check if each image exists in the folder and delete it if found
    for image_name in images_to_remove:
        image_path =3D os.path.join(folder_path, image_name)
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Removed image: {image_name}")
            else:
                print(f"Image not found: {image_name}")
        except Exception as e:
            print(f"Error while removing {image_name}: {str(e)}")

# MAIN - remove found images
#if __name__ =3D=3D "__main__":
    # Replace the following line with the actual path to your folder contai=
ning the images
    folder_path =3D "202303_a_REMOVE"

    # Replace the following line with the actual path to your text file lis=
ting the images to be removed
    text_file_path =3D "FOUND_03A.txt"

    remove_images_from_folder(folder_path, text_file_path)

# Program 2
def rename_images(directory):
    # Check if the provided path is a valid directory
    if not os.path.isdir(directory):
        print("Error: The provided path is not a valid directory.")
        return

    # Get a list of all files in the directory
    files =3D os.listdir(directory)

    # Filter for only image files (you can modify the list of valid image e=
xtensions if needed)
    image_extensions =3D [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    image_files =3D [file for file in files if os.path.splitext(file)[1].lo=
wer() in image_extensions]

    # Sort the image files alphabetically
    image_files.sort()

    # Initialize the counter for renaming
    counter =3D 1

    # Iterate through the image files and rename them
    for image_file in image_files:
        # Create the new name with leading zeros and .jpg extension
        new_name =3D f"IMG_{str(counter).zfill(4)}.jpg"

        # Build the full paths for the old and new names
        old_path =3D os.path.join(directory, image_file)
        new_path =3D os.path.join(directory, new_name)

        # Check if the new name already exists (unlikely, but just in case)
        while os.path.exists(new_path):
            counter +=3D 1
            new_name =3D f"IMG_{str(counter).zfill(4)}.jpg"
            new_path =3D os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {image_file} -> {new_name}")

        # Increment the counter for the next image
        counter +=3D 1

if __name__ =3D=3D "__main__":
    target_directory =3D "NEw_REDUCED"
    rename_images(target_directory)

###########################################################################=
####


# import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# initialize browser window, how code interacts with website browser, choos=
e link, fullscreen
driver =3D webdriver.Firefox()
driver.get(https://cmbdn.cognex.com/free-barcode-scanner)
driver.fullscreen_window()

wait =3D WebDriverWait(driver, 10, 1)  # Explicit wait

textFile =3D open("TEXT2.txt", "a") ####################

# method to unselect or uncheck barcode type box
def unselect2():
    # driver.implicitly_wait(10)

    element =3D wait.until(EC.element_to_be_clickable((By.XPATH, "/html/bod=
y/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/button")))
    element.click()

    element =3D wait.until(EC.element_to_be_clickable((By.XPATH, "/html/bod=
y/div[1]/div[3]/div[1]/div[1]/div[2]/div[4]/div[4]")))
    element.click()

    element =3D wait.until(EC.element_to_be_clickable((By.XPATH, "/html/bod=
y/div[1]/div[3]/div[1]/div[1]/div[2]/div[4]/div[8]")))
    element.click()

def scroll():
    location =3D driver.find_element(By.ID, "barcodeScanner")
    driver.execute_script("arguments[0].scrollIntoView(true);", location) #=
Scroll page to location

def selectIMG(): # Choose IMG and write to txt file - two functions in meth=
od

    numInt =3D 1941 ########## NUMBER FOR STARTING IMAGE
    plusUL =3D numInt + 20 # Plus Upper Limit - 20 Images
    counter =3D 1

    while numInt < plusUL: ########### NUMBER FOR ENDING IMAGE

        strCounter =3D str(counter)
        strNum =3D str(numInt)

        if len(strNum) =3D=3D 1:
            numName =3D '000' + strNum
        elif len(strNum) =3D=3D 2:
            numName =3D '00' + strNum
        elif len(strNum) =3D=3D 3:
            numName =3D '0' + strNum
        else:
            numName =3D strNum

        image_path =3D ("C:\\Users\\DrasonTruong\\source\\repos\\SeleniumPr=
ac\\202303_a_REDUCED\\IMG_" + numName + ".jpg") ########### CHANGE IMAGE PA=
TH TO DESIRED IMAGE DIR LOCATION
        driver.find_element(By.ID, "file-upload").send_keys(image_path)

        imgName =3D "IMG_" + numName + ".jpg"
        textFile.write(imgName + " ")

        try:
            textResult =3D driver.find_element(By.XPATH, "/html/body/div[1]=
/div[3]/div[1]/div[4]/div[2]/div/div[" + strCounter + "]/div[3]/div")

            newText =3D textResult.text
            textFile.write(newText)
            textFile.write("\n")
        except:
            # textFile.write(imgName)
            textFile.write("\n")

        numInt +=3D 1
        counter +=3D 1


# Main Driver Method
if __name__ =3D=3D "__main__":

    # long implicit wait at program start to hopefully load full page
    driver.implicitly_wait(10)

    # After opening browser

    # Set the page - scroll to correct location, select barcode types (Code=
 25)
    scroll()
    unselect2()

    # Upload IMG
    selectIMG()
