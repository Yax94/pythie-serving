# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/xla/python/tpu_driver/tpu_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.compiler.xla.python.tpu_driver import tpu_driver_pb2 as tensorflow_dot_compiler_dot_xla_dot_python_dot_tpu__driver_dot_tpu__driver__pb2
from pythie_serving.tensorflow_proto.tensorflow.compiler.xla.service import hlo_pb2 as tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__pb2
from pythie_serving.tensorflow_proto.tensorflow.compiler.xla import xla_data_pb2 as tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;tensorflow/compiler/xla/python/tpu_driver/tpu_service.proto\x12\ntpu_driver\x1a:tensorflow/compiler/xla/python/tpu_driver/tpu_driver.proto\x1a)tensorflow/compiler/xla/service/hlo.proto\x1a&tensorflow/compiler/xla/xla_data.proto\".\n\rStatusMessage\x12\x0c\n\x04\x63ode\x18\x01 \x02(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x8b\x01\n\x0f\x41llocateRequest\x12\x0f\n\x07\x63ore_id\x18\x01 \x02(\x05\x12(\n\x06region\x18\x02 \x02(\x0e\x32\x18.tpu_driver.MemoryRegion\x12\x13\n\tnum_bytes\x18\x03 \x01(\x03H\x00\x12 \n\x05shape\x18\x04 \x01(\x0b\x32\x0f.xla.ShapeProtoH\x00\x42\x06\n\x04size\"c\n\x14\x41llocateTupleRequest\x12\x0f\n\x07\x63ore_id\x18\x01 \x02(\x05\x12(\n\x06region\x18\x02 \x02(\x0e\x32\x18.tpu_driver.MemoryRegion\x12\x10\n\x08\x63hildren\x18\x03 \x03(\x03\"#\n\x11\x44\x65\x61llocateRequest\x12\x0e\n\x06handle\x18\x01 \x02(\x03\">\n\x17TransferToDeviceRequest\x12\x15\n\rtarget_handle\x18\x01 \x02(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\"2\n\x19TransferFromDeviceRequest\x12\x15\n\rsource_handle\x18\x01 \x02(\x03\"*\n\x1aTransferFromDeviceResponse\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\"Q\n!TransferFromDeviceToDeviceRequest\x12\x15\n\rsource_handle\x18\x01 \x02(\x03\x12\x15\n\rtarget_handle\x18\x02 \x02(\x03\"J\n\x0e\x43ompileRequest\x12\"\n\x0bhlo_program\x18\x01 \x02(\x0b\x32\r.xla.HloProto\x12\x14\n\x0cnum_replicas\x18\x02 \x01(\x03\"H\n\x17\x43ompiledProgramMetadata\x12-\n\rprogram_shape\x18\x01 \x02(\x0b\x32\x16.xla.ProgramShapeProto\"H\n\x0f\x43ompileResponse\x12\x35\n\x08metadata\x18\x01 \x02(\x0b\x32#.tpu_driver.CompiledProgramMetadata\"F\n\x12LoadProgramRequest\x12\x0f\n\x07\x63ore_id\x18\x01 \x02(\x05\x12\x1f\n\x17\x63ompiled_program_handle\x18\x02 \x02(\x03\"5\n\x14UnloadProgramRequest\x12\x1d\n\x15loaded_program_handle\x18\x01 \x02(\x03\"\x93\x01\n\x0e\x45xecuteRequest\x12\x1d\n\x15loaded_program_handle\x18\x01 \x02(\x03\x12\x14\n\x0cinput_handle\x18\x02 \x03(\x03\x12\x15\n\routput_handle\x18\x03 \x03(\x03\x12\x35\n\x11\x64\x65vice_assignment\x18\x04 \x01(\x0b\x32\x1a.xla.DeviceAssignmentProto\"\xb4\x05\n\rStreamRequest\x12.\n\x05\x65ntry\x18\x1e \x03(\x0b\x32\x1f.tpu_driver.StreamRequest.Entry\x1a\xf2\x04\n\x05\x45ntry\x12,\n\x05\x61lloc\x18\x01 \x01(\x0b\x32\x1b.tpu_driver.AllocateRequestH\x00\x12\x37\n\x0b\x61lloc_tuple\x18\x02 \x01(\x0b\x32 .tpu_driver.AllocateTupleRequestH\x00\x12\x30\n\x07\x64\x65\x61lloc\x18\x03 \x01(\x0b\x32\x1d.tpu_driver.DeallocateRequestH\x00\x12:\n\x0btransfer_to\x18\x04 \x01(\x0b\x32#.tpu_driver.TransferToDeviceRequestH\x00\x12>\n\rtransfer_from\x18\x05 \x01(\x0b\x32%.tpu_driver.TransferFromDeviceRequestH\x00\x12I\n\x10transfer_from_to\x18\n \x01(\x0b\x32-.tpu_driver.TransferFromDeviceToDeviceRequestH\x00\x12-\n\x07\x63ompile\x18\x06 \x01(\x0b\x32\x1a.tpu_driver.CompileRequestH\x00\x12.\n\x04load\x18\x07 \x01(\x0b\x32\x1e.tpu_driver.LoadProgramRequestH\x00\x12\x32\n\x06unload\x18\x08 \x01(\x0b\x32 .tpu_driver.UnloadProgramRequestH\x00\x12-\n\x07\x65xecute\x18\t \x01(\x0b\x32\x1a.tpu_driver.ExecuteRequestH\x00\x12\x13\n\x0bwait_for_id\x18\x14 \x03(\x03\x12\x14\n\x0coperation_id\x18\x15 \x02(\x03\x12\x11\n\tthread_id\x18\x16 \x01(\x03\x42\t\n\x07request\"\x89\x02\n\x0eStreamResponse\x12/\n\x05\x65ntry\x18\x14 \x03(\x0b\x32 .tpu_driver.StreamResponse.Entry\x1a\xc5\x01\n\x05\x45ntry\x12?\n\rtransfer_from\x18\x03 \x01(\x0b\x32&.tpu_driver.TransferFromDeviceResponseH\x00\x12.\n\x07\x63ompile\x18\x04 \x01(\x0b\x32\x1b.tpu_driver.CompileResponseH\x00\x12)\n\x06status\x18\n \x02(\x0b\x32\x19.tpu_driver.StatusMessage\x12\x14\n\x0coperation_id\x18\x0b \x02(\x03\x42\n\n\x08response\"(\n\x0bOpenRequest\x12\x19\n\x0e\x63lient_version\x18\x01 \x01(\x05:\x01\x30\"F\n\x0cOpenResponse\x12\x11\n\tclient_id\x18\x01 \x02(\r\x12#\n\x15max_idle_time_seconds\x18\x02 \x01(\x05:\x04\x33\x36\x30\x30\"!\n\x0c\x43loseRequest\x12\x11\n\tclient_id\x18\x01 \x02(\x07\"\x0f\n\rCloseResponse\"\x0e\n\x0cResetRequest\"\x0f\n\rResetResponse\"\x18\n\x16QuerySystemInfoRequest\"F\n\x17QuerySystemInfoResponse\x12+\n\x0bsystem_info\x18\x01 \x02(\x0b\x32\x16.tpu_driver.SystemInfo2\xef\x02\n\x0e\x43loudTpuDriver\x12\x39\n\x04Open\x12\x17.tpu_driver.OpenRequest\x1a\x18.tpu_driver.OpenResponse\x12<\n\x05\x43lose\x12\x18.tpu_driver.CloseRequest\x1a\x19.tpu_driver.CloseResponse\x12<\n\x05Reset\x12\x18.tpu_driver.ResetRequest\x1a\x19.tpu_driver.ResetResponse\x12Z\n\x0fQuerySystemInfo\x12\".tpu_driver.QuerySystemInfoRequest\x1a#.tpu_driver.QuerySystemInfoResponse\x12J\n\rStreamExecute\x12\x19.tpu_driver.StreamRequest\x1a\x1a.tpu_driver.StreamResponse(\x01\x30\x01\x42\x02H\x01')



