# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Pittscord_ipc.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13Pittscord_ipc.proto\" \n\x0bJSONRequest\x12\x11\n\tserver_id\x18\x01 \x01(\x03\"\x1c\n\x0cJSONResponse\x12\x0c\n\x04json\x18\x01 \x01(\t\"\x1b\n\x0cHelloRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1c\n\rHelloResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1f\n\rConfigRequest\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\t\"\x1e\n\x0e\x43onfigResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x32\x97\x01\n\rPittscord_ipc\x12(\n\x07GetJSON\x12\x0c.JSONRequest\x1a\r.JSONResponse\"\x00\x12+\n\x08SayHello\x12\r.HelloRequest\x1a\x0e.HelloResponse\"\x00\x12/\n\nSendConfig\x12\x0e.ConfigRequest\x1a\x0f.ConfigResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Pittscord_ipc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_JSONREQUEST']._serialized_start=23
  _globals['_JSONREQUEST']._serialized_end=55
  _globals['_JSONRESPONSE']._serialized_start=57
  _globals['_JSONRESPONSE']._serialized_end=85
  _globals['_HELLOREQUEST']._serialized_start=87
  _globals['_HELLOREQUEST']._serialized_end=114
  _globals['_HELLORESPONSE']._serialized_start=116
  _globals['_HELLORESPONSE']._serialized_end=144
  _globals['_CONFIGREQUEST']._serialized_start=146
  _globals['_CONFIGREQUEST']._serialized_end=177
  _globals['_CONFIGRESPONSE']._serialized_start=179
  _globals['_CONFIGRESPONSE']._serialized_end=209
  _globals['_PITTSCORD_IPC']._serialized_start=212
  _globals['_PITTSCORD_IPC']._serialized_end=363
# @@protoc_insertion_point(module_scope)
