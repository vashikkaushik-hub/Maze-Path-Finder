# Problem Statement


## Problem Statement

Finding the correct way through a maze can be difficult when there are many paths and turns. If a robot has to solve the maze, it first needs to understand where the walls and paths are and where it has to start and finish.

In this project, the aim is to make a Python program that can take a picture of a maze and try to find a path from the starting point to the ending point. The program processes the image and uses the information from it to understand the basic structure of the maze.

The maze image is changed into a simpler form so that the walls and paths can be detected more easily. After finding the maze structure, starting point and ending point, the program searches for a possible route between them.

## Scope of the Project

This project mainly focuses on solving a maze from an image.

The project includes:

Taking a maze image as input.
Loading and processing the image using Python and OpenCV.
Converting the image into grayscale.
Converting the grayscale image into black and white.
Detecting the main boundary and walls of the maze.
Finding the marked starting and ending points.
Searching for a possible path between the two points.
Displaying the processed maze and the result.

At the current stage, the project is a software-based maze solver. It does not physically control a robot. Connecting the program to a real robot can be considered as a future improvement.

## Target Users

This project can be useful for:

Students who are learning Python.
Beginners who want to learn basic image processing.
Students interested in robotics and automation.
Students learning maze-solving and path-finding algorithms.
Anyone interested in trying a simple automated maze solver.

## High-Level Features

### 1. Maze Image Input

The user gives the path of the maze image to the program. The program loads the image and checks if it was loaded successfully.

### 2. Image Processing

The image is processed using OpenCV. First, it is converted into grayscale and then into black and white. This makes it easier for the program to work with the maze walls and paths.

### 3. Maze Detection

The program tries to detect the main boundary of the maze and identify the walls and open areas inside it.

### 4. Start and End Detection

The maze image contains marked starting and ending points. The program uses these points to determine where the path should start and where it should finish.

### 5. Path Finding

Once the maze and the start and end points are identified, the program searches for a possible path between them.

### 6. Result Display

After processing the maze, the program displays the result so that the user can see the maze and the path found by the program.

## Expected Outcome

The expected result of this project is a program that can take a maze image, process it, and find a possible path between the marked starting and ending points.

Through this project, we can also understand the basic use of Python, OpenCV, image processing, and path-finding concepts in a practical project.