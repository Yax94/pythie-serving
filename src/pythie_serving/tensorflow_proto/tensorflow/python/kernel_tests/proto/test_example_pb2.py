# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/python/kernel_tests/proto/test_example.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7tensorflow/python/kernel_tests/proto/test_example.proto\x12\x18tensorflow.contrib.proto\x1a%tensorflow/core/framework/types.proto\"\x93\x01\n\x08TestCase\x12\x33\n\x06values\x18\x01 \x03(\x0b\x32#.tensorflow.contrib.proto.TestValue\x12\x0e\n\x06shapes\x18\x02 \x03(\x05\x12\r\n\x05sizes\x18\x03 \x03(\x05\x12\x33\n\x06\x66ields\x18\x04 \x03(\x0b\x32#.tensorflow.contrib.proto.FieldSpec\"r\n\tFieldSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x32\n\x05value\x18\x03 \x01(\x0b\x32#.tensorflow.contrib.proto.TestValue\"\xf2\x08\n\tTestValue\x12\x14\n\x0c\x64ouble_value\x18\x01 \x03(\x01\x12\x13\n\x0b\x66loat_value\x18\x02 \x03(\x02\x12\x13\n\x0bint64_value\x18\x03 \x03(\x03\x12\x14\n\x0cuint64_value\x18\x04 \x03(\x04\x12\x13\n\x0bint32_value\x18\x05 \x03(\x05\x12\x15\n\rfixed64_value\x18\x06 \x03(\x06\x12\x15\n\rfixed32_value\x18\x07 \x03(\x07\x12\x12\n\nbool_value\x18\x08 \x03(\x08\x12\x14\n\x0cstring_value\x18\t \x03(\t\x12\x13\n\x0b\x62ytes_value\x18\x0c \x03(\x0c\x12\x14\n\x0cuint32_value\x18\r \x03(\r\x12\x16\n\x0esfixed32_value\x18\x0f \x03(\x0f\x12\x16\n\x0esfixed64_value\x18\x10 \x03(\x10\x12\x14\n\x0csint32_value\x18\x11 \x03(\x11\x12\x14\n\x0csint64_value\x18\x12 \x03(\x12\x12?\n\rmessage_value\x18\x13 \x03(\x0b\x32(.tensorflow.contrib.proto.PrimitiveValue\x12\x33\n\nenum_value\x18# \x03(\x0e\x32\x1f.tensorflow.contrib.proto.Color\x12$\n\x19\x64ouble_value_with_default\x18\x14 \x01(\x01:\x01\x31\x12#\n\x18\x66loat_value_with_default\x18\x15 \x01(\x02:\x01\x32\x12#\n\x18int64_value_with_default\x18\x16 \x01(\x03:\x01\x33\x12$\n\x19uint64_value_with_default\x18\x17 \x01(\x04:\x01\x34\x12#\n\x18int32_value_with_default\x18\x18 \x01(\x05:\x01\x35\x12%\n\x1a\x66ixed64_value_with_default\x18\x19 \x01(\x06:\x01\x36\x12%\n\x1a\x66ixed32_value_with_default\x18\x1a \x01(\x07:\x01\x37\x12%\n\x17\x62ool_value_with_default\x18\x1b \x01(\x08:\x04true\x12$\n\x19string_value_with_default\x18\x1c \x01(\t:\x01\x61\x12\x39\n\x18\x62ytes_value_with_default\x18\x1d \x01(\x0c:\x17\x61 longer default string\x12$\n\x19uint32_value_with_default\x18\x1e \x01(\r:\x01\x39\x12\'\n\x1bsfixed32_value_with_default\x18\x1f \x01(\x0f:\x02\x31\x30\x12\'\n\x1bsfixed64_value_with_default\x18  \x01(\x10:\x02\x31\x31\x12%\n\x19sint32_value_with_default\x18! \x01(\x11:\x02\x31\x32\x12%\n\x19sint64_value_with_default\x18\" \x01(\x12:\x02\x31\x33\x12G\n\x17\x65num_value_with_default\x18$ \x01(\x0e\x32\x1f.tensorflow.contrib.proto.Color:\x05GREEN*\x05\x08\x64\x10\xc8\x01\"\xa5\t\n\x0fPackedTestValue\x12\x18\n\x0c\x64ouble_value\x18\x01 \x03(\x01\x42\x02\x10\x01\x12\x17\n\x0b\x66loat_value\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x17\n\x0bint64_value\x18\x03 \x03(\x03\x42\x02\x10\x01\x12\x18\n\x0cuint64_value\x18\x04 \x03(\x04\x42\x02\x10\x01\x12\x17\n\x0bint32_value\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x19\n\rfixed64_value\x18\x06 \x03(\x06\x42\x02\x10\x01\x12\x19\n\rfixed32_value\x18\x07 \x03(\x07\x42\x02\x10\x01\x12\x16\n\nbool_value\x18\x08 \x03(\x08\x42\x02\x10\x01\x12\x14\n\x0cstring_value\x18\t \x03(\t\x12\x13\n\x0b\x62ytes_value\x18\x0c \x03(\x0c\x12\x18\n\x0cuint32_value\x18\r \x03(\rB\x02\x10\x01\x12\x1a\n\x0esfixed32_value\x18\x0f \x03(\x0f\x42\x02\x10\x01\x12\x1a\n\x0esfixed64_value\x18\x10 \x03(\x10\x42\x02\x10\x01\x12\x18\n\x0csint32_value\x18\x11 \x03(\x11\x42\x02\x10\x01\x12\x18\n\x0csint64_value\x18\x12 \x03(\x12\x42\x02\x10\x01\x12?\n\rmessage_value\x18\x13 \x03(\x0b\x32(.tensorflow.contrib.proto.PrimitiveValue\x12\x33\n\nenum_value\x18# \x03(\x0e\x32\x1f.tensorflow.contrib.proto.Color\x12$\n\x19\x64ouble_value_with_default\x18\x14 \x01(\x01:\x01\x31\x12#\n\x18\x66loat_value_with_default\x18\x15 \x01(\x02:\x01\x32\x12#\n\x18int64_value_with_default\x18\x16 \x01(\x03:\x01\x33\x12$\n\x19uint64_value_with_default\x18\x17 \x01(\x04:\x01\x34\x12#\n\x18int32_value_with_default\x18\x18 \x01(\x05:\x01\x35\x12%\n\x1a\x66ixed64_value_with_default\x18\x19 \x01(\x06:\x01\x36\x12%\n\x1a\x66ixed32_value_with_default\x18\x1a \x01(\x07:\x01\x37\x12%\n\x17\x62ool_value_with_default\x18\x1b \x01(\x08:\x04true\x12$\n\x19string_value_with_default\x18\x1c \x01(\t:\x01\x61\x12\x39\n\x18\x62ytes_value_with_default\x18\x1d \x01(\x0c:\x17\x61 longer default string\x12$\n\x19uint32_value_with_default\x18\x1e \x01(\r:\x01\x39\x12\'\n\x1bsfixed32_value_with_default\x18\x1f \x01(\x0f:\x02\x31\x30\x12\'\n\x1bsfixed64_value_with_default\x18  \x01(\x10:\x02\x31\x31\x12%\n\x19sint32_value_with_default\x18! \x01(\x11:\x02\x31\x32\x12%\n\x19sint64_value_with_default\x18\" \x01(\x12:\x02\x31\x33\x12G\n\x17\x65num_value_with_default\x18$ \x01(\x0e\x32\x1f.tensorflow.contrib.proto.Color:\x05GREEN\"\xda\x02\n\x0ePrimitiveValue\x12\x14\n\x0c\x64ouble_value\x18\x01 \x01(\x01\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x02\x12\x13\n\x0bint64_value\x18\x03 \x01(\x03\x12\x14\n\x0cuint64_value\x18\x04 \x01(\x04\x12\x13\n\x0bint32_value\x18\x05 \x01(\x05\x12\x15\n\rfixed64_value\x18\x06 \x01(\x06\x12\x15\n\rfixed32_value\x18\x07 \x01(\x07\x12\x12\n\nbool_value\x18\x08 \x01(\x08\x12\x14\n\x0cstring_value\x18\t \x01(\t\x12\x13\n\x0b\x62ytes_value\x18\x0c \x01(\x0c\x12\x14\n\x0cuint32_value\x18\r \x01(\r\x12\x16\n\x0esfixed32_value\x18\x0f \x01(\x0f\x12\x16\n\x0esfixed64_value\x18\x10 \x01(\x10\x12\x14\n\x0csint32_value\x18\x11 \x01(\x11\x12\x14\n\x0csint64_value\x18\x12 \x01(\x12\"9\n\x0b\x45xtraFields\x12\x15\n\x0cstring_value\x18\xf0\r \x01(\t\x12\x13\n\nbool_value\x18\xf1\r \x01(\x08\">\n\x11InnerMessageValue\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x02\x12\x14\n\x0c\x62ytes_values\x18\x08 \x03(\x0c\"\x84\x01\n\x12MiddleMessageValue\x12\x14\n\x0cint32_values\x18\x05 \x03(\x05\x12\x42\n\rmessage_value\x18\x0b \x01(\x0b\x32+.tensorflow.contrib.proto.InnerMessageValue\x12\x14\n\x0cuint32_value\x18\r \x01(\r\"i\n\x0cMessageValue\x12\x14\n\x0c\x64ouble_value\x18\x01 \x01(\x01\x12\x43\n\rmessage_value\x18\x0b \x01(\x0b\x32,.tensorflow.contrib.proto.MiddleMessageValue\"\xb2\x01\n\x14RepeatedMessageValue\x12Y\n\x0emessage_values\x18\x0b \x03(\x0b\x32\x41.tensorflow.contrib.proto.RepeatedMessageValue.NestedMessageValue\x1a?\n\x12NestedMessageValue\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x02\x12\x14\n\x0c\x62ytes_values\x18\x08 \x03(\x0c*U\n\x05\x43olor\x12\x07\n\x03RED\x10\x00\x12\n\n\x06ORANGE\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\x08\n\x04\x42LUE\x10\x04\x12\n\n\x06INDIGO\x10\x05\x12\n\n\x06VIOLET\x10\x06:`\n\text_value\x12#.tensorflow.contrib.proto.TestValue\x18\x64 \x03(\x0b\x32(.tensorflow.contrib.proto.PrimitiveValue')