_STATUSMESSAGE = DESCRIPTOR.message_types_by_name['StatusMessage']
_ALLOCATEREQUEST = DESCRIPTOR.message_types_by_name['AllocateRequest']
_ALLOCATETUPLEREQUEST = DESCRIPTOR.message_types_by_name['AllocateTupleRequest']
_DEALLOCATEREQUEST = DESCRIPTOR.message_types_by_name['DeallocateRequest']
_TRANSFERTODEVICEREQUEST = DESCRIPTOR.message_types_by_name['TransferToDeviceRequest']
_TRANSFERFROMDEVICEREQUEST = DESCRIPTOR.message_types_by_name['TransferFromDeviceRequest']
_TRANSFERFROMDEVICERESPONSE = DESCRIPTOR.message_types_by_name['TransferFromDeviceResponse']
_TRANSFERFROMDEVICETODEVICEREQUEST = DESCRIPTOR.message_types_by_name['TransferFromDeviceToDeviceRequest']
_COMPILEREQUEST = DESCRIPTOR.message_types_by_name['CompileRequest']
_COMPILEDPROGRAMMETADATA = DESCRIPTOR.message_types_by_name['CompiledProgramMetadata']
_COMPILERESPONSE = DESCRIPTOR.message_types_by_name['CompileResponse']
_LOADPROGRAMREQUEST = DESCRIPTOR.message_types_by_name['LoadProgramRequest']
_UNLOADPROGRAMREQUEST = DESCRIPTOR.message_types_by_name['UnloadProgramRequest']
_EXECUTEREQUEST = DESCRIPTOR.message_types_by_name['ExecuteRequest']
_STREAMREQUEST = DESCRIPTOR.message_types_by_name['StreamRequest']
_STREAMREQUEST_ENTRY = _STREAMREQUEST.nested_types_by_name['Entry']
_STREAMRESPONSE = DESCRIPTOR.message_types_by_name['StreamResponse']
_STREAMRESPONSE_ENTRY = _STREAMRESPONSE.nested_types_by_name['Entry']
_OPENREQUEST = DESCRIPTOR.message_types_by_name['OpenRequest']
_OPENRESPONSE = DESCRIPTOR.message_types_by_name['OpenResponse']
_CLOSEREQUEST = DESCRIPTOR.message_types_by_name['CloseRequest']
_CLOSERESPONSE = DESCRIPTOR.message_types_by_name['CloseResponse']
_RESETREQUEST = DESCRIPTOR.message_types_by_name['ResetRequest']
_RESETRESPONSE = DESCRIPTOR.message_types_by_name['ResetResponse']
_QUERYSYSTEMINFOREQUEST = DESCRIPTOR.message_types_by_name['QuerySystemInfoRequest']
_QUERYSYSTEMINFORESPONSE = DESCRIPTOR.message_types_by_name['QuerySystemInfoResponse']
StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)

