# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/kernel_def.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*tensorflow/core/framework/kernel_def.proto\x12\ntensorflow\x1a*tensorflow/core/framework/attr_value.proto\"\xef\x01\n\tKernelDef\x12\n\n\x02op\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x02 \x01(\t\x12\x38\n\nconstraint\x18\x03 \x03(\x0b\x32$.tensorflow.KernelDef.AttrConstraint\x12\x17\n\x0fhost_memory_arg\x18\x04 \x03(\t\x12\r\n\x05label\x18\x05 \x01(\t\x12\x10\n\x08priority\x18\x06 \x01(\x05\x1aM\n\x0e\x41ttrConstraint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x0e\x61llowed_values\x18\x02 \x01(\x0b\x32\x15.tensorflow.AttrValue\"3\n\nKernelList\x12%\n\x06kernel\x18\x01 \x03(\x0b\x32\x15.tensorflow.KernelDefB\x83\x01\n\x18org.tensorflow.frameworkB\x0fKernelDefProtosP\x01ZQgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/kernel_def_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.framework.kernel_def_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\017KernelDefProtosP\001ZQgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/kernel_def_go_proto\370\001\001'
  _KERNELDEF._serialized_start=103
  _KERNELDEF._serialized_end=342
  _KERNELDEF_ATTRCONSTRAINT._serialized_start=265
  _KERNELDEF_ATTRCONSTRAINT._serialized_end=342
  _KERNELLIST._serialized_start=344
  _KERNELLIST._serialized_end=395
# @@protoc_insertion_point(module_scope)
