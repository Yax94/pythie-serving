# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/lite/toco/toco_flags.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.lite.toco import types_pb2 as tensorflow_dot_lite_dot_toco_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/lite/toco/toco_flags.proto',
  package='toco',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%tensorflow/lite/toco/toco_flags.proto\x12\x04toco\x1a tensorflow/lite/toco/types.proto\"\xd6\x07\n\tTocoFlags\x12&\n\x0cinput_format\x18\x01 \x01(\x0e\x32\x10.toco.FileFormat\x12\'\n\routput_format\x18\x02 \x01(\x0e\x32\x10.toco.FileFormat\x12.\n\x14inference_input_type\x18\x0b \x01(\x0e\x32\x10.toco.IODataType\x12(\n\x0einference_type\x18\x04 \x01(\x0e\x32\x10.toco.IODataType\x12\x1a\n\x12\x64\x65\x66\x61ult_ranges_min\x18\x05 \x01(\x02\x12\x1a\n\x12\x64\x65\x66\x61ult_ranges_max\x18\x06 \x01(\x02\x12 \n\x18\x64\x65\x66\x61ult_int16_ranges_min\x18\x0f \x01(\x02\x12 \n\x18\x64\x65\x66\x61ult_int16_ranges_max\x18\x10 \x01(\x02\x12\x17\n\x0f\x64rop_fake_quant\x18\x07 \x01(\x08\x12!\n\x19reorder_across_fake_quant\x18\x08 \x01(\x08\x12\x18\n\x10\x61llow_custom_ops\x18\n \x01(\x08\x12\x1f\n\x17\x64rop_control_dependency\x18\x0c \x01(\x08\x12+\n#debug_disable_recurrent_cell_fusion\x18\r \x01(\x08\x12%\n\x1dpropagate_fake_quant_num_bits\x18\x0e \x01(\x08\x12\x35\n-allow_nudging_weights_to_use_fast_gemm_kernel\x18\x11 \x01(\x08\x12\'\n\x1b\x64\x65\x64upe_array_min_size_bytes\x18\x12 \x01(\x03:\x02\x36\x34\x12&\n\x18split_tflite_lstm_inputs\x18\x13 \x01(\x08:\x04true\x12\x1f\n\x10quantize_weights\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11\x64ump_graphviz_dir\x18\x18 \x01(\t\x12#\n\x1b\x64ump_graphviz_include_video\x18\x19 \x01(\x08\x12%\n\x16post_training_quantize\x18\x1a \x01(\x08:\x05\x66\x61lse\x12#\n\x14\x65nable_select_tf_ops\x18\x1b \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x66orce_select_tf_ops\x18\x1c \x01(\x08:\x05\x66\x61lse\x12\"\n\x13quantize_to_float16\x18\x1d \x01(\x08:\x05\x66\x61lse\x12#\n\x15\x61llow_dynamic_tensors\x18\x1e \x01(\x08:\x04true\x12\x1e\n\x16\x63onversion_summary_dir\x18\x1f \x01(\t\x12\x15\n\rcustom_opdefs\x18  \x03(\t*\\\n\nFileFormat\x12\x17\n\x13\x46ILE_FORMAT_UNKNOWN\x10\x00\x12\x17\n\x13TENSORFLOW_GRAPHDEF\x10\x01\x12\n\n\x06TFLITE\x10\x02\x12\x10\n\x0cGRAPHVIZ_DOT\x10\x03'
  ,
  dependencies=[tensorflow_dot_lite_dot_toco_dot_types__pb2.DESCRIPTOR,])

_FILEFORMAT = _descriptor.EnumDescriptor(
  name='FileFormat',
  full_name='toco.FileFormat',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE_FORMAT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TENSORFLOW_GRAPHDEF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TFLITE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GRAPHVIZ_DOT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1066,
  serialized_end=1158,
)
_sym_db.RegisterEnumDescriptor(_FILEFORMAT)