_COLOR = DESCRIPTOR.enum_types_by_name['Color']
Color = enum_type_wrapper.EnumTypeWrapper(_COLOR)
RED = 0
ORANGE = 1
YELLOW = 2
GREEN = 3
BLUE = 4
INDIGO = 5
VIOLET = 6

EXT_VALUE_FIELD_NUMBER = 100
ext_value = DESCRIPTOR.extensions_by_name['ext_value']

_TESTCASE = DESCRIPTOR.message_types_by_name['TestCase']
_FIELDSPEC = DESCRIPTOR.message_types_by_name['FieldSpec']
_TESTVALUE = DESCRIPTOR.message_types_by_name['TestValue']
_PACKEDTESTVALUE = DESCRIPTOR.message_types_by_name['PackedTestValue']
_PRIMITIVEVALUE = DESCRIPTOR.message_types_by_name['PrimitiveValue']
_EXTRAFIELDS = DESCRIPTOR.message_types_by_name['ExtraFields']
_INNERMESSAGEVALUE = DESCRIPTOR.message_types_by_name['InnerMessageValue']
_MIDDLEMESSAGEVALUE = DESCRIPTOR.message_types_by_name['MiddleMessageValue']
_MESSAGEVALUE = DESCRIPTOR.message_types_by_name['MessageValue']
_REPEATEDMESSAGEVALUE = DESCRIPTOR.message_types_by_name['RepeatedMessageValue']
_REPEATEDMESSAGEVALUE_NESTEDMESSAGEVALUE = _REPEATEDMESSAGEVALUE.nested_types_by_name['NestedMessageValue']
TestCase = _reflection.GeneratedProtocolMessageType('TestCase', (_message.Message,), {
  'DESCRIPTOR' : _TESTCASE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.TestCase)
  })
