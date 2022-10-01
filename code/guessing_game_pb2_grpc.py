# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import code.guessing_game_pb2 as guessing__game__pb2


class GuessingGameStub(object):
    """service ran on the server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reply = channel.unary_unary(
                '/guessing_game.GuessingGame/Reply',
                request_serializer=guessing__game__pb2.Guess.SerializeToString,
                response_deserializer=guessing__game__pb2.Feedback.FromString,
                )
        self.tell_name = channel.unary_unary(
                '/guessing_game.GuessingGame/tell_name',
                request_serializer=guessing__game__pb2.Name.SerializeToString,
                response_deserializer=guessing__game__pb2.Name.FromString,
                )


class GuessingGameServicer(object):
    """service ran on the server
    """

    def Reply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def tell_name(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GuessingGameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Reply': grpc.unary_unary_rpc_method_handler(
                    servicer.Reply,
                    request_deserializer=guessing__game__pb2.Guess.FromString,
                    response_serializer=guessing__game__pb2.Feedback.SerializeToString,
            ),
            'tell_name': grpc.unary_unary_rpc_method_handler(
                    servicer.tell_name,
                    request_deserializer=guessing__game__pb2.Name.FromString,
                    response_serializer=guessing__game__pb2.Name.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'guessing_game.GuessingGame', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GuessingGame(object):
    """service ran on the server
    """

    @staticmethod
    def Reply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/guessing_game.GuessingGame/Reply',
            guessing__game__pb2.Guess.SerializeToString,
            guessing__game__pb2.Feedback.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def tell_name(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/guessing_game.GuessingGame/tell_name',
            guessing__game__pb2.Name.SerializeToString,
            guessing__game__pb2.Name.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
