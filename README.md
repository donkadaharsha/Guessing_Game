# guessing_game
# Donkada Harsha Vardhan

# docker-compose up --build to run and build application. It will create containers for Alice, Bob and Server.

# I have used 3 different files - for Alice(Alice.py), for Bob(Bob.py) and for server(guess_server.py)

# it generates a random integer at the beginning of the program n the Server side, and implement the 2 rpc calls defined in proto 
# it checks if the guess provided by client is less/greater/equal to the number that server itself generated and based on the guess value it returns the message to the client giving indication as low/high/you won the game.
# As soon as the client receives "you won the game", it prints "I am done" and exit the game silently while the other client continue
# to guess.
# Gif link of running application:



![ezgif com-gif-maker](https://user-images.githubusercontent.com/114453047/193425353-eb72d72f-282a-469e-8d1e-e34f72f3ca34.gif)
