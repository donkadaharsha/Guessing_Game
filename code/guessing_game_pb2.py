# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guessing_game.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13guessing_game.proto\x12\rguessing_game\"\x17\n\x05Guess\x12\x0e\n\x06number\x18\x01 \x01(\x05\"\x1b\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x04Name\x12\x0f\n\x07message\x18\x01 \x01(\t2\x81\x01\n\x0cGuessingGame\x12\x38\n\x05Reply\x12\x14.guessing_game.Guess\x1a\x17.guessing_game.Feedback\"\x00\x12\x37\n\ttell_name\x12\x13.guessing_game.Name\x1a\x13.guessing_game.Name\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'guessing_game_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GUESS._serialized_start=38
  _GUESS._serialized_end=61
  _FEEDBACK._serialized_start=63
  _FEEDBACK._serialized_end=90
  _NAME._serialized_start=92
  _NAME._serialized_end=115
  _GUESSINGGAME._serialized_start=118
  _GUESSINGGAME._serialized_end=247
# @@protoc_insertion_point(module_scope)
