# guessing_game
# Donkada Harsha Vardhan

# docker-compose up --build to run and build application. It will create containers for Alice, Bob and Server.

# I have used 3 different files - for Alice(Alice.py), for Bob(Bob.py) and for server(guess_server.py)

# it generates a random integer at the beginning of the program in the Server side. This shall implement the 2 rpc calls defined in proto 
# it checks if the guess provided by client is greater than or less than or equal to the number that server generated. Based on the guess value and comparision, it will return the message to client giving indication as 
# low - if guess is lower than server generated number
# high- if guess is grester than server generated number
# You won the game - iF it is equal to the server generated number.
# If one client receives "you won the game", it then prints "I am done" and will exit the game silently while the another client continues
# to guess.
# when the second client also guesses the number, it will print "You won the game" then "I am done" and the program will terminate.
# Bugs- Sometimes client exits with error code 139. 

# Gif link of running application:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/114453047/193425353-eb72d72f-282a-469e-8d1e-e34f72f3ca34.gif)
