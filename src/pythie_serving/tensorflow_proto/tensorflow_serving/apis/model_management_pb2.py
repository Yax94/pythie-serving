# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/model_management.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow_serving.apis import status_pb2 as tensorflow__serving_dot_apis_dot_status__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.config import model_server_config_pb2 as tensorflow__serving_dot_config_dot_model__server__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.tensorflow_serving/apis/model_management.proto\x12\x12tensorflow.serving\x1a$tensorflow_serving/apis/status.proto\x1a\x33tensorflow_serving/config/model_server_config.proto\"L\n\x13ReloadConfigRequest\x12\x35\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.tensorflow.serving.ModelServerConfig\"G\n\x14ReloadConfigResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x1f.tensorflow.serving.StatusProtoB\x03\xf8\x01\x01\x62\x06proto3')



_RELOADCONFIGREQUEST = DESCRIPTOR.message_types_by_name['ReloadConfigRequest']
_RELOADCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ReloadConfigResponse']
ReloadConfigRequest = _reflection.GeneratedProtocolMessageType('ReloadConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELOADCONFIGREQUEST,
  '__module__' : 'tensorflow_serving.apis.model_management_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ReloadConfigRequest)
  })
_sym_db.RegisterMessage(ReloadConfigRequest)

ReloadConfigResponse = _reflection.GeneratedProtocolMessageType('ReloadConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _RELOADCONFIGRESPONSE,
  '__module__' : 'tensorflow_serving.apis.model_management_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ReloadConfigResponse)
  })
_sym_db.RegisterMessage(ReloadConfigResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _RELOADCONFIGREQUEST._serialized_start=161
  _RELOADCONFIGREQUEST._serialized_end=237
  _RELOADCONFIGRESPONSE._serialized_start=239
  _RELOADCONFIGRESPONSE._serialized_end=310
# @@protoc_insertion_point(module_scope)
