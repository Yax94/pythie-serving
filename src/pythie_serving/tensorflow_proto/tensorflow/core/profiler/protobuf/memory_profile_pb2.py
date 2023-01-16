# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/protobuf/memory_profile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6tensorflow/core/profiler/protobuf/memory_profile.proto\x12\x13tensorflow.profiler\"\xa1\x01\n\x16MemoryAggregationStats\x12\x1c\n\x14stack_reserved_bytes\x18\x01 \x01(\x03\x12\x1c\n\x14heap_allocated_bytes\x18\x02 \x01(\x03\x12\x19\n\x11\x66ree_memory_bytes\x18\x03 \x01(\x03\x12\x15\n\rfragmentation\x18\x04 \x01(\x01\x12\x19\n\x11peak_bytes_in_use\x18\x05 \x01(\x03\"\xfd\x01\n\x16MemoryActivityMetadata\x12<\n\x0fmemory_activity\x18\x01 \x01(\x0e\x32#.tensorflow.profiler.MemoryActivity\x12\x17\n\x0frequested_bytes\x18\x02 \x01(\x03\x12\x18\n\x10\x61llocation_bytes\x18\x03 \x01(\x03\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\x04\x12\x12\n\ntf_op_name\x18\x05 \x01(\t\x12\x0f\n\x07step_id\x18\x06 \x01(\x03\x12\x13\n\x0bregion_type\x18\x07 \x01(\t\x12\x11\n\tdata_type\x18\x08 \x01(\t\x12\x14\n\x0ctensor_shape\x18\t \x01(\t\"\xbf\x01\n\x15MemoryProfileSnapshot\x12\x16\n\x0etime_offset_ps\x18\x01 \x01(\x03\x12\x46\n\x11\x61ggregation_stats\x18\x02 \x01(\x0b\x32+.tensorflow.profiler.MemoryAggregationStats\x12\x46\n\x11\x61\x63tivity_metadata\x18\x03 \x01(\x0b\x32+.tensorflow.profiler.MemoryActivityMetadata\"\xaf\x01\n\x14MemoryProfileSummary\x12!\n\x19peak_bytes_usage_lifetime\x18\x01 \x01(\x03\x12?\n\npeak_stats\x18\x02 \x01(\x0b\x32+.tensorflow.profiler.MemoryAggregationStats\x12\x1a\n\x12peak_stats_time_ps\x18\x03 \x01(\x03\x12\x17\n\x0fmemory_capacity\x18\x04 \x01(\x03\"Z\n\x10\x41\x63tiveAllocation\x12\x16\n\x0esnapshot_index\x18\x01 \x01(\x03\x12\x15\n\rspecial_index\x18\x02 \x01(\x03\x12\x17\n\x0fnum_occurrences\x18\x03 \x01(\x03\"\x8a\x03\n\x19PerAllocatorMemoryProfile\x12L\n\x18memory_profile_snapshots\x18\x01 \x03(\x0b\x32*.tensorflow.profiler.MemoryProfileSnapshot\x12\x42\n\x0fprofile_summary\x18\x02 \x01(\x0b\x32).tensorflow.profiler.MemoryProfileSummary\x12\x41\n\x12\x61\x63tive_allocations\x18\x03 \x03(\x0b\x32%.tensorflow.profiler.ActiveAllocation\x12H\n\x13special_allocations\x18\x04 \x03(\x0b\x32+.tensorflow.profiler.MemoryActivityMetadata\x12N\n\x1asampled_timeline_snapshots\x18\x05 \x03(\x0b\x32*.tensorflow.profiler.MemoryProfileSnapshot\"\xa8\x02\n\rMemoryProfile\x12g\n\x1cmemory_profile_per_allocator\x18\x01 \x03(\x0b\x32\x41.tensorflow.profiler.MemoryProfile.MemoryProfilePerAllocatorEntry\x12\x11\n\tnum_hosts\x18\x02 \x01(\x05\x12\x12\n\nmemory_ids\x18\x03 \x03(\t\x12\x0f\n\x07version\x18\x05 \x01(\x05\x1ap\n\x1eMemoryProfilePerAllocatorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..tensorflow.profiler.PerAllocatorMemoryProfile:\x02\x38\x01J\x04\x08\x04\x10\x05*h\n\x0eMemoryActivity\x12\x14\n\x10UNKNOWN_ACTIVITY\x10\x00\x12\x0e\n\nALLOCATION\x10\x01\x12\x10\n\x0c\x44\x45\x41LLOCATION\x10\x02\x12\x0f\n\x0bRESERVATION\x10\x03\x12\r\n\tEXPANSION\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.profiler.protobuf.memory_profile_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MEMORYPROFILE_MEMORYPROFILEPERALLOCATORENTRY._options = None
  _MEMORYPROFILE_MEMORYPROFILEPERALLOCATORENTRY._serialized_options = b'8\001'
  _MEMORYACTIVITY._serialized_start=1659
  _MEMORYACTIVITY._serialized_end=1763
  _MEMORYAGGREGATIONSTATS._serialized_start=80
  _MEMORYAGGREGATIONSTATS._serialized_end=241
  _MEMORYACTIVITYMETADATA._serialized_start=244
  _MEMORYACTIVITYMETADATA._serialized_end=497
  _MEMORYPROFILESNAPSHOT._serialized_start=500
  _MEMORYPROFILESNAPSHOT._serialized_end=691
  _MEMORYPROFILESUMMARY._serialized_start=694
  _MEMORYPROFILESUMMARY._serialized_end=869
  _ACTIVEALLOCATION._serialized_start=871
  _ACTIVEALLOCATION._serialized_end=961
  _PERALLOCATORMEMORYPROFILE._serialized_start=964
  _PERALLOCATORMEMORYPROFILE._serialized_end=1358
  _MEMORYPROFILE._serialized_start=1361
  _MEMORYPROFILE._serialized_end=1657
  _MEMORYPROFILE_MEMORYPROFILEPERALLOCATORENTRY._serialized_start=1539
  _MEMORYPROFILE_MEMORYPROFILEPERALLOCATORENTRY._serialized_end=1651
# @@protoc_insertion_point(module_scope)