_sym_db.RegisterMessage(TestCase)

FieldSpec = _reflection.GeneratedProtocolMessageType('FieldSpec', (_message.Message,), {
  'DESCRIPTOR' : _FIELDSPEC,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.FieldSpec)
  })
_sym_db.RegisterMessage(FieldSpec)

TestValue = _reflection.GeneratedProtocolMessageType('TestValue', (_message.Message,), {
  'DESCRIPTOR' : _TESTVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.TestValue)
  })
_sym_db.RegisterMessage(TestValue)

PackedTestValue = _reflection.GeneratedProtocolMessageType('PackedTestValue', (_message.Message,), {
  'DESCRIPTOR' : _PACKEDTESTVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.PackedTestValue)
  })
_sym_db.RegisterMessage(PackedTestValue)

PrimitiveValue = _reflection.GeneratedProtocolMessageType('PrimitiveValue', (_message.Message,), {
  'DESCRIPTOR' : _PRIMITIVEVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.PrimitiveValue)
  })
_sym_db.RegisterMessage(PrimitiveValue)

ExtraFields = _reflection.GeneratedProtocolMessageType('ExtraFields', (_message.Message,), {
  'DESCRIPTOR' : _EXTRAFIELDS,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.ExtraFields)
  })
_sym_db.RegisterMessage(ExtraFields)

