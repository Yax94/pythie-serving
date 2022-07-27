# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/protobuf/pod_viewer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.profiler.protobuf import diagnostics_pb2 as tensorflow_dot_core_dot_profiler_dot_protobuf_dot_diagnostics__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.profiler.protobuf import pod_stats_pb2 as tensorflow_dot_core_dot_profiler_dot_protobuf_dot_pod__stats__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2tensorflow/core/profiler/protobuf/pod_viewer.proto\x12\x13tensorflow.profiler\x1a\x33tensorflow/core/profiler/protobuf/diagnostics.proto\x1a\x31tensorflow/core/profiler/protobuf/pod_stats.proto\"#\n\x0cReplicaGroup\x12\x13\n\x0breplica_ids\x18\x01 \x03(\x03\"\xac\x01\n\x0f\x41llReduceOpInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0boccurrences\x18\x02 \x01(\r\x12\x13\n\x0b\x64uration_us\x18\x03 \x01(\x01\x12\x11\n\tdata_size\x18\x04 \x01(\x04\x12\x39\n\x0ereplica_groups\x18\x05 \x03(\x0b\x32!.tensorflow.profiler.ReplicaGroup\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"\xe1\x03\n\x0bPodStatsMap\x12\x10\n\x08step_num\x18\x01 \x01(\r\x12Q\n\x12pod_stats_per_core\x18\x02 \x03(\x0b\x32\x35.tensorflow.profiler.PodStatsMap.PodStatsPerCoreEntry\x12\x34\n\nchannel_db\x18\x03 \x03(\x0b\x32 .tensorflow.profiler.ChannelInfo\x12]\n\x19\x63ore_id_to_replica_id_map\x18\x04 \x03(\x0b\x32:.tensorflow.profiler.PodStatsMap.CoreIdToReplicaIdMapEntry\x12>\n\x10\x61ll_reduce_op_db\x18\x05 \x03(\x0b\x32$.tensorflow.profiler.AllReduceOpInfo\x1a[\n\x14PodStatsPerCoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.tensorflow.profiler.PodStatsRecord:\x02\x38\x01\x1a;\n\x19\x43oreIdToReplicaIdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"K\n\x10PodStatsSequence\x12\x37\n\rpod_stats_map\x18\x01 \x03(\x0b\x32 .tensorflow.profiler.PodStatsMap\"\xf0\x01\n\x0b\x43hannelInfo\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12\x14\n\x0csrc_core_ids\x18\x0b \x03(\r\x12\x14\n\x0c\x64st_core_ids\x18\x0c \x03(\r\x12\x11\n\tdata_size\x18\x04 \x01(\x04\x12\x13\n\x0b\x64uration_us\x18\x05 \x01(\x01\x12\x13\n\x0boccurrences\x18\x06 \x01(\r\x12\x13\n\x0butilization\x18\x07 \x01(\x01\x12\x11\n\thlo_names\x18\x08 \x03(\t\x12\x15\n\rsend_delay_us\x18\t \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\tJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\n\x10\x0b\"$\n\x10PodViewerSummary\x12\x10\n\x08warnings\x18\x01 \x03(\t\"\xb3\x01\n\x11PodViewerTopology\x12\x13\n\x0bx_dimension\x18\x01 \x01(\x05\x12\x13\n\x0by_dimension\x18\x02 \x01(\x05\x12\x13\n\x0bz_dimension\x18\x03 \x01(\x05\x12\x15\n\rhost_x_stride\x18\x04 \x01(\x05\x12\x15\n\rhost_y_stride\x18\x05 \x01(\x05\x12\x15\n\rhost_z_stride\x18\x06 \x01(\x05\x12\x1a\n\x12num_cores_per_chip\x18\x07 \x01(\x05\"\xfb\x02\n\x11PodViewerDatabase\x12\x13\n\x0b\x64\x65vice_type\x18\n \x01(\t\x12\x41\n\x12pod_stats_sequence\x18\x03 \x01(\x0b\x32%.tensorflow.profiler.PodStatsSequence\x12\x36\n\x07summary\x18\x07 \x01(\x0b\x32%.tensorflow.profiler.PodViewerSummary\x12\x35\n\x0b\x64iagnostics\x18\x08 \x01(\x0b\x32 .tensorflow.profiler.Diagnostics\x12G\n\x15step_breakdown_events\x18\t \x03(\x0b\x32(.tensorflow.profiler.StepBreakdownEvents\x12\x38\n\x08topology\x18\x0b \x01(\x0b\x32&.tensorflow.profiler.PodViewerTopologyJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\x62\x06proto3')



_REPLICAGROUP = DESCRIPTOR.message_types_by_name['ReplicaGroup']
_ALLREDUCEOPINFO = DESCRIPTOR.message_types_by_name['AllReduceOpInfo']
_PODSTATSMAP = DESCRIPTOR.message_types_by_name['PodStatsMap']
_PODSTATSMAP_PODSTATSPERCOREENTRY = _PODSTATSMAP.nested_types_by_name['PodStatsPerCoreEntry']
_PODSTATSMAP_COREIDTOREPLICAIDMAPENTRY = _PODSTATSMAP.nested_types_by_name['CoreIdToReplicaIdMapEntry']
_PODSTATSSEQUENCE = DESCRIPTOR.message_types_by_name['PodStatsSequence']
_CHANNELINFO = DESCRIPTOR.message_types_by_name['ChannelInfo']
_PODVIEWERSUMMARY = DESCRIPTOR.message_types_by_name['PodViewerSummary']
_PODVIEWERTOPOLOGY = DESCRIPTOR.message_types_by_name['PodViewerTopology']
_PODVIEWERDATABASE = DESCRIPTOR.message_types_by_name['PodViewerDatabase']
ReplicaGroup = _reflection.GeneratedProtocolMessageType('ReplicaGroup', (_message.Message,), {
  'DESCRIPTOR' : _REPLICAGROUP,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.ReplicaGroup)
  })
