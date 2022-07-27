# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/tensor_bundle.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_slice_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__slice__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import versions_pb2 as tensorflow_dot_core_dot_framework_dot_versions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,tensorflow/core/protobuf/tensor_bundle.proto\x12\ntensorflow\x1a,tensorflow/core/framework/tensor_shape.proto\x1a,tensorflow/core/framework/tensor_slice.proto\x1a%tensorflow/core/framework/types.proto\x1a(tensorflow/core/framework/versions.proto\"\xb1\x01\n\x11\x42undleHeaderProto\x12\x12\n\nnum_shards\x18\x01 \x01(\x05\x12<\n\nendianness\x18\x02 \x01(\x0e\x32(.tensorflow.BundleHeaderProto.Endianness\x12\'\n\x07version\x18\x03 \x01(\x0b\x32\x16.tensorflow.VersionDef\"!\n\nEndianness\x12\n\n\x06LITTLE\x10\x00\x12\x07\n\x03\x42IG\x10\x01\"\xd2\x01\n\x10\x42undleEntryProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x10\n\x08shard_id\x18\x03 \x01(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x03\x12\x0c\n\x04size\x18\x05 \x01(\x03\x12\x0e\n\x06\x63rc32c\x18\x06 \x01(\x07\x12,\n\x06slices\x18\x07 \x03(\x0b\x32\x1c.tensorflow.TensorSliceProtoB\x85\x01\n\x13org.tensorflow.utilB\x12TensorBundleProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')



_BUNDLEHEADERPROTO = DESCRIPTOR.message_types_by_name['BundleHeaderProto']
_BUNDLEENTRYPROTO = DESCRIPTOR.message_types_by_name['BundleEntryProto']
_BUNDLEHEADERPROTO_ENDIANNESS = _BUNDLEHEADERPROTO.enum_types_by_name['Endianness']
BundleHeaderProto = _reflection.GeneratedProtocolMessageType('BundleHeaderProto', (_message.Message,), {
  'DESCRIPTOR' : _BUNDLEHEADERPROTO,
  '__module__' : 'tensorflow.core.protobuf.tensor_bundle_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BundleHeaderProto)
  })
_sym_db.RegisterMessage(BundleHeaderProto)

BundleEntryProto = _reflection.GeneratedProtocolMessageType('BundleEntryProto', (_message.Message,), {
  'DESCRIPTOR' : _BUNDLEENTRYPROTO,
  '__module__' : 'tensorflow.core.protobuf.tensor_bundle_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BundleEntryProto)
  })
_sym_db.RegisterMessage(BundleEntryProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023org.tensorflow.utilB\022TensorBundleProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'
  _BUNDLEHEADERPROTO._serialized_start=234
  _BUNDLEHEADERPROTO._serialized_end=411
  _BUNDLEHEADERPROTO_ENDIANNESS._serialized_start=378
  _BUNDLEHEADERPROTO_ENDIANNESS._serialized_end=411
  _BUNDLEENTRYPROTO._serialized_start=414
  _BUNDLEENTRYPROTO._serialized_end=624
# @@protoc_insertion_point(module_scope)