AllocateRequest = _reflection.GeneratedProtocolMessageType('AllocateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.AllocateRequest)
  })
_sym_db.RegisterMessage(AllocateRequest)

AllocateTupleRequest = _reflection.GeneratedProtocolMessageType('AllocateTupleRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATETUPLEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.AllocateTupleRequest)
  })
_sym_db.RegisterMessage(AllocateTupleRequest)

DeallocateRequest = _reflection.GeneratedProtocolMessageType('DeallocateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEALLOCATEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.DeallocateRequest)
  })
_sym_db.RegisterMessage(DeallocateRequest)

TransferToDeviceRequest = _reflection.GeneratedProtocolMessageType('TransferToDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERTODEVICEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.TransferToDeviceRequest)
  })
_sym_db.RegisterMessage(TransferToDeviceRequest)

TransferFromDeviceRequest = _reflection.GeneratedProtocolMessageType('TransferFromDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERFROMDEVICEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.TransferFromDeviceRequest)
  })
_sym_db.RegisterMessage(TransferFromDeviceRequest)

TransferFromDeviceResponse = _reflection.GeneratedProtocolMessageType('TransferFromDeviceResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERFROMDEVICERESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.TransferFromDeviceResponse)
  })
_sym_db.RegisterMessage(TransferFromDeviceResponse)

