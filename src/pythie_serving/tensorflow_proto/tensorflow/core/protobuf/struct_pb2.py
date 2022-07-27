# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/struct.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%tensorflow/core/protobuf/struct.proto\x12\ntensorflow\x1a&tensorflow/core/framework/tensor.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"\x90\x05\n\x0fStructuredValue\x12+\n\nnone_value\x18\x01 \x01(\x0b\x32\x15.tensorflow.NoneValueH\x00\x12\x17\n\rfloat64_value\x18\x0b \x01(\x01H\x00\x12\x15\n\x0bint64_value\x18\x0c \x01(\x12H\x00\x12\x16\n\x0cstring_value\x18\r \x01(\tH\x00\x12\x14\n\nbool_value\x18\x0e \x01(\x08H\x00\x12:\n\x12tensor_shape_value\x18\x1f \x01(\x0b\x32\x1c.tensorflow.TensorShapeProtoH\x00\x12\x32\n\x12tensor_dtype_value\x18  \x01(\x0e\x32\x14.tensorflow.DataTypeH\x00\x12\x38\n\x11tensor_spec_value\x18! \x01(\x0b\x32\x1b.tensorflow.TensorSpecProtoH\x00\x12\x34\n\x0ftype_spec_value\x18\" \x01(\x0b\x32\x19.tensorflow.TypeSpecProtoH\x00\x12G\n\x19\x62ounded_tensor_spec_value\x18# \x01(\x0b\x32\".tensorflow.BoundedTensorSpecProtoH\x00\x12+\n\nlist_value\x18\x33 \x01(\x0b\x32\x15.tensorflow.ListValueH\x00\x12-\n\x0btuple_value\x18\x34 \x01(\x0b\x32\x16.tensorflow.TupleValueH\x00\x12+\n\ndict_value\x18\x35 \x01(\x0b\x32\x15.tensorflow.DictValueH\x00\x12\x38\n\x11named_tuple_value\x18\x36 \x01(\x0b\x32\x1b.tensorflow.NamedTupleValueH\x00\x42\x06\n\x04kind\"\x0b\n\tNoneValue\"8\n\tListValue\x12+\n\x06values\x18\x01 \x03(\x0b\x32\x1b.tensorflow.StructuredValue\"9\n\nTupleValue\x12+\n\x06values\x18\x01 \x03(\x0b\x32\x1b.tensorflow.StructuredValue\"\x8a\x01\n\tDictValue\x12\x31\n\x06\x66ields\x18\x01 \x03(\x0b\x32!.tensorflow.DictValue.FieldsEntry\x1aJ\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.tensorflow.StructuredValue:\x02\x38\x01\"D\n\tPairValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.tensorflow.StructuredValue\"F\n\x0fNamedTupleValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x06values\x18\x02 \x03(\x0b\x32\x15.tensorflow.PairValue\"q\n\x0fTensorSpecProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12#\n\x05\x64type\x18\x03 \x01(\x0e\x32\x14.tensorflow.DataType\"\xcc\x01\n\x16\x42oundedTensorSpecProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12#\n\x05\x64type\x18\x03 \x01(\x0e\x32\x14.tensorflow.DataType\x12(\n\x07minimum\x18\x04 \x01(\x0b\x32\x17.tensorflow.TensorProto\x12(\n\x07maximum\x18\x05 \x01(\x0b\x32\x17.tensorflow.TensorProto\"\xdb\x03\n\rTypeSpecProto\x12@\n\x0ftype_spec_class\x18\x01 \x01(\x0e\x32\'.tensorflow.TypeSpecProto.TypeSpecClass\x12/\n\ntype_state\x18\x02 \x01(\x0b\x32\x1b.tensorflow.StructuredValue\x12\x1c\n\x14type_spec_class_name\x18\x03 \x01(\t\"\xb8\x02\n\rTypeSpecClass\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\x12SPARSE_TENSOR_SPEC\x10\x01\x12\x17\n\x13INDEXED_SLICES_SPEC\x10\x02\x12\x16\n\x12RAGGED_TENSOR_SPEC\x10\x03\x12\x15\n\x11TENSOR_ARRAY_SPEC\x10\x04\x12\x15\n\x11\x44\x41TA_DATASET_SPEC\x10\x05\x12\x16\n\x12\x44\x41TA_ITERATOR_SPEC\x10\x06\x12\x11\n\rOPTIONAL_SPEC\x10\x07\x12\x14\n\x10PER_REPLICA_SPEC\x10\x08\x12\x11\n\rVARIABLE_SPEC\x10\t\x12\x16\n\x12ROW_PARTITION_SPEC\x10\n\x12\x18\n\x14REGISTERED_TYPE_SPEC\x10\x0c\x12\x17\n\x13\x45XTENSION_TYPE_SPEC\x10\r\"\x04\x08\x0b\x10\x0b\x42WZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_protob\x06proto3')



