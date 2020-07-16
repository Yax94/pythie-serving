# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/servables/tensorflow/session_bundle_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.protobuf import config_pb2 as tensorflow_dot_core_dot_protobuf_dot_config__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.protobuf import named_tensor_pb2 as tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/servables/tensorflow/session_bundle_config.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCtensorflow_serving/servables/tensorflow/session_bundle_config.proto\x12\x12tensorflow.serving\x1a\x1egoogle/protobuf/wrappers.proto\x1a%tensorflow/core/protobuf/config.proto\x1a+tensorflow/core/protobuf/named_tensor.proto\"Q\n\x12ModelWarmupOptions\x12;\n\x16num_request_iterations\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\xdb\x04\n\x13SessionBundleConfig\x12\x16\n\x0esession_target\x18\x01 \x01(\t\x12/\n\x0esession_config\x18\x02 \x01(\x0b\x32\x17.tensorflow.ConfigProto\x12\x43\n\x13\x62\x61tching_parameters\x18\x03 \x01(\x0b\x32&.tensorflow.serving.BatchingParameters\x12\x46\n!session_run_load_threadpool_index\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x34\n,experimental_transient_ram_bytes_during_load\x18\x05 \x01(\x04\x12\x18\n\x10saved_model_tags\x18\x06 \x03(\t\x12G\n experimental_fixed_input_tensors\x18\x8a\x06 \x03(\x0b\x32\x1c.tensorflow.NamedTensorProto\x12\x1c\n\x13\x65nable_model_warmup\x18\x8b\x06 \x01(\x08\x12\x45\n\x14model_warmup_options\x18\x8c\x06 \x01(\x0b\x32&.tensorflow.serving.ModelWarmupOptions\x12 \n\x17\x65nable_session_metadata\x18\x8d\x06 \x01(\x08\x12\x33\n*remove_unused_fields_from_bundle_metagraph\x18\x8e\x06 \x01(\x08\x12\x19\n\x10use_tflite_model\x18\x8f\x06 \x01(\x08\"\xf0\x02\n\x12\x42\x61tchingParameters\x12\x33\n\x0emax_batch_size\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14\x62\x61tch_timeout_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14max_enqueued_batches\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11num_batch_threads\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x10thread_pool_name\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1b\n\x13\x61llowed_batch_sizes\x18\x06 \x03(\x03\x12\"\n\x1apad_variable_length_inputs\x18\x07 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_config__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2.DESCRIPTOR,])




_MODELWARMUPOPTIONS = _descriptor.Descriptor(
  name='ModelWarmupOptions',
  full_name='tensorflow.serving.ModelWarmupOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_request_iterations', full_name='tensorflow.serving.ModelWarmupOptions.num_request_iterations', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=288,
)


_SESSIONBUNDLECONFIG = _descriptor.Descriptor(
  name='SessionBundleConfig',
  full_name='tensorflow.serving.SessionBundleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_target', full_name='tensorflow.serving.SessionBundleConfig.session_target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_config', full_name='tensorflow.serving.SessionBundleConfig.session_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batching_parameters', full_name='tensorflow.serving.SessionBundleConfig.batching_parameters', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_run_load_threadpool_index', full_name='tensorflow.serving.SessionBundleConfig.session_run_load_threadpool_index', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experimental_transient_ram_bytes_during_load', full_name='tensorflow.serving.SessionBundleConfig.experimental_transient_ram_bytes_during_load', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saved_model_tags', full_name='tensorflow.serving.SessionBundleConfig.saved_model_tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experimental_fixed_input_tensors', full_name='tensorflow.serving.SessionBundleConfig.experimental_fixed_input_tensors', index=6,
      number=778, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_model_warmup', full_name='tensorflow.serving.SessionBundleConfig.enable_model_warmup', index=7,
      number=779, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_warmup_options', full_name='tensorflow.serving.SessionBundleConfig.model_warmup_options', index=8,
      number=780, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_session_metadata', full_name='tensorflow.serving.SessionBundleConfig.enable_session_metadata', index=9,
      number=781, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove_unused_fields_from_bundle_metagraph', full_name='tensorflow.serving.SessionBundleConfig.remove_unused_fields_from_bundle_metagraph', index=10,
      number=782, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_tflite_model', full_name='tensorflow.serving.SessionBundleConfig.use_tflite_model', index=11,
      number=783, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=894,
)