_sym_db.RegisterMessage(ReplicaGroup)

AllReduceOpInfo = _reflection.GeneratedProtocolMessageType('AllReduceOpInfo', (_message.Message,), {
  'DESCRIPTOR' : _ALLREDUCEOPINFO,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.AllReduceOpInfo)
  })
_sym_db.RegisterMessage(AllReduceOpInfo)

PodStatsMap = _reflection.GeneratedProtocolMessageType('PodStatsMap', (_message.Message,), {

  'PodStatsPerCoreEntry' : _reflection.GeneratedProtocolMessageType('PodStatsPerCoreEntry', (_message.Message,), {
    'DESCRIPTOR' : _PODSTATSMAP_PODSTATSPERCOREENTRY,
    '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodStatsMap.PodStatsPerCoreEntry)
    })
  ,

  'CoreIdToReplicaIdMapEntry' : _reflection.GeneratedProtocolMessageType('CoreIdToReplicaIdMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _PODSTATSMAP_COREIDTOREPLICAIDMAPENTRY,
    '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodStatsMap.CoreIdToReplicaIdMapEntry)
    })
  ,
  'DESCRIPTOR' : _PODSTATSMAP,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodStatsMap)
  })
_sym_db.RegisterMessage(PodStatsMap)
_sym_db.RegisterMessage(PodStatsMap.PodStatsPerCoreEntry)
_sym_db.RegisterMessage(PodStatsMap.CoreIdToReplicaIdMapEntry)

PodStatsSequence = _reflection.GeneratedProtocolMessageType('PodStatsSequence', (_message.Message,), {
  'DESCRIPTOR' : _PODSTATSSEQUENCE,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodStatsSequence)
  })
_sym_db.RegisterMessage(PodStatsSequence)

ChannelInfo = _reflection.GeneratedProtocolMessageType('ChannelInfo', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELINFO,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.ChannelInfo)
  })
_sym_db.RegisterMessage(ChannelInfo)

PodViewerSummary = _reflection.GeneratedProtocolMessageType('PodViewerSummary', (_message.Message,), {
  'DESCRIPTOR' : _PODVIEWERSUMMARY,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodViewerSummary)
  })
_sym_db.RegisterMessage(PodViewerSummary)

PodViewerTopology = _reflection.GeneratedProtocolMessageType('PodViewerTopology', (_message.Message,), {
  'DESCRIPTOR' : _PODVIEWERTOPOLOGY,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodViewerTopology)
  })
_sym_db.RegisterMessage(PodViewerTopology)

PodViewerDatabase = _reflection.GeneratedProtocolMessageType('PodViewerDatabase', (_message.Message,), {
  'DESCRIPTOR' : _PODVIEWERDATABASE,
  '__module__' : 'tensorflow.core.profiler.protobuf.pod_viewer_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.PodViewerDatabase)
  })
_sym_db.RegisterMessage(PodViewerDatabase)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PODSTATSMAP_PODSTATSPERCOREENTRY._options = None
  _PODSTATSMAP_PODSTATSPERCOREENTRY._serialized_options = b'8\001'
  _PODSTATSMAP_COREIDTOREPLICAIDMAPENTRY._options = None
  _PODSTATSMAP_COREIDTOREPLICAIDMAPENTRY._serialized_options = b'8\001'
  _REPLICAGROUP._serialized_start=179
  _REPLICAGROUP._serialized_end=214
  _ALLREDUCEOPINFO._serialized_start=217
  _ALLREDUCEOPINFO._serialized_end=389
  _PODSTATSMAP._serialized_start=392
  _PODSTATSMAP._serialized_end=873
  _PODSTATSMAP_PODSTATSPERCOREENTRY._serialized_start=721
  _PODSTATSMAP_PODSTATSPERCOREENTRY._serialized_end=812
  _PODSTATSMAP_COREIDTOREPLICAIDMAPENTRY._serialized_start=814
  _PODSTATSMAP_COREIDTOREPLICAIDMAPENTRY._serialized_end=873
  _PODSTATSSEQUENCE._serialized_start=875
  _PODSTATSSEQUENCE._serialized_end=950
  _CHANNELINFO._serialized_start=953
  _CHANNELINFO._serialized_end=1193
  _PODVIEWERSUMMARY._serialized_start=1195
  _PODVIEWERSUMMARY._serialized_end=1231
  _PODVIEWERTOPOLOGY._serialized_start=1234
  _PODVIEWERTOPOLOGY._serialized_end=1413
  _PODVIEWERDATABASE._serialized_start=1416
  _PODVIEWERDATABASE._serialized_end=1795
# @@protoc_insertion_point(module_scope)
