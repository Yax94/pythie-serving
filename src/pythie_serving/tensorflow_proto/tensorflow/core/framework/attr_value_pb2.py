# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/attr_value.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*tensorflow/core/framework/attr_value.proto\x12\ntensorflow\x1a&tensorflow/core/framework/tensor.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"\xa6\x04\n\tAttrValue\x12\x0b\n\x01s\x18\x02 \x01(\x0cH\x00\x12\x0b\n\x01i\x18\x03 \x01(\x03H\x00\x12\x0b\n\x01\x66\x18\x04 \x01(\x02H\x00\x12\x0b\n\x01\x62\x18\x05 \x01(\x08H\x00\x12$\n\x04type\x18\x06 \x01(\x0e\x32\x14.tensorflow.DataTypeH\x00\x12-\n\x05shape\x18\x07 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProtoH\x00\x12)\n\x06tensor\x18\x08 \x01(\x0b\x32\x17.tensorflow.TensorProtoH\x00\x12/\n\x04list\x18\x01 \x01(\x0b\x32\x1f.tensorflow.AttrValue.ListValueH\x00\x12(\n\x04\x66unc\x18\n \x01(\x0b\x32\x18.tensorflow.NameAttrListH\x00\x12\x15\n\x0bplaceholder\x18\t \x01(\tH\x00\x1a\xe9\x01\n\tListValue\x12\t\n\x01s\x18\x02 \x03(\x0c\x12\r\n\x01i\x18\x03 \x03(\x03\x42\x02\x10\x01\x12\r\n\x01\x66\x18\x04 \x03(\x02\x42\x02\x10\x01\x12\r\n\x01\x62\x18\x05 \x03(\x08\x42\x02\x10\x01\x12&\n\x04type\x18\x06 \x03(\x0e\x32\x14.tensorflow.DataTypeB\x02\x10\x01\x12+\n\x05shape\x18\x07 \x03(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\'\n\x06tensor\x18\x08 \x03(\x0b\x32\x17.tensorflow.TensorProto\x12&\n\x04\x66unc\x18\t \x03(\x0b\x32\x18.tensorflow.NameAttrListB\x07\n\x05value\"\x92\x01\n\x0cNameAttrList\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x04\x61ttr\x18\x02 \x03(\x0b\x32\".tensorflow.NameAttrList.AttrEntry\x1a\x42\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.tensorflow.AttrValue:\x02\x38\x01\x42\x83\x01\n\x18org.tensorflow.frameworkB\x0f\x41ttrValueProtosP\x01ZQgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/attr_value_go_proto\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.framework.attr_value_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030org.tensorflow.frameworkB\017AttrValueProtosP\001ZQgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/attr_value_go_proto\370\001\001'
  _ATTRVALUE_LISTVALUE.fields_by_name['i']._options = None
  _ATTRVALUE_LISTVALUE.fields_by_name['i']._serialized_options = b'\020\001'
  _ATTRVALUE_LISTVALUE.fields_by_name['f']._options = None
  _ATTRVALUE_LISTVALUE.fields_by_name['f']._serialized_options = b'\020\001'
  _ATTRVALUE_LISTVALUE.fields_by_name['b']._options = None
  _ATTRVALUE_LISTVALUE.fields_by_name['b']._serialized_options = b'\020\001'
  _ATTRVALUE_LISTVALUE.fields_by_name['type']._options = None
  _ATTRVALUE_LISTVALUE.fields_by_name['type']._serialized_options = b'\020\001'
  _NAMEATTRLIST_ATTRENTRY._options = None
  _NAMEATTRLIST_ATTRENTRY._serialized_options = b'8\001'
  _ATTRVALUE._serialized_start=184
  _ATTRVALUE._serialized_end=734
  _ATTRVALUE_LISTVALUE._serialized_start=492
  _ATTRVALUE_LISTVALUE._serialized_end=725
  _NAMEATTRLIST._serialized_start=737
  _NAMEATTRLIST._serialized_end=883
  _NAMEATTRLIST_ATTRENTRY._serialized_start=817
  _NAMEATTRLIST_ATTRENTRY._serialized_end=883
# @@protoc_insertion_point(module_scope)
