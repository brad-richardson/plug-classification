# Plug Classification

##[Website](https://bradsrichardson.github.io/plug-classification/)

## Setup

All of this work is largely based on information from these two tutorials:

####[TensorFlow for poets](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html)

####[TensorFlow for poets mobile](https://petewarden.com/2016/09/27/tensorflow-for-mobile-poets/)

If you get stuck on any of these steps, those sites will be very helpful in understanding better what is going on. This guide assumes that you are doing your work on macOS. If that isn't the case, please see the guides above.

Most important thing is to first download Docker:
https://docs.docker.com/docker-for-mac

Next, you need to train using your images. Start by placing your images into ~/tf_files/plug_images. Then, run `model/train_cmd.sh` from inside a docker quickstart terminal. You can skip this part if you don't want to collect your own images. I have included a pre-built model and labels in the model/ directory.

After you have your model trained (it should be at ~/tf_files/retrained_graph.pb with labels at ~/tf_files/retrained_labels.txt), run `model/optimize_model_for_mobile.sh` from the docker quickstart terminal.

Now, switch back to a macOS terminal and run `helper/setup_ios_environment.sh`. You should now be setup to build for iOS and able to open Xcode to build the app. 

Add your optimized model from ~/tf_files/mmapped_graph.pb to the data folder in the Xcode project and change the model settings to match the following:

```Objective-C
// If you have your own model, modify this to the file name, and make sure
// you've added the file to your app resources too.
static NSString* model_file_name = @"mmapped_graph";
static NSString* model_file_type = @"pb";
// This controls whether we'll be loading a plain GraphDef proto, or a
// file created by the convert_graphdef_memmapped_format utility that wraps a
// GraphDef and parameter file that can be mapped into memory from file to
// reduce overall memory usage.
const bool model_uses_memory_mapping = true;
// If you have your own model, point this to the labels file.
static NSString* labels_file_name = @"retrained_labels";
static NSString* labels_file_type = @"txt";
// These dimensions need to match those the model was trained with.
const int wanted_input_width = 299;
const int wanted_input_height = 299;
const int wanted_input_channels = 3;
const float input_mean = 128.0f;
const float input_std = 128.0f;
const std::string input_layer_name = "Mul";
const std::string output_layer_name = "final_result";
```

Now you should be able to build to a device and run the app!

