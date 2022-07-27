# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/debug_event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.protobuf import graph_debug_info_pb2 as tensorflow_dot_core_dot_protobuf_dot_graph__debug__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*tensorflow/core/protobuf/debug_event.proto\x12\ntensorflow\x1a&tensorflow/core/framework/tensor.proto\x1a/tensorflow/core/protobuf/graph_debug_info.proto\"\xfe\x03\n\nDebugEvent\x12\x11\n\twall_time\x18\x01 \x01(\x01\x12\x0c\n\x04step\x18\x02 \x01(\x03\x12\x33\n\x0e\x64\x65\x62ug_metadata\x18\x03 \x01(\x0b\x32\x19.tensorflow.DebugMetadataH\x00\x12-\n\x0bsource_file\x18\x04 \x01(\x0b\x32\x16.tensorflow.SourceFileH\x00\x12;\n\x13stack_frame_with_id\x18\x06 \x01(\x0b\x32\x1c.tensorflow.StackFrameWithIdH\x00\x12\x38\n\x11graph_op_creation\x18\x07 \x01(\x0b\x32\x1b.tensorflow.GraphOpCreationH\x00\x12\x33\n\x0e\x64\x65\x62ugged_graph\x18\x08 \x01(\x0b\x32\x19.tensorflow.DebuggedGraphH\x00\x12*\n\texecution\x18\t \x01(\x0b\x32\x15.tensorflow.ExecutionH\x00\x12@\n\x15graph_execution_trace\x18\n \x01(\x0b\x32\x1f.tensorflow.GraphExecutionTraceH\x00\x12\x12\n\x08graph_id\x18\x0b \x01(\tH\x00\x12\x35\n\x0f\x64\x65\x62ugged_device\x18\x0c \x01(\x0b\x32\x1a.tensorflow.DebuggedDeviceH\x00\x42\x06\n\x04what\"W\n\rDebugMetadata\x12\x1a\n\x12tensorflow_version\x18\x01 \x01(\t\x12\x14\n\x0c\x66ile_version\x18\x02 \x01(\t\x12\x14\n\x0ctfdbg_run_id\x18\x03 \x01(\t\"A\n\nSourceFile\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x11\n\thost_name\x18\x02 \x01(\t\x12\r\n\x05lines\x18\x03 \x03(\t\"]\n\x10StackFrameWithId\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\rfile_line_col\x18\x02 \x01(\x0b\x32&.tensorflow.GraphDebugInfo.FileLineCol\":\n\x0c\x43odeLocation\x12\x11\n\thost_name\x18\x01 \x01(\t\x12\x17\n\x0fstack_frame_ids\x18\x02 \x03(\t\"\xe4\x01\n\x0fGraphOpCreation\x12\x0f\n\x07op_type\x18\x01 \x01(\t\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\x12\n\ngraph_name\x18\x03 \x01(\t\x12\x10\n\x08graph_id\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x05 \x01(\t\x12\x13\n\x0binput_names\x18\x06 \x03(\t\x12\x13\n\x0bnum_outputs\x18\x07 \x01(\x05\x12/\n\rcode_location\x18\x08 \x01(\x0b\x32\x18.tensorflow.CodeLocation\x12\x19\n\x11output_tensor_ids\x18\t \x03(\x05\"\xa5\x01\n\rDebuggedGraph\x12\x10\n\x08graph_id\x18\x01 \x01(\t\x12\x12\n\ngraph_name\x18\x02 \x01(\t\x12\x18\n\x10instrumented_ops\x18\x03 \x03(\t\x12\x1a\n\x12original_graph_def\x18\x04 \x01(\x0c\x12\x1e\n\x16instrumented_graph_def\x18\x05 \x01(\x0c\x12\x18\n\x10outer_context_id\x18\x06 \x01(\t\"8\n\x0e\x44\x65\x62uggedDevice\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\x05\"\xb3\x02\n\tExecution\x12\x0f\n\x07op_type\x18\x01 \x01(\t\x12\x13\n\x0bnum_outputs\x18\x02 \x01(\x05\x12\x10\n\x08graph_id\x18\x03 \x01(\t\x12\x18\n\x10input_tensor_ids\x18\x04 \x03(\x03\x12\x19\n\x11output_tensor_ids\x18\x05 \x03(\x03\x12\x36\n\x11tensor_debug_mode\x18\x06 \x01(\x0e\x32\x1b.tensorflow.TensorDebugMode\x12.\n\rtensor_protos\x18\x07 \x03(\x0b\x32\x17.tensorflow.TensorProto\x12/\n\rcode_location\x18\x08 \x01(\x0b\x32\x18.tensorflow.CodeLocation\x12 \n\x18output_tensor_device_ids\x18\t \x03(\x05\"\xd1\x01\n\x13GraphExecutionTrace\x12\x18\n\x10tfdbg_context_id\x18\x01 \x01(\t\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\x13\n\x0boutput_slot\x18\x03 \x01(\x05\x12\x36\n\x11tensor_debug_mode\x18\x04 \x01(\x0e\x32\x1b.tensorflow.TensorDebugMode\x12-\n\x0ctensor_proto\x18\x05 \x01(\x0b\x32\x17.tensorflow.TensorProto\x12\x13\n\x0b\x64\x65vice_name\x18\x06 \x01(\t*\xb6\x01\n\x0fTensorDebugMode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tNO_TENSOR\x10\x01\x12\x0f\n\x0b\x43URT_HEALTH\x10\x02\x12\x12\n\x0e\x43ONCISE_HEALTH\x10\x03\x12\x0f\n\x0b\x46ULL_HEALTH\x10\x04\x12\t\n\x05SHAPE\x10\x05\x12\x11\n\rFULL_NUMERICS\x10\x06\x12\x0f\n\x0b\x46ULL_TENSOR\x10\x07\x12\x1e\n\x1aREDUCE_INF_NAN_THREE_SLOTS\x10\x08\x42\x83\x01\n\x13org.tensorflow.utilB\x10\x44\x65\x62ugEventProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')

