# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/lite/tools/evaluation/proto/evaluation_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.lite.tools.evaluation.proto import evaluation_stages_pb2 as tensorflow_dot_lite_dot_tools_dot_evaluation_dot_proto_dot_evaluation__stages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/lite/tools/evaluation/proto/evaluation_config.proto',
  package='tflite.evaluation',
  syntax='proto2',
  serialized_options=b'\n\021tflite.evaluationP\001\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>tensorflow/lite/tools/evaluation/proto/evaluation_config.proto\x12\x11tflite.evaluation\x1a>tensorflow/lite/tools/evaluation/proto/evaluation_stages.proto\"e\n\x15\x45valuationStageConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\rspecification\x18\x02 \x01(\x0b\x32\'.tflite.evaluation.ProcessSpecification\"f\n\x16\x45valuationStageMetrics\x12\x10\n\x08num_runs\x18\x01 \x01(\x05\x12:\n\x0fprocess_metrics\x18\x02 \x01(\x0b\x32!.tflite.evaluation.ProcessMetricsB\x18\n\x11tflite.evaluationP\x01\xf8\x01\x01'
  ,
  dependencies=[tensorflow_dot_lite_dot_tools_dot_evaluation_dot_proto_dot_evaluation__stages__pb2.DESCRIPTOR,])




_EVALUATIONSTAGECONFIG = _descriptor.Descriptor(
  name='EvaluationStageConfig',
  full_name='tflite.evaluation.EvaluationStageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tflite.evaluation.EvaluationStageConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specification', full_name='tflite.evaluation.EvaluationStageConfig.specification', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=149,
  serialized_end=250,
)


_EVALUATIONSTAGEMETRICS = _descriptor.Descriptor(
  name='EvaluationStageMetrics',
  full_name='tflite.evaluation.EvaluationStageMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_runs', full_name='tflite.evaluation.EvaluationStageMetrics.num_runs', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_metrics', full_name='tflite.evaluation.EvaluationStageMetrics.process_metrics', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=252,
  serialized_end=354,
)

_EVALUATIONSTAGECONFIG.fields_by_name['specification'].message_type = tensorflow_dot_lite_dot_tools_dot_evaluation_dot_proto_dot_evaluation__stages__pb2._PROCESSSPECIFICATION
_EVALUATIONSTAGEMETRICS.fields_by_name['process_metrics'].message_type = tensorflow_dot_lite_dot_tools_dot_evaluation_dot_proto_dot_evaluation__stages__pb2._PROCESSMETRICS
DESCRIPTOR.message_types_by_name['EvaluationStageConfig'] = _EVALUATIONSTAGECONFIG
DESCRIPTOR.message_types_by_name['EvaluationStageMetrics'] = _EVALUATIONSTAGEMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvaluationStageConfig = _reflection.GeneratedProtocolMessageType('EvaluationStageConfig', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONSTAGECONFIG,
  '__module__' : 'tensorflow.lite.tools.evaluation.proto.evaluation_config_pb2'
  # @@protoc_insertion_point(class_scope:tflite.evaluation.EvaluationStageConfig)
  })
_sym_db.RegisterMessage(EvaluationStageConfig)

EvaluationStageMetrics = _reflection.GeneratedProtocolMessageType('EvaluationStageMetrics', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONSTAGEMETRICS,
  '__module__' : 'tensorflow.lite.tools.evaluation.proto.evaluation_config_pb2'
  # @@protoc_insertion_point(class_scope:tflite.evaluation.EvaluationStageMetrics)
  })
_sym_db.RegisterMessage(EvaluationStageMetrics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
