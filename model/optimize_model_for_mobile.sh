#!/bin/bash

docker run -it -p 8888:8888 -v $HOME/tf_files:/tf_files \
	tensorflow/tensorflow:nightly-devel

cd /tensorflow/
bazel build tensorflow/examples/label_image:label_image

bazel build tensorflow/python/tools:optimize_for_inference
bazel-bin/tensorflow/python/tools/optimize_for_inference \
	--input=/tf_files/retrained_graph.pb \
	--output=/tf_files/optimized_graph.pb \
	--input_names=Mul \
	--output_names=final_result

bazel build tensorflow/tools/quantization:quantize_graph
bazel-bin/tensorflow/tools/quantization/quantize_graph \
	--input=/tf_files/optimized_graph.pb \
	--output=/tf_files/rounded_graph.pb \
	--output_node_names=final_result \
	--mode=weights_rounded

bazel build tensorflow/contrib/util:convert_graphdef_memmapped_format
bazel-bin/tensorflow/contrib/util/convert_graphdef_memmapped_format \
	--in_graph=/tf_files/rounded_graph.pb \
	--out_graph=/tf_files/mmapped_graph.pb


