#miniconda = lightweight version of conda, which is a package manager for Python and other languages. It allows you to create isolated environments for your projects, making it easier to manage dependencies and avoid conflicts.
FROM continuumio/miniconda3:latest

#Working directory for the container
WORKDIR /workspace

#Copy the environment.yml file into the container. This file contains the dependencies and packages required for the project.
COPY environment.yml .

#Create a new conda environment named AOC_2026 using the environment.yml file. This command will install all the dependencies specified in the file.
RUN conda env create -f environment.yml

#Activate conda env in bash sessions
SHELL ["/bin/bash", "--login", "-c"]
RUN echo "conda activate AOC_2026" >> ~/.bashrc

#default command to run 
CMD ["/bin/bash"]