# Futil
Futil is a handy Python based CLI tool that performs several useful functions to search/compare/decode/encodefiles. But wait, there is more! You can also extract EXIF and Metadata with F_util. This Runs on Windows, macOS, and Linux with the only requirement being python3. 

# Requirements:

Python3

If you do not have python3 install, follow the option below that matches your OS. 

# Windows:

Download the Python 3 installer from the official website (https://www.python.org/downloads/windows/) and run it.
   
# macOS:

Install Python 3 using Homebrew 
    
First, install Homebrew:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
    
then run 

    
    brew install python3 
Make this even easier by creating an alias:
    
     alias futil='python3 /Users/cmd/script_s/fileutil.py' >> ~/.zshrc

# Linux:

Use the package manager of your Linux distribution to install Python 3. *you can also use homebrew to install, see macOS install above
    
run the command 
    
     sudo apt-get install python3
Create alias to allow quick use by just typing "futil" from any where on your UNIX based machine, 
add the following line to your shell configuration file (e.g., ~/.bashrc or ~/.zshrc):

    echo 'alias futil="python3 /path/to/futil.py"' >> ~/.bashrc && source ~/.bashrc


# USAGE:

    futil
    
    
   
   ![image](https://user-images.githubusercontent.com/113065386/223303512-bf1142cc-c476-4ee8-9722-e4629c857f4d.png)

This can be used without setting an alias:

    cd futil
    
    python3 futil.py
    

Most of my tools are created to use during investigations to reduce time and increase efficency. In the event this tool or any tool I create to aid in an investigation, or if the ability or functionality were called in to question, I provide a functions breakdown of the tool used along with the results of the tool etc. You can see this function breakdown below. 

# Functions

# Compare Files

Compares two or more files and returns whether they are the same or different.  

![image](https://user-images.githubusercontent.com/113065386/223295495-4a50ba53-2356-4307-8b99-5f885e6a1832.png)




# Search File

Searches for a word in a file and returns the line number where it is found.

![image](https://user-images.githubusercontent.com/113065386/223295401-1667c1e5-f215-4850-83b2-6bbea6362619.png)



# Decode File

Decodes a file with the specified encoding and returns the content as a string.

![image](https://user-images.githubusercontent.com/113065386/223292346-0b078cfe-c2f4-46ef-bd5b-85ce90a08084.png)




# Encode File

Encodes a file with the specified encoding.

![image](https://user-images.githubusercontent.com/113065386/223292192-d4b65a5a-5a7e-4076-80a6-5d3e8c0a8d93.png)



# Unzip File

![image](https://user-images.githubusercontent.com/113065386/223292687-0c1d0691-a93c-4969-b502-05cb8b776adf.png)



# Extract EXIF

Extracts EXIF data from a file using the exiftool command line tool.

![image](https://user-images.githubusercontent.com/113065386/223292439-e0effb00-6936-4cf4-bbab-9dc3f2efcd2d.png)



# Extract Metadata

Extracts metadata from a file using the exiv2 command line tool.

![image](https://user-images.githubusercontent.com/113065386/223292546-09930269-0dcd-4bd0-a6f0-fa0f799ff4e5.png)



# Search URLs

Searches a file for URLs . 


![image](https://user-images.githubusercontent.com/113065386/223293021-afa05e84-48f1-4651-b836-f33c04515cd3.png)


If exiv2 is not installed and you receive an error, run:
      brew install exiv2