TransferFromDeviceToDeviceRequest = _reflection.GeneratedProtocolMessageType('TransferFromDeviceToDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERFROMDEVICETODEVICEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.TransferFromDeviceToDeviceRequest)
  })
_sym_db.RegisterMessage(TransferFromDeviceToDeviceRequest)

CompileRequest = _reflection.GeneratedProtocolMessageType('CompileRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPILEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.CompileRequest)
  })
_sym_db.RegisterMessage(CompileRequest)

CompiledProgramMetadata = _reflection.GeneratedProtocolMessageType('CompiledProgramMetadata', (_message.Message,), {
  'DESCRIPTOR' : _COMPILEDPROGRAMMETADATA,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.CompiledProgramMetadata)
  })
_sym_db.RegisterMessage(CompiledProgramMetadata)

CompileResponse = _reflection.GeneratedProtocolMessageType('CompileResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPILERESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.CompileResponse)
  })
_sym_db.RegisterMessage(CompileResponse)

LoadProgramRequest = _reflection.GeneratedProtocolMessageType('LoadProgramRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADPROGRAMREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.LoadProgramRequest)
  })
_sym_db.RegisterMessage(LoadProgramRequest)

UnloadProgramRequest = _reflection.GeneratedProtocolMessageType('UnloadProgramRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOADPROGRAMREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.UnloadProgramRequest)
  })
_sym_db.RegisterMessage(UnloadProgramRequest)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _STREAMREQUEST_ENTRY,
    '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
    # @@protoc_insertion_point(class_scope:tpu_driver.StreamRequest.Entry)
    })
  ,
  'DESCRIPTOR' : _STREAMREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.StreamRequest)
  })
_sym_db.RegisterMessage(StreamRequest)
_sym_db.RegisterMessage(StreamRequest.Entry)

StreamResponse = _reflection.GeneratedProtocolMessageType('StreamResponse', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _STREAMRESPONSE_ENTRY,
    '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
    # @@protoc_insertion_point(class_scope:tpu_driver.StreamResponse.Entry)
    })
  ,
  'DESCRIPTOR' : _STREAMRESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.StreamResponse)
  })
_sym_db.RegisterMessage(StreamResponse)
_sym_db.RegisterMessage(StreamResponse.Entry)

OpenRequest = _reflection.GeneratedProtocolMessageType('OpenRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.OpenRequest)
  })
_sym_db.RegisterMessage(OpenRequest)

OpenResponse = _reflection.GeneratedProtocolMessageType('OpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENRESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.OpenResponse)
  })
_sym_db.RegisterMessage(OpenResponse)

CloseRequest = _reflection.GeneratedProtocolMessageType('CloseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.CloseRequest)
  })
_sym_db.RegisterMessage(CloseRequest)

CloseResponse = _reflection.GeneratedProtocolMessageType('CloseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSERESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.CloseResponse)
  })
_sym_db.RegisterMessage(CloseResponse)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.ResetRequest)
  })
_sym_db.RegisterMessage(ResetRequest)

ResetResponse = _reflection.GeneratedProtocolMessageType('ResetResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETRESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.ResetResponse)
  })
_sym_db.RegisterMessage(ResetResponse)

QuerySystemInfoRequest = _reflection.GeneratedProtocolMessageType('QuerySystemInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSYSTEMINFOREQUEST,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.QuerySystemInfoRequest)
  })
_sym_db.RegisterMessage(QuerySystemInfoRequest)

