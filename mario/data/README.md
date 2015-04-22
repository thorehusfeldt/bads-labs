# Race tracks for Super Vector Mario!

Here is a simple input file for a 3x3 race track:

    3
    3
    OOO
    S F
    OOO

In general, the input form is:

    Number of rows
    Number of colums
    Row 1
    Row 2
    etc.

Each row description consists of a sequence of letters with the following intended meaning:

    F A finish square
    S The starting square
    (space) Somewhere that Mario can land
    O Offroad square (Mario can’t land here)

Each input file comes with a correspondingly named output file that contains just  a single integer, the optimal number of moves Mario needs to get from S to any of the Fs.
(We count the first move, where Mario is standing still.)
