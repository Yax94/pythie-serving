# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/node_def.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import full_type_pb2 as tensorflow_dot_core_dot_framework_dot_full__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(tensorflow/core/framework/node_def.proto\x12\ntensorflow\x1a*tensorflow/core/framework/attr_value.proto\x1a)tensorflow/core/framework/full_type.proto\"\x86\x03\n\x07NodeDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x03(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12+\n\x04\x61ttr\x18\x05 \x03(\x0b\x32\x1d.tensorflow.NodeDef.AttrEntry\x12J\n\x17\x65xperimental_debug_info\x18\x06 \x01(\x0b\x32).tensorflow.NodeDef.ExperimentalDebugInfo\x12\x32\n\x11\x65xperimental_type\x18\x07 \x01(\x0b\x32\x17.tensorflow.FullTypeDef\x1a\x42\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.tensorflow.AttrValue:\x02\x38\x01\x1aQ\n\x15\x45xperimentalDebugInfo\x12\x1b\n\x13original_node_names\x18\x01 \x03(\t\x12\x1b\n\x13original_func_names\x18\x02 \x03(\tB{\n\x18org.tensorflow.frameworkB\tNodeProtoP\x01ZOgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/node_def_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.framework.node_def_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\tNodeProtoP\001ZOgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/node_def_go_proto\370\001\001'
  _NODEDEF_ATTRENTRY._options = None
  _NODEDEF_ATTRENTRY._serialized_options = b'8\001'
  _NODEDEF._serialized_start=144
  _NODEDEF._serialized_end=534
  _NODEDEF_ATTRENTRY._serialized_start=385
  _NODEDEF_ATTRENTRY._serialized_end=451
  _NODEDEF_EXPERIMENTALDEBUGINFO._serialized_start=453
  _NODEDEF_EXPERIMENTALDEBUGINFO._serialized_end=534
# @@protoc_insertion_point(module_scope)
