"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class TPUEmbeddingOutputLayout(google.protobuf.message.Message):
    """In the comments here, "layout" refers to the top-level EmbeddingOutputLayout
    proto contained in the TPUEmbeddingConfiguration.

    This proto is deprecated and its contents are no longer used.

    The embedding output consists of a list of tensors, each specified by an
    EmbeddingOutputTensor proto within the EmbeddingOutputLayout (the "output"
    field). Each table and feature lookup is then placed into some number of
    particular positions within some output tensor (identified by "tensor_index"
    within OutputLocation). The tree of table lookups, feature lookups, and
    output locations is specified by the
    "table(table_id).feature(feature_id).output_location" repeated fields within
    EmbeddingOutputLayout.

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OutputLocation(google.protobuf.message.Message):
        """Location of one copy of the feature's data."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TENSOR_INDEX_FIELD_NUMBER: builtins.int
        DIM0_OFFSET_FIELD_NUMBER: builtins.int
        DIM1_OFFSET_FIELD_NUMBER: builtins.int
        tensor_index: builtins.int
        """Which output tensor this copy of the feature will go into. Must be
        between 0 and layout.output_size().
        """

        dim0_offset: builtins.int
        """Offset in dimension 0 for this feature copy. Must be between 0 and
        layout.output(tensor_index).dim0_size_per_sample().
        """

        dim1_offset: builtins.int
        """Offset in dimension 1 for this feature copy. Must be between 0 and
        layout.output(tensor_index).dim1_size() - table width; repeated or
        partially/fully overlapping values are allowed and results in the same
        range will be summed (with the gradients replicated in the backward
        pass).
        """

        def __init__(self,
            *,
            tensor_index: builtins.int = ...,
            dim0_offset: builtins.int = ...,
            dim1_offset: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["dim0_offset",b"dim0_offset","dim1_offset",b"dim1_offset","tensor_index",b"tensor_index"]) -> None: ...

    class FeatureDescriptor(google.protobuf.message.Message):
        """Description of the output placement for one feature."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        OUTPUT_LOCATION_FIELD_NUMBER: builtins.int
        @property
        def output_location(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TPUEmbeddingOutputLayout.OutputLocation]:
            """Typically, only one copy of each feature is used, but multiple are
            allowed and the same data will be copied to all of them (with the
            gradients summed in the backward pass).
            """
            pass
        def __init__(self,
            *,
            output_location: typing.Optional[typing.Iterable[global___TPUEmbeddingOutputLayout.OutputLocation]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["output_location",b"output_location"]) -> None: ...

    class TableDescriptor(google.protobuf.message.Message):
        """Description of the output placement for features of one table."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        FEATURE_FIELD_NUMBER: builtins.int
        @property
        def feature(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TPUEmbeddingOutputLayout.FeatureDescriptor]:
            """Output locations for each feature loaded from this table."""
            pass
        def __init__(self,
            *,
            feature: typing.Optional[typing.Iterable[global___TPUEmbeddingOutputLayout.FeatureDescriptor]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["feature",b"feature"]) -> None: ...

    class TwoDOutputTensor(google.protobuf.message.Message):
        """Data layout and shape computation information for a single output tensor.
        Any unused locations in the tensor will be filled with zeros, and
        corresponding gradients will be ignored.

        Size and layout information for 2-D tensors.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        DIM0_SIZE_PER_SAMPLE_FIELD_NUMBER: builtins.int
        DIM1_SIZE_FIELD_NUMBER: builtins.int
        dim0_size_per_sample: builtins.int
        """Multiplier for output dimension 0 size; used to match legacy format that
        stacks features within a sample in dimension 0.
        """

        dim1_size: builtins.int
        """The size (in dimension 1) of this output tensor."""

        def __init__(self,
            *,
            dim0_size_per_sample: builtins.int = ...,
            dim1_size: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["dim0_size_per_sample",b"dim0_size_per_sample","dim1_size",b"dim1_size"]) -> None: ...

    class EmbeddingOutputTensor(google.protobuf.message.Message):
        """Format information for a single output tensor."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TWO_D_FIELD_NUMBER: builtins.int
        @property
        def two_d(self) -> global___TPUEmbeddingOutputLayout.TwoDOutputTensor: ...
        def __init__(self,
            *,
            two_d: typing.Optional[global___TPUEmbeddingOutputLayout.TwoDOutputTensor] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["output_format",b"output_format","two_d",b"two_d"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["output_format",b"output_format","two_d",b"two_d"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["output_format",b"output_format"]) -> typing.Optional[typing_extensions.Literal["two_d"]]: ...

    TABLE_FIELD_NUMBER: builtins.int
    OUTPUT_FIELD_NUMBER: builtins.int
    @property
    def table(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TPUEmbeddingOutputLayout.TableDescriptor]:
        """Output locations for each feature of each table."""
        pass
    @property
    def output(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TPUEmbeddingOutputLayout.EmbeddingOutputTensor]:
        """Shape and layout information for each tensor."""
        pass
    def __init__(self,
        *,
        table: typing.Optional[typing.Iterable[global___TPUEmbeddingOutputLayout.TableDescriptor]] = ...,
        output: typing.Optional[typing.Iterable[global___TPUEmbeddingOutputLayout.EmbeddingOutputTensor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["output",b"output","table",b"table"]) -> None: ...
global___TPUEmbeddingOutputLayout = TPUEmbeddingOutputLayout
