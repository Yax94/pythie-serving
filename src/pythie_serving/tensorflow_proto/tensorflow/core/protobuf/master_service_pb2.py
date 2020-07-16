# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/master_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.protobuf import master_pb2 as tensorflow_dot_core_dot_protobuf_dot_master__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/master_service.proto',
  package='tensorflow.grpc',
  syntax='proto3',
  serialized_options=b'\n\032org.tensorflow.distruntimeB\023MasterServiceProtosP\001ZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-tensorflow/core/protobuf/master_service.proto\x12\x0ftensorflow.grpc\x1a%tensorflow/core/protobuf/master.proto2\xbb\x06\n\rMasterService\x12T\n\rCreateSession\x12 .tensorflow.CreateSessionRequest\x1a!.tensorflow.CreateSessionResponse\x12T\n\rExtendSession\x12 .tensorflow.ExtendSessionRequest\x1a!.tensorflow.ExtendSessionResponse\x12Z\n\x0fPartialRunSetup\x12\".tensorflow.PartialRunSetupRequest\x1a#.tensorflow.PartialRunSetupResponse\x12\x42\n\x07RunStep\x12\x1a.tensorflow.RunStepRequest\x1a\x1b.tensorflow.RunStepResponse\x12Q\n\x0c\x43loseSession\x12\x1f.tensorflow.CloseSessionRequest\x1a .tensorflow.CloseSessionResponse\x12N\n\x0bListDevices\x12\x1e.tensorflow.ListDevicesRequest\x1a\x1f.tensorflow.ListDevicesResponse\x12<\n\x05Reset\x12\x18.tensorflow.ResetRequest\x1a\x19.tensorflow.ResetResponse\x12Q\n\x0cMakeCallable\x12\x1f.tensorflow.MakeCallableRequest\x1a .tensorflow.MakeCallableResponse\x12N\n\x0bRunCallable\x12\x1e.tensorflow.RunCallableRequest\x1a\x1f.tensorflow.RunCallableResponse\x12Z\n\x0fReleaseCallable\x12\".tensorflow.ReleaseCallableRequest\x1a#.tensorflow.ReleaseCallableResponseB}\n\x1aorg.tensorflow.distruntimeB\x13MasterServiceProtosP\x01ZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_protob\x06proto3'
  ,
  dependencies=[tensorflow_dot_core_dot_protobuf_dot_master__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MASTERSERVICE = _descriptor.ServiceDescriptor(
  name='MasterService',
  full_name='tensorflow.grpc.MasterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=106,
  serialized_end=933,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateSession',
    full_name='tensorflow.grpc.MasterService.CreateSession',
    index=0,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._CREATESESSIONREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._CREATESESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExtendSession',
    full_name='tensorflow.grpc.MasterService.ExtendSession',
    index=1,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._EXTENDSESSIONREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._EXTENDSESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PartialRunSetup',
    full_name='tensorflow.grpc.MasterService.PartialRunSetup',
    index=2,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._PARTIALRUNSETUPREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._PARTIALRUNSETUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunStep',
    full_name='tensorflow.grpc.MasterService.RunStep',
    index=3,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RUNSTEPREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RUNSTEPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseSession',
    full_name='tensorflow.grpc.MasterService.CloseSession',
    index=4,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._CLOSESESSIONREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._CLOSESESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListDevices',
    full_name='tensorflow.grpc.MasterService.ListDevices',
    index=5,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._LISTDEVICESREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._LISTDEVICESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='tensorflow.grpc.MasterService.Reset',
    index=6,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RESETREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RESETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MakeCallable',
    full_name='tensorflow.grpc.MasterService.MakeCallable',
    index=7,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._MAKECALLABLEREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._MAKECALLABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunCallable',
    full_name='tensorflow.grpc.MasterService.RunCallable',
    index=8,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RUNCALLABLEREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RUNCALLABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseCallable',
    full_name='tensorflow.grpc.MasterService.ReleaseCallable',
    index=9,
    containing_service=None,
    input_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RELEASECALLABLEREQUEST,
    output_type=tensorflow_dot_core_dot_protobuf_dot_master__pb2._RELEASECALLABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MASTERSERVICE)

DESCRIPTOR.services_by_name['MasterService'] = _MASTERSERVICE

# @@protoc_insertion_point(module_scope)