QuerySystemInfoResponse = _reflection.GeneratedProtocolMessageType('QuerySystemInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSYSTEMINFORESPONSE,
  '__module__' : 'tensorflow.compiler.xla.python.tpu_driver.tpu_service_pb2'
  # @@protoc_insertion_point(class_scope:tpu_driver.QuerySystemInfoResponse)
  })
_sym_db.RegisterMessage(QuerySystemInfoResponse)

_CLOUDTPUDRIVER = DESCRIPTOR.services_by_name['CloudTpuDriver']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001'
  _STATUSMESSAGE._serialized_start=218
  _STATUSMESSAGE._serialized_end=264
  _ALLOCATEREQUEST._serialized_start=267
  _ALLOCATEREQUEST._serialized_end=406
  _ALLOCATETUPLEREQUEST._serialized_start=408
  _ALLOCATETUPLEREQUEST._serialized_end=507
  _DEALLOCATEREQUEST._serialized_start=509
  _DEALLOCATEREQUEST._serialized_end=544
  _TRANSFERTODEVICEREQUEST._serialized_start=546
  _TRANSFERTODEVICEREQUEST._serialized_end=608
  _TRANSFERFROMDEVICEREQUEST._serialized_start=610
  _TRANSFERFROMDEVICEREQUEST._serialized_end=660
  _TRANSFERFROMDEVICERESPONSE._serialized_start=662
  _TRANSFERFROMDEVICERESPONSE._serialized_end=704
  _TRANSFERFROMDEVICETODEVICEREQUEST._serialized_start=706
  _TRANSFERFROMDEVICETODEVICEREQUEST._serialized_end=787
  _COMPILEREQUEST._serialized_start=789
  _COMPILEREQUEST._serialized_end=863
  _COMPILEDPROGRAMMETADATA._serialized_start=865
  _COMPILEDPROGRAMMETADATA._serialized_end=937
  _COMPILERESPONSE._serialized_start=939
  _COMPILERESPONSE._serialized_end=1011
  _LOADPROGRAMREQUEST._serialized_start=1013
  _LOADPROGRAMREQUEST._serialized_end=1083
  _UNLOADPROGRAMREQUEST._serialized_start=1085
  _UNLOADPROGRAMREQUEST._serialized_end=1138
  _EXECUTEREQUEST._serialized_start=1141
  _EXECUTEREQUEST._serialized_end=1288
  _STREAMREQUEST._serialized_start=1291
  _STREAMREQUEST._serialized_end=1983
  _STREAMREQUEST_ENTRY._serialized_start=1357
  _STREAMREQUEST_ENTRY._serialized_end=1983
  _STREAMRESPONSE._serialized_start=1986
  _STREAMRESPONSE._serialized_end=2251
  _STREAMRESPONSE_ENTRY._serialized_start=2054
  _STREAMRESPONSE_ENTRY._serialized_end=2251
  _OPENREQUEST._serialized_start=2253
  _OPENREQUEST._serialized_end=2293
  _OPENRESPONSE._serialized_start=2295
  _OPENRESPONSE._serialized_end=2365
  _CLOSEREQUEST._serialized_start=2367
  _CLOSEREQUEST._serialized_end=2400
  _CLOSERESPONSE._serialized_start=2402
  _CLOSERESPONSE._serialized_end=2417
  _RESETREQUEST._serialized_start=2419
  _RESETREQUEST._serialized_end=2433
  _RESETRESPONSE._serialized_start=2435
  _RESETRESPONSE._serialized_end=2450
  _QUERYSYSTEMINFOREQUEST._serialized_start=2452
  _QUERYSYSTEMINFOREQUEST._serialized_end=2476
  _QUERYSYSTEMINFORESPONSE._serialized_start=2478
  _QUERYSYSTEMINFORESPONSE._serialized_end=2548
  _CLOUDTPUDRIVER._serialized_start=2551
  _CLOUDTPUDRIVER._serialized_end=2918
# @@protoc_insertion_point(module_scope)