FileFormat = enum_type_wrapper.EnumTypeWrapper(_FILEFORMAT)
FILE_FORMAT_UNKNOWN = 0
TENSORFLOW_GRAPHDEF = 1
TFLITE = 2
GRAPHVIZ_DOT = 3



_TOCOFLAGS = _descriptor.Descriptor(
  name='TocoFlags',
  full_name='toco.TocoFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_format', full_name='toco.TocoFlags.input_format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_format', full_name='toco.TocoFlags.output_format', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inference_input_type', full_name='toco.TocoFlags.inference_input_type', index=2,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inference_type', full_name='toco.TocoFlags.inference_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_ranges_min', full_name='toco.TocoFlags.default_ranges_min', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_ranges_max', full_name='toco.TocoFlags.default_ranges_max', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_int16_ranges_min', full_name='toco.TocoFlags.default_int16_ranges_min', index=6,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_int16_ranges_max', full_name='toco.TocoFlags.default_int16_ranges_max', index=7,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drop_fake_quant', full_name='toco.TocoFlags.drop_fake_quant', index=8,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reorder_across_fake_quant', full_name='toco.TocoFlags.reorder_across_fake_quant', index=9,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_custom_ops', full_name='toco.TocoFlags.allow_custom_ops', index=10,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drop_control_dependency', full_name='toco.TocoFlags.drop_control_dependency', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_disable_recurrent_cell_fusion', full_name='toco.TocoFlags.debug_disable_recurrent_cell_fusion', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propagate_fake_quant_num_bits', full_name='toco.TocoFlags.propagate_fake_quant_num_bits', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_nudging_weights_to_use_fast_gemm_kernel', full_name='toco.TocoFlags.allow_nudging_weights_to_use_fast_gemm_kernel', index=14,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dedupe_array_min_size_bytes', full_name='toco.TocoFlags.dedupe_array_min_size_bytes', index=15,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_tflite_lstm_inputs', full_name='toco.TocoFlags.split_tflite_lstm_inputs', index=16,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantize_weights', full_name='toco.TocoFlags.quantize_weights', index=17,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dump_graphviz_dir', full_name='toco.TocoFlags.dump_graphviz_dir', index=18,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dump_graphviz_include_video', full_name='toco.TocoFlags.dump_graphviz_include_video', index=19,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='post_training_quantize', full_name='toco.TocoFlags.post_training_quantize', index=20,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_select_tf_ops', full_name='toco.TocoFlags.enable_select_tf_ops', index=21,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force_select_tf_ops', full_name='toco.TocoFlags.force_select_tf_ops', index=22,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantize_to_float16', full_name='toco.TocoFlags.quantize_to_float16', index=23,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_dynamic_tensors', full_name='toco.TocoFlags.allow_dynamic_tensors', index=24,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversion_summary_dir', full_name='toco.TocoFlags.conversion_summary_dir', index=25,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_opdefs', full_name='toco.TocoFlags.custom_opdefs', index=26,
      number=32, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=1064,
)

_TOCOFLAGS.fields_by_name['input_format'].enum_type = _FILEFORMAT
_TOCOFLAGS.fields_by_name['output_format'].enum_type = _FILEFORMAT
_TOCOFLAGS.fields_by_name['inference_input_type'].enum_type = tensorflow_dot_lite_dot_toco_dot_types__pb2._IODATATYPE
_TOCOFLAGS.fields_by_name['inference_type'].enum_type = tensorflow_dot_lite_dot_toco_dot_types__pb2._IODATATYPE
DESCRIPTOR.message_types_by_name['TocoFlags'] = _TOCOFLAGS
DESCRIPTOR.enum_types_by_name['FileFormat'] = _FILEFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TocoFlags = _reflection.GeneratedProtocolMessageType('TocoFlags', (_message.Message,), {
  'DESCRIPTOR' : _TOCOFLAGS,
  '__module__' : 'tensorflow.lite.toco.toco_flags_pb2'
  # @@protoc_insertion_point(class_scope:toco.TocoFlags)
  })
_sym_db.RegisterMessage(TocoFlags)


# @@protoc_insertion_point(module_scope)