_BATCHINGPARAMETERS = _descriptor.Descriptor(
  name='BatchingParameters',
  full_name='tensorflow.serving.BatchingParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_batch_size', full_name='tensorflow.serving.BatchingParameters.max_batch_size', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_timeout_micros', full_name='tensorflow.serving.BatchingParameters.batch_timeout_micros', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_enqueued_batches', full_name='tensorflow.serving.BatchingParameters.max_enqueued_batches', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_batch_threads', full_name='tensorflow.serving.BatchingParameters.num_batch_threads', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thread_pool_name', full_name='tensorflow.serving.BatchingParameters.thread_pool_name', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_batch_sizes', full_name='tensorflow.serving.BatchingParameters.allowed_batch_sizes', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pad_variable_length_inputs', full_name='tensorflow.serving.BatchingParameters.pad_variable_length_inputs', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=897,
  serialized_end=1265,
)

_MODELWARMUPOPTIONS.fields_by_name['num_request_iterations'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SESSIONBUNDLECONFIG.fields_by_name['session_config'].message_type = tensorflow_dot_core_dot_protobuf_dot_config__pb2._CONFIGPROTO
_SESSIONBUNDLECONFIG.fields_by_name['batching_parameters'].message_type = _BATCHINGPARAMETERS
_SESSIONBUNDLECONFIG.fields_by_name['session_run_load_threadpool_index'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SESSIONBUNDLECONFIG.fields_by_name['experimental_fixed_input_tensors'].message_type = tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2._NAMEDTENSORPROTO
_SESSIONBUNDLECONFIG.fields_by_name['model_warmup_options'].message_type = _MODELWARMUPOPTIONS
_BATCHINGPARAMETERS.fields_by_name['max_batch_size'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BATCHINGPARAMETERS.fields_by_name['batch_timeout_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BATCHINGPARAMETERS.fields_by_name['max_enqueued_batches'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BATCHINGPARAMETERS.fields_by_name['num_batch_threads'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BATCHINGPARAMETERS.fields_by_name['thread_pool_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['ModelWarmupOptions'] = _MODELWARMUPOPTIONS
DESCRIPTOR.message_types_by_name['SessionBundleConfig'] = _SESSIONBUNDLECONFIG
DESCRIPTOR.message_types_by_name['BatchingParameters'] = _BATCHINGPARAMETERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelWarmupOptions = _reflection.GeneratedProtocolMessageType('ModelWarmupOptions', (_message.Message,), {
  'DESCRIPTOR' : _MODELWARMUPOPTIONS,
  '__module__' : 'tensorflow_serving.servables.tensorflow.session_bundle_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelWarmupOptions)
  })
_sym_db.RegisterMessage(ModelWarmupOptions)

SessionBundleConfig = _reflection.GeneratedProtocolMessageType('SessionBundleConfig', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONBUNDLECONFIG,
  '__module__' : 'tensorflow_serving.servables.tensorflow.session_bundle_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.SessionBundleConfig)
  })
_sym_db.RegisterMessage(SessionBundleConfig)

BatchingParameters = _reflection.GeneratedProtocolMessageType('BatchingParameters', (_message.Message,), {
  'DESCRIPTOR' : _BATCHINGPARAMETERS,
  '__module__' : 'tensorflow_serving.servables.tensorflow.session_bundle_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.BatchingParameters)
  })
_sym_db.RegisterMessage(BatchingParameters)


# @@protoc_insertion_point(module_scope)
