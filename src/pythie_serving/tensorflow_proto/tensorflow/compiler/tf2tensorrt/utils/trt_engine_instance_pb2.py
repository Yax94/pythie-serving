# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/tf2tensorrt/utils/trt_engine_instance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?tensorflow/compiler/tf2tensorrt/utils/trt_engine_instance.proto\x12\x13tensorflow.tensorrt\x1a,tensorflow/core/framework/tensor_shape.proto\"b\n\x11TRTEngineInstance\x12\x32\n\x0cinput_shapes\x18\x01 \x03(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x19\n\x11serialized_engine\x18\x02 \x01(\x0c\x62\x06proto3')



_TRTENGINEINSTANCE = DESCRIPTOR.message_types_by_name['TRTEngineInstance']
TRTEngineInstance = _reflection.GeneratedProtocolMessageType('TRTEngineInstance', (_message.Message,), {
  'DESCRIPTOR' : _TRTENGINEINSTANCE,
  '__module__' : 'tensorflow.compiler.tf2tensorrt.utils.trt_engine_instance_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorrt.TRTEngineInstance)
  })
_sym_db.RegisterMessage(TRTEngineInstance)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRTENGINEINSTANCE._serialized_start=134
  _TRTENGINEINSTANCE._serialized_end=232
# @@protoc_insertion_point(module_scope)
