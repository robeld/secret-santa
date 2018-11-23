# secret-santa
Simple Secret Santa Python program. Uses the method described at https://www.youtube.com/watch?v=5kC5k5QBqcc:

1) Shuffle participants.
2) Copy the shuffled list of participants.
3) Shift the copy by 1.
4) Assign person i from the first list to person i in the second list.

Essentially, the list of participants is randomized and is treated like a circular array where each person buys for the next person. The copying is done for ease of reading, but only one list is needed.


Writes to a separate text file for each person, as well as a master key, but can be easily modified to e-mail anonymously if the CSV file inputted contains participants' e-mail addresses.
