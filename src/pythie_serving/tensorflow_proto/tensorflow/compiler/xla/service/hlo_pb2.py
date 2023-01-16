# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/xla/service/hlo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.compiler.xla import xla_data_pb2 as tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)tensorflow/compiler/xla/service/hlo.proto\x12\x03xla\x1a&tensorflow/compiler/xla/xla_data.proto\"\x95\x15\n\x13HloInstructionProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06opcode\x18\x02 \x01(\t\x12\x1e\n\x05shape\x18\x03 \x01(\x0b\x32\x0f.xla.ShapeProto\x12!\n\x08metadata\x18\x07 \x01(\x0b\x32\x0f.xla.OpMetadata\x12\"\n\x07literal\x18\x08 \x01(\x0b\x32\x11.xla.LiteralProto\x12\x18\n\x10parameter_number\x18\t \x01(\x03\x12\x13\n\x0b\x66usion_kind\x18\x0b \x01(\t\x12\x13\n\x0btuple_index\x18\r \x01(\x03\x12\x12\n\ndimensions\x18\x0e \x03(\x03\x12\x1b\n\x06window\x18\x0f \x01(\x0b\x32\x0b.xla.Window\x12G\n\x1d\x63onvolution_dimension_numbers\x18\x10 \x01(\x0b\x32 .xla.ConvolutionDimensionNumbers\x12\x1b\n\x13\x66\x65\x61ture_group_count\x18\x32 \x01(\x03\x12\x19\n\x11\x62\x61tch_group_count\x18: \x01(\x03\x12\x42\n\x10slice_dimensions\x18\x11 \x03(\x0b\x32(.xla.HloInstructionProto.SliceDimensions\x12\x15\n\rexponent_bits\x18\x12 \x01(\x05\x12\x15\n\rmantissa_bits\x18\x13 \x01(\x05\x12\x1b\n\x13\x64ynamic_slice_sizes\x18\x14 \x03(\x03\x12*\n\x0epadding_config\x18\x15 \x01(\x0b\x32\x12.xla.PaddingConfig\x12\x16\n\x0eoutfeed_config\x18\x16 \x01(\x0c\x12-\n\x0c\x64istribution\x18\x17 \x01(\x0e\x32\x17.xla.RandomDistribution\x12\x0f\n\x07\x65psilon\x18\x18 \x01(\x02\x12\x15\n\rfeature_index\x18\x19 \x01(\x03\x12\x12\n\nchannel_id\x18\x1a \x01(\x03\x12\x15\n\rinfeed_config\x18\x1b \x01(\x0c\x12\x1a\n\x12\x63ustom_call_target\x18\x1c \x01(\t\x12&\n\routfeed_shape\x18\x1d \x01(\x0b\x32\x0f.xla.ShapeProto\x12\x37\n\x15\x64ot_dimension_numbers\x18\x1e \x01(\x0b\x32\x18.xla.DotDimensionNumbers\x12\x1e\n\x08\x66\x66t_type\x18\x1f \x01(\x0e\x32\x0c.xla.FftType\x12\x12\n\nfft_length\x18  \x03(\x03\x12\x1c\n\x14\x63omparison_direction\x18? \x01(\t\x12=\n\x18gather_dimension_numbers\x18! \x01(\x0b\x32\x1b.xla.GatherDimensionNumbers\x12\x1a\n\x12gather_slice_sizes\x18\" \x03(\x03\x12\n\n\x02id\x18# \x01(\x03\x12\x13\n\x0boperand_ids\x18$ \x03(\x03\x12\x1f\n\x17\x63ontrol_predecessor_ids\x18% \x03(\x03\x12\x1e\n\x16\x63\x61lled_computation_ids\x18& \x03(\x03\x12!\n\x08sharding\x18( \x01(\x0b\x32\x0f.xla.OpSharding\x12\x16\n\x0e\x62\x61\x63kend_config\x18+ \x01(\x0c\x12)\n\x0ereplica_groups\x18\x31 \x03(\x0b\x32\x11.xla.ReplicaGroup\x12\x19\n\rall_reduce_id\x18- \x01(\x03\x42\x02\x18\x01\x12\x1d\n\x15use_global_device_ids\x18G \x01(\x08\x12\x18\n\x10is_host_transfer\x18/ \x01(\x08\x12\x11\n\tis_stable\x18< \x01(\x08\x12?\n\x19scatter_dimension_numbers\x18\x30 \x01(\x0b\x32\x1c.xla.ScatterDimensionNumbers\x12.\n\x10precision_config\x18\x33 \x01(\x0b\x32\x14.xla.PrecisionConfig\x12.\n\x13source_target_pairs\x18\x34 \x03(\x0b\x32\x11.xla.SourceTarget\x12.\n\x15\x64omain_entry_sharding\x18\x36 \x01(\x0b\x32\x0f.xla.OpSharding\x12-\n\x14\x64omain_exit_sharding\x18\x37 \x01(\x0b\x32\x0f.xla.OpSharding\x12\x18\n\x10\x63onstrain_layout\x18\x38 \x01(\x08\x12\x33\n\x1aoperand_shapes_with_layout\x18\x39 \x03(\x0b\x32\x0f.xla.ShapeProto\x12=\n\x18triangular_solve_options\x18; \x01(\x0b\x32\x1b.xla.TriangularSolveOptions\x12.\n\x10\x63holesky_options\x18> \x01(\x0b\x32\x14.xla.CholeskyOptions\x12\x38\n\x15parameter_replication\x18= \x01(\x0b\x32\x19.xla.ParameterReplication\x12#\n\x1b\x63ustom_call_has_side_effect\x18\x41 \x01(\x08\x12Q\n#custom_call_output_operand_aliasing\x18J \x03(\x0b\x32$.xla.CustomCallOutputOperandAliasing\x12\x35\n\x14\x63ustom_call_schedule\x18L \x01(\x0e\x32\x17.xla.CustomCallSchedule\x12\r\n\x05\x64\x65lta\x18\x42 \x01(\x03\x12\x1a\n\x12indices_are_sorted\x18\x43 \x01(\x08\x12\x34\n\x13\x66rontend_attributes\x18\x44 \x01(\x0b\x32\x17.xla.FrontendAttributes\x12\x16\n\x0eunique_indices\x18\x45 \x01(\x08\x12+\n\rrng_algorithm\x18\x46 \x01(\x0e\x32\x14.xla.RandomAlgorithm\x12\x17\n\x0f\x63omparison_type\x18H \x01(\t\x12!\n\x19is_cross_program_prefetch\x18I \x01(\x08\x12&\n\x0cpadding_type\x18K \x01(\x0e\x32\x10.xla.PaddingType\x12:\n\x17\x63ustom_call_api_version\x18M \x01(\x0e\x32\x19.xla.CustomCallApiVersion\x12\x16\n\x0e\x61sync_group_id\x18N \x01(\x03\x12\x1e\n\x16\x61sync_execution_thread\x18O \x01(\t\x1a?\n\x0fSliceDimensions\x12\r\n\x05start\x18\x01 \x01(\x03\x12\r\n\x05limit\x18\x02 \x01(\x03\x12\x0e\n\x06stride\x18\x03 \x01(\x03J\x04\x08\n\x10\x0bJ\x04\x08\x0c\x10\rJ\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08,\x10-J\x04\x08\x35\x10\x36J\x04\x08.\x10/J\x04\x08)\x10*J\x04\x08*\x10+J\x04\x08@\x10\x41R\x0eparameter_nameR\x1e\x66used_instructions_computationR\roperand_namesR\x19\x63ontrol_predecessor_namesR\x18\x63\x61lled_computation_namesR\x11replica_group_idsR\x12\x63ustom_call_opaqueR\x12\x61ll_reduce_barrier\"\xe9\x01\n\x13HloComputationProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x0cinstructions\x18\x02 \x03(\x0b\x32\x18.xla.HloInstructionProto\x12-\n\rprogram_shape\x18\x04 \x01(\x0b\x32\x16.xla.ProgramShapeProto\x12\n\n\x02id\x18\x05 \x01(\x03\x12\x0f\n\x07root_id\x18\x06 \x01(\x03\x12\x1d\n\x15is_fusion_computation\x18\x07 \x01(\x08\x12\x18\n\x10\x65xecution_thread\x18\x08 \x01(\tJ\x04\x08\x03\x10\x04R\troot_name\"\xd8\x01\n\x10HloScheduleProto\x12\x37\n\tsequences\x18\x01 \x03(\x0b\x32$.xla.HloScheduleProto.SequencesEntry\x1a.\n\x13InstructionSequence\x12\x17\n\x0finstruction_ids\x18\x01 \x03(\x03\x1a[\n\x0eSequencesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).xla.HloScheduleProto.InstructionSequence:\x02\x38\x01\"\xdb\x01\n\x18HloInputOutputAliasProto\x12>\n\x07\x65ntries\x18\x01 \x03(\x0b\x32-.xla.HloInputOutputAliasProto.AliasEntryProto\x1a\x7f\n\x0f\x41liasEntryProto\x12\x1a\n\x12output_shape_index\x18\x01 \x03(\x03\x12\x18\n\x10parameter_number\x18\x02 \x01(\x03\x12\x1d\n\x15parameter_shape_index\x18\x03 \x03(\x03\x12\x17\n\x04kind\x18\x04 \x01(\x0e\x32\t.xla.Kind\"\xf2\x01\n\x1c\x44ynamicParameterBindingProto\x12:\n\x07\x65ntries\x18\x01 \x03(\x0b\x32).xla.DynamicParameterBindingProto.Binding\x1a\x95\x01\n\x07\x42inding\x12\x19\n\x11\x64ynamic_param_num\x18\x01 \x01(\x03\x12\x1b\n\x13\x64ynamic_param_index\x18\x02 \x03(\x03\x12\x18\n\x10target_param_num\x18\x03 \x01(\x03\x12\x1a\n\x12target_param_index\x18\x04 \x03(\x03\x12\x1c\n\x14target_param_dim_num\x18\x05 \x01(\x03\"8\n\x14\x43rossProgramPrefetch\x12\x11\n\tparameter\x18\x01 \x01(\x03\x12\r\n\x05index\x18\x02 \x03(\x03\"\xc2\x07\n\x0eHloModuleProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16\x65ntry_computation_name\x18\x02 \x01(\t\x12\x1c\n\x14\x65ntry_computation_id\x18\x06 \x01(\x03\x12.\n\x0c\x63omputations\x18\x03 \x03(\x0b\x32\x18.xla.HloComputationProto\x12\x32\n\x12host_program_shape\x18\x04 \x01(\x0b\x32\x16.xla.ProgramShapeProto\x12\n\n\x02id\x18\x05 \x01(\x03\x12\'\n\x08schedule\x18\x07 \x01(\x0b\x32\x15.xla.HloScheduleProto\x12\x39\n\x12input_output_alias\x18\x08 \x01(\x0b\x32\x1d.xla.HloInputOutputAliasProto\x12\x44\n\x19\x64ynamic_parameter_binding\x18\t \x01(\x0b\x32!.xla.DynamicParameterBindingProto\x12;\n\x18\x63ross_program_prefetches\x18\n \x03(\x0b\x32\x19.xla.CrossProgramPrefetch\x12\x12\n\nis_dynamic\x18\x0b \x01(\x08\x12-\n\x14spmd_output_sharding\x18\x0c \x01(\x0b\x32\x0f.xla.OpSharding\x12\x32\n\x19spmd_parameters_shardings\x18\x0e \x03(\x0b\x32\x0f.xla.OpSharding\x12\"\n\x1ause_auto_spmd_partitioning\x18\x10 \x01(\x08\x12\x35\n\x0cprofile_info\x18\r \x03(\x0b\x32\x1f.xla.HloModuleProto.ProfileInfo\x12\x35\n\x11\x64\x65vice_assignment\x18\x0f \x01(\x0b\x32\x1a.xla.DeviceAssignmentProto\x1a\xbc\x01\n\x0bProfileInfo\x12\x35\n\x0cprofile_type\x18\x01 \x01(\x0e\x32\x1f.xla.HloModuleProto.ProfileType\x12\x18\n\x10relative_speedup\x18\x02 \x01(\x01\x12*\n\x0eprofile_source\x18\x03 \x01(\x0e\x32\x12.xla.ProfileSource\x12\x30\n\x11\x63ompilation_event\x18\x04 \x01(\x0e\x32\x15.xla.CompilationEvent\"E\n\x0bProfileType\x12\x0b\n\x07INVALID\x10\x00\x12\x08\n\x04\x46LAG\x10\x01\x12\n\n\x06\x46USION\x10\x02\x12\n\n\x06LAYOUT\x10\x03\x12\x07\n\x03\x44OT\x10\x04\"\xe8\x01\n\x12LogicalBufferProto\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x34\n\ndefined_at\x18\x03 \x01(\x0b\x32 .xla.LogicalBufferProto.Location\x12\r\n\x05\x63olor\x18\x04 \x01(\x03\x1as\n\x08Location\x12\x1c\n\x10\x63omputation_name\x18\x01 \x01(\tB\x02\x18\x01\x12\x1c\n\x10instruction_name\x18\x02 \x01(\tB\x02\x18\x01\x12\x16\n\x0einstruction_id\x18\x04 \x01(\x03\x12\x13\n\x0bshape_index\x18\x03 \x03(\x03\"\xf8\x02\n\x15\x42ufferAllocationProto\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x17\n\x0fis_thread_local\x18\x03 \x01(\x08\x12\x10\n\x08is_tuple\x18\x0b \x01(\x08\x12&\n\x1eis_entry_computation_parameter\x18\x05 \x01(\x08\x12\x13\n\x0bis_constant\x18\x0c \x01(\x08\x12\x18\n\x10parameter_number\x18\x06 \x01(\x03\x12\x1d\n\x15parameter_shape_index\x18\n \x03(\x03\x12\x16\n\x0emaybe_live_out\x18\x07 \x01(\x08\x12\r\n\x05\x63olor\x18\x08 \x01(\x03\x12\x35\n\x08\x61ssigned\x18\t \x03(\x0b\x32#.xla.BufferAllocationProto.Assigned\x1a\x43\n\x08\x41ssigned\x12\x19\n\x11logical_buffer_id\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04size\x18\x03 \x01(\x03\"\xd6\x02\n\x12HeapSimulatorTrace\x12-\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1d.xla.HeapSimulatorTrace.Event\x12\x1f\n\x17whole_module_simulation\x18\x02 \x01(\x08\x12\x1f\n\x17\x62uffer_allocation_index\x18\x03 \x01(\x03\x1a\xce\x01\n\x05\x45vent\x12\x30\n\x04kind\x18\x01 \x01(\x0e\x32\".xla.HeapSimulatorTrace.Event.Kind\x12\x11\n\tbuffer_id\x18\x02 \x01(\x03\x12\x18\n\x10\x63omputation_name\x18\x03 \x01(\t\x12\x18\n\x10instruction_name\x18\x04 \x01(\t\x12\x1f\n\x17share_with_canonical_id\x18\x05 \x01(\x03\"+\n\x04Kind\x12\t\n\x05\x41LLOC\x10\x00\x12\x08\n\x04\x46REE\x10\x01\x12\x0e\n\nSHARE_WITH\x10\x02\"M\n\x13HloModuleGroupProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x0bhlo_modules\x18\x02 \x03(\x0b\x32\x13.xla.HloModuleProto\"\xd6\x02\n\x15\x42ufferAssignmentProto\x12\x30\n\x0flogical_buffers\x18\x01 \x03(\x0b\x32\x17.xla.LogicalBufferProto\x12>\n\x0e\x62uffer_aliases\x18\x02 \x03(\x0b\x32&.xla.BufferAssignmentProto.BufferAlias\x12\x36\n\x12\x62uffer_allocations\x18\x03 \x03(\x0b\x32\x1a.xla.BufferAllocationProto\x12\x36\n\x15heap_simulator_traces\x18\x04 \x03(\x0b\x32\x17.xla.HeapSimulatorTrace\x1a[\n\x0b\x42ufferAlias\x12\x18\n\x10source_buffer_id\x18\x01 \x01(\x03\x12\x32\n\x08location\x18\x02 \x01(\x0b\x32 .xla.LogicalBufferProto.Location\"~\n\x08HloProto\x12\'\n\nhlo_module\x18\x01 \x01(\x0b\x32\x13.xla.HloModuleProto\x12\x35\n\x11\x62uffer_assignment\x18\x03 \x01(\x0b\x32\x1a.xla.BufferAssignmentProtoJ\x04\x08\x02\x10\x03R\x0chlo_ordering\"\x8e\x01\n\x0bHloSnapshot\x12\x1a\n\x03hlo\x18\x01 \x01(\x0b\x32\r.xla.HloProto\x12$\n\targuments\x18\x02 \x03(\x0b\x32\x11.xla.LiteralProto\x12!\n\x06result\x18\x03 \x01(\x0b\x32\x11.xla.LiteralProto\x12\x1a\n\x12\x65xecution_platform\x18\x04 \x01(\t\"\xb9\x01\n\x16HloModuleMetadataProto\x12\x1b\n\x13\x63\x61nonical_module_id\x18\x01 \x01(\x03\x12\x19\n\x11module_group_name\x18\x02 \x01(\t\x12\x1a\n\x12original_module_id\x18\x03 \x01(\x03\x12\x1e\n\x16partitioned_module_ids\x18\x04 \x03(\x03\x12+\n\rpass_metadata\x18\x05 \x03(\x0b\x32\x14.xla.HloPassMetadata\"\xea\x01\n\x0fHloPassMetadata\x12\x0f\n\x07pass_id\x18\x01 \x01(\x03\x12\x11\n\tpass_name\x18\x02 \x01(\t\x12\x15\n\rpipeline_name\x18\x03 \x01(\t\x12\x16\n\x0e\x64ump_filenames\x18\x04 \x03(\t\x12\x16\n\x0emodule_changed\x18\x05 \x01(\x08\x12\x11\n\tmodule_id\x18\x06 \x01(\x03\x12\x1f\n\x17module_group_module_ids\x18\x07 \x03(\x03\x12\x1c\n\x14start_timestamp_usec\x18\x08 \x01(\x03\x12\x1a\n\x12\x65nd_timestamp_usec\x18\t \x01(\x03\"\xb3\x03\n\x17\x45ntryFunctionAttributes\x12G\n\x07\x62uffers\x18\x01 \x03(\x0b\x32\x36.xla.EntryFunctionAttributes.BufferParameterAttributes\x12\x18\n\x10result_xla_shape\x18\x02 \x01(\t\x1a\x1d\n\nShapeIndex\x12\x0f\n\x07indices\x18\x01 \x03(\x03\x1a\x95\x02\n\x19\x42ufferParameterAttributes\x12\x14\n\x0clmhlo_params\x18\x01 \x01(\x03\x12\x1c\n\x14lmhlo_params_present\x18\x06 \x01(\x08\x12H\n\x17lmhlo_param_shape_index\x18\x02 \x01(\x0b\x32\'.xla.EntryFunctionAttributes.ShapeIndex\x12\x1b\n\x13lmhlo_constant_name\x18\x03 \x01(\t\x12\x18\n\x10lmhlo_must_alias\x18\x04 \x01(\x08\x12\x43\n\x12lmhlo_output_index\x18\x05 \x01(\x0b\x32\'.xla.EntryFunctionAttributes.ShapeIndex\"\xa9\x01\n\x19XlaRuntimeExecutableProto\x12-\n\x10hlo_module_proto\x18\x01 \x01(\x0b\x32\x13.xla.HloModuleProto\x12\x36\n\x10\x65ntry_func_attrs\x18\x02 \x01(\x0b\x32\x1c.xla.EntryFunctionAttributes\x12\x10\n\x08obj_file\x18\x03 \x01(\x0c\x12\x13\n\x0bmlir_module\x18\x04 \x01(\t*S\n\x12\x43ustomCallSchedule\x12\x11\n\rSCHEDULE_NONE\x10\x00\x12\x13\n\x0fSCHEDULE_LATEST\x10\x01\x12\x15\n\x11SCHEDULE_EARLIEST\x10\x02*\x99\x01\n\x14\x43ustomCallApiVersion\x12\x1b\n\x17\x41PI_VERSION_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41PI_VERSION_ORIGINAL\x10\x01\x12 \n\x1c\x41PI_VERSION_STATUS_RETURNING\x10\x02\x12(\n$API_VERSION_STATUS_RETURNING_UNIFIED\x10\x03*:\n\x04Kind\x12\x13\n\x0fUNDEFINED_ALIAS\x10\x00\x12\r\n\tMAY_ALIAS\x10\x01\x12\x0e\n\nMUST_ALIAS\x10\x02\x42\x03\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.compiler.xla.service.hlo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _HLOINSTRUCTIONPROTO.fields_by_name['all_reduce_id']._options = None
  _HLOINSTRUCTIONPROTO.fields_by_name['all_reduce_id']._serialized_options = b'\030\001'
  _HLOSCHEDULEPROTO_SEQUENCESENTRY._options = None
  _HLOSCHEDULEPROTO_SEQUENCESENTRY._serialized_options = b'8\001'
  _LOGICALBUFFERPROTO_LOCATION.fields_by_name['computation_name']._options = None
  _LOGICALBUFFERPROTO_LOCATION.fields_by_name['computation_name']._serialized_options = b'\030\001'
  _LOGICALBUFFERPROTO_LOCATION.fields_by_name['instruction_name']._options = None
  _LOGICALBUFFERPROTO_LOCATION.fields_by_name['instruction_name']._serialized_options = b'\030\001'
  _CUSTOMCALLSCHEDULE._serialized_start=7438
  _CUSTOMCALLSCHEDULE._serialized_end=7521
  _CUSTOMCALLAPIVERSION._serialized_start=7524
  _CUSTOMCALLAPIVERSION._serialized_end=7677
  _KIND._serialized_start=7679
  _KIND._serialized_end=7737
  _HLOINSTRUCTIONPROTO._serialized_start=91
  _HLOINSTRUCTIONPROTO._serialized_end=2800
  _HLOINSTRUCTIONPROTO_SLICEDIMENSIONS._serialized_start=2496
  _HLOINSTRUCTIONPROTO_SLICEDIMENSIONS._serialized_end=2559
  _HLOCOMPUTATIONPROTO._serialized_start=2803
  _HLOCOMPUTATIONPROTO._serialized_end=3036
  _HLOSCHEDULEPROTO._serialized_start=3039
  _HLOSCHEDULEPROTO._serialized_end=3255
  _HLOSCHEDULEPROTO_INSTRUCTIONSEQUENCE._serialized_start=3116
  _HLOSCHEDULEPROTO_INSTRUCTIONSEQUENCE._serialized_end=3162
  _HLOSCHEDULEPROTO_SEQUENCESENTRY._serialized_start=3164
  _HLOSCHEDULEPROTO_SEQUENCESENTRY._serialized_end=3255
  _HLOINPUTOUTPUTALIASPROTO._serialized_start=3258
  _HLOINPUTOUTPUTALIASPROTO._serialized_end=3477
  _HLOINPUTOUTPUTALIASPROTO_ALIASENTRYPROTO._serialized_start=3350
  _HLOINPUTOUTPUTALIASPROTO_ALIASENTRYPROTO._serialized_end=3477
  _DYNAMICPARAMETERBINDINGPROTO._serialized_start=3480
  _DYNAMICPARAMETERBINDINGPROTO._serialized_end=3722
  _DYNAMICPARAMETERBINDINGPROTO_BINDING._serialized_start=3573
  _DYNAMICPARAMETERBINDINGPROTO_BINDING._serialized_end=3722
  _CROSSPROGRAMPREFETCH._serialized_start=3724
  _CROSSPROGRAMPREFETCH._serialized_end=3780
  _HLOMODULEPROTO._serialized_start=3783
  _HLOMODULEPROTO._serialized_end=4745
  _HLOMODULEPROTO_PROFILEINFO._serialized_start=4486
  _HLOMODULEPROTO_PROFILEINFO._serialized_end=4674
  _HLOMODULEPROTO_PROFILETYPE._serialized_start=4676
  _HLOMODULEPROTO_PROFILETYPE._serialized_end=4745
  _LOGICALBUFFERPROTO._serialized_start=4748
  _LOGICALBUFFERPROTO._serialized_end=4980
  _LOGICALBUFFERPROTO_LOCATION._serialized_start=4865
  _LOGICALBUFFERPROTO_LOCATION._serialized_end=4980
  _BUFFERALLOCATIONPROTO._serialized_start=4983
  _BUFFERALLOCATIONPROTO._serialized_end=5359
  _BUFFERALLOCATIONPROTO_ASSIGNED._serialized_start=5292
  _BUFFERALLOCATIONPROTO_ASSIGNED._serialized_end=5359
  _HEAPSIMULATORTRACE._serialized_start=5362
  _HEAPSIMULATORTRACE._serialized_end=5704
  _HEAPSIMULATORTRACE_EVENT._serialized_start=5498
  _HEAPSIMULATORTRACE_EVENT._serialized_end=5704
  _HEAPSIMULATORTRACE_EVENT_KIND._serialized_start=5661
  _HEAPSIMULATORTRACE_EVENT_KIND._serialized_end=5704
  _HLOMODULEGROUPPROTO._serialized_start=5706
  _HLOMODULEGROUPPROTO._serialized_end=5783
  _BUFFERASSIGNMENTPROTO._serialized_start=5786
  _BUFFERASSIGNMENTPROTO._serialized_end=6128
  _BUFFERASSIGNMENTPROTO_BUFFERALIAS._serialized_start=6037
  _BUFFERASSIGNMENTPROTO_BUFFERALIAS._serialized_end=6128
  _HLOPROTO._serialized_start=6130
  _HLOPROTO._serialized_end=6256
  _HLOSNAPSHOT._serialized_start=6259
  _HLOSNAPSHOT._serialized_end=6401
  _HLOMODULEMETADATAPROTO._serialized_start=6404
  _HLOMODULEMETADATAPROTO._serialized_end=6589
  _HLOPASSMETADATA._serialized_start=6592
  _HLOPASSMETADATA._serialized_end=6826
  _ENTRYFUNCTIONATTRIBUTES._serialized_start=6829
  _ENTRYFUNCTIONATTRIBUTES._serialized_end=7264
  _ENTRYFUNCTIONATTRIBUTES_SHAPEINDEX._serialized_start=6955
  _ENTRYFUNCTIONATTRIBUTES_SHAPEINDEX._serialized_end=6984
  _ENTRYFUNCTIONATTRIBUTES_BUFFERPARAMETERATTRIBUTES._serialized_start=6987
  _ENTRYFUNCTIONATTRIBUTES_BUFFERPARAMETERATTRIBUTES._serialized_end=7264
  _XLARUNTIMEEXECUTABLEPROTO._serialized_start=7267
  _XLARUNTIMEEXECUTABLEPROTO._serialized_end=7436
# @@protoc_insertion_point(module_scope)
