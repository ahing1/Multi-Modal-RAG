import tensorrt as trt

try:
    print(f"✅ TensorRT version: {trt.__version__}")
except Exception as e:
    print(f"❌ TensorRT not installed properly: {e}")
