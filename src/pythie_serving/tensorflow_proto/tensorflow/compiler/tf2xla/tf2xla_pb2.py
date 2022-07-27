# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/tf2xla/tf2xla.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'tensorflow/compiler/tf2xla/tf2xla.proto\x12\x11tensorflow.tf2xla\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"3\n\x08TensorId\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x14\n\x0coutput_index\x18\x02 \x01(\x03\"\x8e\x01\n\x04\x46\x65\x65\x64\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.tensorflow.tf2xla.TensorId\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\"\x8f\x01\n\x05\x46\x65tch\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.tensorflow.tf2xla.TensorId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\"\x8e\x01\n\x08Variable\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\"\n\x04type\x18\x04 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x10\n\x08readonly\x18\x05 \x01(\x08\"7\n\x11\x43onversionOptions\x12\"\n\x1a\x63ustom_fake_quant_op_calls\x18\x01 \x01(\x08\"\xc9\x01\n\x06\x43onfig\x12%\n\x04\x66\x65\x65\x64\x18\x01 \x03(\x0b\x32\x17.tensorflow.tf2xla.Feed\x12\'\n\x05\x66\x65tch\x18\x02 \x03(\x0b\x32\x18.tensorflow.tf2xla.Fetch\x12-\n\x08variable\x18\x03 \x03(\x0b\x32\x1b.tensorflow.tf2xla.Variable\x12@\n\x12\x63onversion_options\x18\x04 \x01(\x0b\x32$.tensorflow.tf2xla.ConversionOptionsB*\n\x15org.tensorflow.tf2xlaB\x0cTf2XlaProtosP\x01\xf8\x01\x01\x62\x06proto3')



_TENSORID = DESCRIPTOR.message_types_by_name['TensorId']
_FEED = DESCRIPTOR.message_types_by_name['Feed']
_FETCH = DESCRIPTOR.message_types_by_name['Fetch']
_VARIABLE = DESCRIPTOR.message_types_by_name['Variable']
_CONVERSIONOPTIONS = DESCRIPTOR.message_types_by_name['ConversionOptions']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
TensorId = _reflection.GeneratedProtocolMessageType('TensorId', (_message.Message,), {
  'DESCRIPTOR' : _TENSORID,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.TensorId)
  })
_sym_db.RegisterMessage(TensorId)

Feed = _reflection.GeneratedProtocolMessageType('Feed', (_message.Message,), {
  'DESCRIPTOR' : _FEED,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Feed)
  })
_sym_db.RegisterMessage(Feed)

Fetch = _reflection.GeneratedProtocolMessageType('Fetch', (_message.Message,), {
  'DESCRIPTOR' : _FETCH,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Fetch)
  })
_sym_db.RegisterMessage(Fetch)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLE,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Variable)
  })
_sym_db.RegisterMessage(Variable)

ConversionOptions = _reflection.GeneratedProtocolMessageType('ConversionOptions', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONOPTIONS,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.ConversionOptions)
  })
_sym_db.RegisterMessage(ConversionOptions)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'tensorflow.compiler.tf2xla.tf2xla_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025org.tensorflow.tf2xlaB\014Tf2XlaProtosP\001\370\001\001'
  _TENSORID._serialized_start=147
  _TENSORID._serialized_end=198
  _FEED._serialized_start=201
  _FEED._serialized_end=343
  _FETCH._serialized_start=346
  _FETCH._serialized_end=489
  _VARIABLE._serialized_start=492
  _VARIABLE._serialized_end=634
  _CONVERSIONOPTIONS._serialized_start=636
  _CONVERSIONOPTIONS._serialized_end=691
  _CONFIG._serialized_start=694
  _CONFIG._serialized_end=895
# @@protoc_insertion_point(module_scope)
