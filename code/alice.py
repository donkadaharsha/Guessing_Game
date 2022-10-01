import guessing_game_pb2
import guessing_game_pb2_grpc
import grpc
import random
import sys


def run(num):
    sys.setrecursionlimit(100000)
    with grpc.insecure_channel('server:50051') as channel:
        stub = guessing_game_pb2_grpc.GuessingGameStub(channel)
        number = num
        print("Guess:",   number)

        response = stub.Reply(guessing_game_pb2.Guess(number = number))

        if response.message == "low":
            num = random.randint(number,100000)
            run(num)
        elif response.message == "high":
            num = random.randint(1,number)
            run(num)
        else:
            print("I am done")
            channel.close()
        

def close(channel):
    channel.close()

if __name__ == "__main__":
    number = random.randint(1,100000)
    run(number)