_STRUCTUREDVALUE = DESCRIPTOR.message_types_by_name['StructuredValue']
_NONEVALUE = DESCRIPTOR.message_types_by_name['NoneValue']
_LISTVALUE = DESCRIPTOR.message_types_by_name['ListValue']
_TUPLEVALUE = DESCRIPTOR.message_types_by_name['TupleValue']
_DICTVALUE = DESCRIPTOR.message_types_by_name['DictValue']
_DICTVALUE_FIELDSENTRY = _DICTVALUE.nested_types_by_name['FieldsEntry']
_PAIRVALUE = DESCRIPTOR.message_types_by_name['PairValue']
_NAMEDTUPLEVALUE = DESCRIPTOR.message_types_by_name['NamedTupleValue']
_TENSORSPECPROTO = DESCRIPTOR.message_types_by_name['TensorSpecProto']
_BOUNDEDTENSORSPECPROTO = DESCRIPTOR.message_types_by_name['BoundedTensorSpecProto']
_TYPESPECPROTO = DESCRIPTOR.message_types_by_name['TypeSpecProto']
_TYPESPECPROTO_TYPESPECCLASS = _TYPESPECPROTO.enum_types_by_name['TypeSpecClass']
StructuredValue = _reflection.GeneratedProtocolMessageType('StructuredValue', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTUREDVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.StructuredValue)
  })
_sym_db.RegisterMessage(StructuredValue)

NoneValue = _reflection.GeneratedProtocolMessageType('NoneValue', (_message.Message,), {
  'DESCRIPTOR' : _NONEVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NoneValue)
  })
_sym_db.RegisterMessage(NoneValue)

ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), {
  'DESCRIPTOR' : _LISTVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ListValue)
  })
_sym_db.RegisterMessage(ListValue)

TupleValue = _reflection.GeneratedProtocolMessageType('TupleValue', (_message.Message,), {
  'DESCRIPTOR' : _TUPLEVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TupleValue)
  })
_sym_db.RegisterMessage(TupleValue)

DictValue = _reflection.GeneratedProtocolMessageType('DictValue', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DICTVALUE_FIELDSENTRY,
    '__module__' : 'tensorflow.core.protobuf.struct_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.DictValue.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _DICTVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DictValue)
  })
_sym_db.RegisterMessage(DictValue)
_sym_db.RegisterMessage(DictValue.FieldsEntry)

PairValue = _reflection.GeneratedProtocolMessageType('PairValue', (_message.Message,), {
  'DESCRIPTOR' : _PAIRVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.PairValue)
  })
_sym_db.RegisterMessage(PairValue)

NamedTupleValue = _reflection.GeneratedProtocolMessageType('NamedTupleValue', (_message.Message,), {
  'DESCRIPTOR' : _NAMEDTUPLEVALUE,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NamedTupleValue)
  })
_sym_db.RegisterMessage(NamedTupleValue)

TensorSpecProto = _reflection.GeneratedProtocolMessageType('TensorSpecProto', (_message.Message,), {
  'DESCRIPTOR' : _TENSORSPECPROTO,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TensorSpecProto)
  })
_sym_db.RegisterMessage(TensorSpecProto)

BoundedTensorSpecProto = _reflection.GeneratedProtocolMessageType('BoundedTensorSpecProto', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDEDTENSORSPECPROTO,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BoundedTensorSpecProto)
  })
_sym_db.RegisterMessage(BoundedTensorSpecProto)

TypeSpecProto = _reflection.GeneratedProtocolMessageType('TypeSpecProto', (_message.Message,), {
  'DESCRIPTOR' : _TYPESPECPROTO,
  '__module__' : 'tensorflow.core.protobuf.struct_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TypeSpecProto)
  })
_sym_db.RegisterMessage(TypeSpecProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto'
  _DICTVALUE_FIELDSENTRY._options = None
  _DICTVALUE_FIELDSENTRY._serialized_options = b'8\001'
  _STRUCTUREDVALUE._serialized_start=179
  _STRUCTUREDVALUE._serialized_end=835
  _NONEVALUE._serialized_start=837
  _NONEVALUE._serialized_end=848
  _LISTVALUE._serialized_start=850
  _LISTVALUE._serialized_end=906
  _TUPLEVALUE._serialized_start=908
  _TUPLEVALUE._serialized_end=965
  _DICTVALUE._serialized_start=968
  _DICTVALUE._serialized_end=1106
  _DICTVALUE_FIELDSENTRY._serialized_start=1032
  _DICTVALUE_FIELDSENTRY._serialized_end=1106
  _PAIRVALUE._serialized_start=1108
  _PAIRVALUE._serialized_end=1176
  _NAMEDTUPLEVALUE._serialized_start=1178
  _NAMEDTUPLEVALUE._serialized_end=1248
  _TENSORSPECPROTO._serialized_start=1250
  _TENSORSPECPROTO._serialized_end=1363
  _BOUNDEDTENSORSPECPROTO._serialized_start=1366
  _BOUNDEDTENSORSPECPROTO._serialized_end=1570
  _TYPESPECPROTO._serialized_start=1573
  _TYPESPECPROTO._serialized_end=2048
  _TYPESPECPROTO_TYPESPECCLASS._serialized_start=1736
  _TYPESPECPROTO_TYPESPECCLASS._serialized_end=2048
# @@protoc_insertion_point(module_scope)