InnerMessageValue = _reflection.GeneratedProtocolMessageType('InnerMessageValue', (_message.Message,), {
  'DESCRIPTOR' : _INNERMESSAGEVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.InnerMessageValue)
  })
_sym_db.RegisterMessage(InnerMessageValue)

MiddleMessageValue = _reflection.GeneratedProtocolMessageType('MiddleMessageValue', (_message.Message,), {
  'DESCRIPTOR' : _MIDDLEMESSAGEVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.MiddleMessageValue)
  })
_sym_db.RegisterMessage(MiddleMessageValue)

MessageValue = _reflection.GeneratedProtocolMessageType('MessageValue', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.MessageValue)
  })
_sym_db.RegisterMessage(MessageValue)

RepeatedMessageValue = _reflection.GeneratedProtocolMessageType('RepeatedMessageValue', (_message.Message,), {

  'NestedMessageValue' : _reflection.GeneratedProtocolMessageType('NestedMessageValue', (_message.Message,), {
    'DESCRIPTOR' : _REPEATEDMESSAGEVALUE_NESTEDMESSAGEVALUE,
    '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.RepeatedMessageValue.NestedMessageValue)
    })
  ,
  'DESCRIPTOR' : _REPEATEDMESSAGEVALUE,
  '__module__' : 'tensorflow.python.kernel_tests.proto.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.proto.RepeatedMessageValue)
  })
_sym_db.RegisterMessage(RepeatedMessageValue)
_sym_db.RegisterMessage(RepeatedMessageValue.NestedMessageValue)

if _descriptor._USE_C_DESCRIPTORS == False:
  TestValue.RegisterExtension(ext_value)

  DESCRIPTOR._options = None
  _PACKEDTESTVALUE.fields_by_name['double_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['double_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['float_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['float_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['int64_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['int64_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['uint64_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['uint64_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['int32_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['int32_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['fixed64_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['fixed64_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['fixed32_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['fixed32_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['bool_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['bool_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['uint32_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['uint32_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['sfixed32_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['sfixed32_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['sfixed64_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['sfixed64_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['sint32_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['sint32_value']._serialized_options = b'\020\001'
  _PACKEDTESTVALUE.fields_by_name['sint64_value']._options = None
  _PACKEDTESTVALUE.fields_by_name['sint64_value']._serialized_options = b'\020\001'
  _COLOR._serialized_start=3618
  _COLOR._serialized_end=3703
  _TESTCASE._serialized_start=125
  _TESTCASE._serialized_end=272
  _FIELDSPEC._serialized_start=274
  _FIELDSPEC._serialized_end=388
  _TESTVALUE._serialized_start=391
  _TESTVALUE._serialized_end=1529
  _PACKEDTESTVALUE._serialized_start=1532
  _PACKEDTESTVALUE._serialized_end=2721
  _PRIMITIVEVALUE._serialized_start=2724
  _PRIMITIVEVALUE._serialized_end=3070
  _EXTRAFIELDS._serialized_start=3072
  _EXTRAFIELDS._serialized_end=3129
  _INNERMESSAGEVALUE._serialized_start=3131
  _INNERMESSAGEVALUE._serialized_end=3193
  _MIDDLEMESSAGEVALUE._serialized_start=3196
  _MIDDLEMESSAGEVALUE._serialized_end=3328
  _MESSAGEVALUE._serialized_start=3330
  _MESSAGEVALUE._serialized_end=3435
  _REPEATEDMESSAGEVALUE._serialized_start=3438
  _REPEATEDMESSAGEVALUE._serialized_end=3616
  _REPEATEDMESSAGEVALUE_NESTEDMESSAGEVALUE._serialized_start=3553
  _REPEATEDMESSAGEVALUE_NESTEDMESSAGEVALUE._serialized_end=3616
# @@protoc_insertion_point(module_scope)
