<<<Fermat’s Last Theorem Near Miss Finder>>>


GETTING STARTED
        
        These instructions are intended to provide a copy of the project to the user so that they can run the program on their own machine.


PREREQUISITES


        The project requires Python 3.x. There are no additional requirements in the form of external files or plugins or the like. There are no external files created by this project.


RUNNING THE PROGRAM


        Navigate to the directory where “fermat’s_last_theorem_miss_finder.py” is located and run the project by entering the following command into the terminal, “python fermat’s_last_theorem_miss_finder.py”.


        Alternatively, you may be able to find the directory where the project “fermat’s_last_theorem_miss_finder.py” is located and run it manually from the GUI of your operating system. In the case of Windows, you may check your Downloads folder first and double click to run the program from there.


USAGE


        Once the program starts, the user is prompted to input values for n and k. The program validates these inputs to ensure they are numbers, with n being in the range (2, 12) and k greater than 10.


	The program iterates over possible x and y values, computes the sum of their powers, and calculates misses based on potential z values.


	The program provides progress updates and prints any near misses found. After the calculations are complete, the total number of near misses is printed along with the smallest identified miss.


	At the end, the user is given an option to run the program again.


OVERFLOW HANDLING AND OPTIMIZATION


	The program includes exception handling to manage potential overflow errors that might occur for large n and k values. It will print a message and skip the specific calculations causing the overflow to provide a more user-friendly and accessible experience over a more detailed output with steeper hardware requirements.


	Note: The current program runs in O(k^2) time complexity due to nested loops. Therefore, the program may take longer to run for large k values.


CONTACT


        For any questions or queries please contact me at andrewjmilligan@lewisu.edu


RESOURCES


        Numberfile on Youtube, www.geeksforgeeks.org, www.w3schools.com