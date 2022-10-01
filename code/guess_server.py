from concurrent import futures
import guessing_game_pb2 as pb2
import guessing_game_pb2_grpc as pb2_grpc
import random
import grpc

class GuessingGameServicer(pb2_grpc.GuessingGameServicer):
    
    def tell_name(self, request, context):
        message = request.message
        return pb2.Name(message)

    def Reply(self, request, context):
        msg = ""

        if(request.number > x):
            msg = "high"
            print(msg)

        elif(request.number < x):
            msg = "low"
            print(msg)

        else:
            msg =  "you won the game"
            print(msg)

        return pb2.Feedback(message = msg)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pb2_grpc.add_GuessingGameServicer_to_server(GuessingGameServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()

if __name__ ==  "__main__":
    x = random.randint(1, 100000)
    serve()