_TENSORDEBUGMODE = DESCRIPTOR.enum_types_by_name['TensorDebugMode']
TensorDebugMode = enum_type_wrapper.EnumTypeWrapper(_TENSORDEBUGMODE)
UNSPECIFIED = 0
NO_TENSOR = 1
CURT_HEALTH = 2
CONCISE_HEALTH = 3
FULL_HEALTH = 4
SHAPE = 5
FULL_NUMERICS = 6
FULL_TENSOR = 7
REDUCE_INF_NAN_THREE_SLOTS = 8


_DEBUGEVENT = DESCRIPTOR.message_types_by_name['DebugEvent']
_DEBUGMETADATA = DESCRIPTOR.message_types_by_name['DebugMetadata']
_SOURCEFILE = DESCRIPTOR.message_types_by_name['SourceFile']
_STACKFRAMEWITHID = DESCRIPTOR.message_types_by_name['StackFrameWithId']
_CODELOCATION = DESCRIPTOR.message_types_by_name['CodeLocation']
_GRAPHOPCREATION = DESCRIPTOR.message_types_by_name['GraphOpCreation']
_DEBUGGEDGRAPH = DESCRIPTOR.message_types_by_name['DebuggedGraph']
_DEBUGGEDDEVICE = DESCRIPTOR.message_types_by_name['DebuggedDevice']
_EXECUTION = DESCRIPTOR.message_types_by_name['Execution']
_GRAPHEXECUTIONTRACE = DESCRIPTOR.message_types_by_name['GraphExecutionTrace']
DebugEvent = _reflection.GeneratedProtocolMessageType('DebugEvent', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGEVENT,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DebugEvent)
  })
_sym_db.RegisterMessage(DebugEvent)

DebugMetadata = _reflection.GeneratedProtocolMessageType('DebugMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGMETADATA,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DebugMetadata)
  })
_sym_db.RegisterMessage(DebugMetadata)

SourceFile = _reflection.GeneratedProtocolMessageType('SourceFile', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEFILE,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.SourceFile)
  })
_sym_db.RegisterMessage(SourceFile)

StackFrameWithId = _reflection.GeneratedProtocolMessageType('StackFrameWithId', (_message.Message,), {
  'DESCRIPTOR' : _STACKFRAMEWITHID,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.StackFrameWithId)
  })
_sym_db.RegisterMessage(StackFrameWithId)

CodeLocation = _reflection.GeneratedProtocolMessageType('CodeLocation', (_message.Message,), {
  'DESCRIPTOR' : _CODELOCATION,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CodeLocation)
  })
_sym_db.RegisterMessage(CodeLocation)

GraphOpCreation = _reflection.GeneratedProtocolMessageType('GraphOpCreation', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHOPCREATION,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GraphOpCreation)
  })
_sym_db.RegisterMessage(GraphOpCreation)

DebuggedGraph = _reflection.GeneratedProtocolMessageType('DebuggedGraph', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGGEDGRAPH,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DebuggedGraph)
  })
_sym_db.RegisterMessage(DebuggedGraph)

DebuggedDevice = _reflection.GeneratedProtocolMessageType('DebuggedDevice', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGGEDDEVICE,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DebuggedDevice)
  })
_sym_db.RegisterMessage(DebuggedDevice)

Execution = _reflection.GeneratedProtocolMessageType('Execution', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTION,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.Execution)
  })
_sym_db.RegisterMessage(Execution)

GraphExecutionTrace = _reflection.GeneratedProtocolMessageType('GraphExecutionTrace', (_message.Message,), {
  'DESCRIPTOR' : _GRAPHEXECUTIONTRACE,
  '__module__' : 'tensorflow.core.protobuf.debug_event_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GraphExecutionTrace)
  })
_sym_db.RegisterMessage(GraphExecutionTrace)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023org.tensorflow.utilB\020DebugEventProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'
  _TENSORDEBUGMODE._serialized_start=1951
  _TENSORDEBUGMODE._serialized_end=2133
  _DEBUGEVENT._serialized_start=148
  _DEBUGEVENT._serialized_end=658
  _DEBUGMETADATA._serialized_start=660
  _DEBUGMETADATA._serialized_end=747
  _SOURCEFILE._serialized_start=749
  _SOURCEFILE._serialized_end=814
  _STACKFRAMEWITHID._serialized_start=816
  _STACKFRAMEWITHID._serialized_end=909
  _CODELOCATION._serialized_start=911
  _CODELOCATION._serialized_end=969
  _GRAPHOPCREATION._serialized_start=972
  _GRAPHOPCREATION._serialized_end=1200
  _DEBUGGEDGRAPH._serialized_start=1203
  _DEBUGGEDGRAPH._serialized_end=1368
  _DEBUGGEDDEVICE._serialized_start=1370
  _DEBUGGEDDEVICE._serialized_end=1426
  _EXECUTION._serialized_start=1429
  _EXECUTION._serialized_end=1736
  _GRAPHEXECUTIONTRACE._serialized_start=1739
  _GRAPHEXECUTIONTRACE._serialized_end=1948
# @@protoc_insertion_point(module_scope)
