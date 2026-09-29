# Maze Path Finder


## Project Overview

Maze Path Finder is a Python project that takes a picture of a maze and tries to find a path from the starting point to the ending point.

The main idea behind this project is to make the computer understand a maze from an image. First, the image is processed and converted into a simpler black and white format so that the walls and open paths are easier to detect. After that, the program finds the maze structure, identifies the start and end points, and searches for a possible path between them.

This project combines basic Python programming, OpenCV image processing, and a path-finding algorithm to solve a maze.

## Features

* Takes a maze image as input from the user.
* Loads and displays the maze image.
* Converts the image into grayscale.
* Converts the image into black and white.
* Detects the main boundary of the maze.
* Identifies the walls and open paths.
* Finds the marked starting and ending points.
* Searches for a path between the start and end.
* Shows the final maze with the path.

## Technologies Used

* **Python** – Used to build the main program.
* **OpenCV (cv2)** – Used for reading and processing the maze image.
* **Collections / deque** – Used while searching for the path.
* **Git & GitHub** – Used to manage and submit the project.

## Project Workflow

The project works in the following steps:

```text
Maze Image
    ↓
Load Image
    ↓
Convert to Grayscale
    ↓
Convert to Black & White
    ↓
Detect Maze Boundary
    ↓
Detect Walls and Paths
    ↓
Find Start and End
    ↓
Find the Path
    ↓
Display the Result
```

## Requirements

To run this project, Python should be installed on the computer.

The required OpenCV library can be installed using:

```bash
pip install opencv-python
```

No other external software is required apart from Python and the required library.

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Install OpenCV using the command given above.
4. Run the Python file.

For example:

```bash
python "Maze Path Finder.py"
```

5. When the program asks for the image path, enter the location of your maze image.

Example:

```text
Enter the path of maze image: maze.jpg
```

6. The program will process the image and show the detected maze and the path.

## Input

The input is an image of a maze.

For the program to work properly, the image should have:

* Clearly visible maze walls
* Open paths
* A marked starting point
* A marked ending point

## Output

The program displays the processed maze image and shows the path found between the starting point and ending point.

This makes it easier to see how the program understood the maze and which route it selected.

## Testing

The project can be tested using different types of maze images.

Some examples are:

1. A simple maze with a short path.
2. A maze with multiple turns.
3. A maze with a longer path.
4. An invalid or incorrect image path.
5. A maze where there is no possible path between the start and end.

The program should also show an appropriate message if the image cannot be loaded.

## Project Structure

The project can be organized into different files so that each part of the program has a separate purpose.

```text
Maze-Path-Finder/
│
├── main.py
├── image_loader.py
├── image_processing.py
├── maze_detection.py
├── start_end_detection.py
├── path_finding.py
├── display.py
│
├── test_maze/
│   ├── maze1.jpg
│   └── maze2.jpg
│
└── README.md
```

Keeping the code in separate files makes it easier to understand, test, and make changes later.

## Future Improvements

There are several things that can be added to the project in the future:

* Improve the detection of the start and end points.
* Make the maze detection work with more types of images.
* Improve the accuracy of the path-finding process.
* Add a simple graphical user interface.
* Allow the user to select an image using a file picker instead of entering its path.
* Connect the software with an actual robotic car.
* Make the robot physically follow the path found by the program.

## Conclusion

Maze Path Finder is a simple attempt to solve a real-world type of problem using Python. It helped in understanding how images can be processed and how an algorithm can be used to find a path through a maze.

The project also gives a basic introduction to computer vision and shows how Python can be used together with OpenCV to build something practical.