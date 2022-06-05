import os.path
import os
import subprocess

class GpuProfiler:
	def __init__(self, session_name):
		self.session_name = session_name
		if not os.path.exists(session_name):
			os.mkdir(session_name)

	def start_profiling(self, report_name):
		print("start profiling...")
		path = os.path.join(self.session_name, report_name)
		os.mkdir(path)
		proc = subprocess.run(["nsys", "start", "-o", os.path.join(path, report_name), "--gpu-metrics-device=all", "--gpu-metrics-frequency=25000"], capture_output=True)
		print(proc.stdout)
		print(proc.stderr)

	def stop_profiling(self):
		print("stop profiling...")
		proc = subprocess.run(["nsys", "stop"], capture_output=True)
		print(proc.stdout)
		print(proc.stderr)
	
	def create_stats(self):
		print("creating stats files...")
		for item in os.listdir(self.session_name):
			report_path = os.path.join(self.session_name, item, "%s.nsys-rep" % item)
			stats_path = os.path.join(self.session_name, item, item)
			if os.path.exists(report_path):
				print("creating stats for %s" % item)
				proc = subprocess.run(["nsys", "stats", report_path, "--format", "csv", "-o", stats_path, "--report", "apigpusum,cudaapisum,cudaapitrace,dx11pixsum,dx12gpumarkersum,dx12pixsum,gpukernsum,gpumemsizesum,gpumemtimesum,gpusum,gputrace,kernexecsum,kernexectrace,khrdebuggpusum,khrdebugsum,nvtxgpuproj,nvtxkernsum,nvtxppsum,nvtxpptrace,nvtxsesum,nvtxsssum,nvtxsum,openaccsum,openmpevtsum,osrtsum,umcpupagefaults,unifiedmemory,unifiedmemorytotals,vulkangpumarkersum,vulkanmarkerssum,wddmqueuesdetails"], capture_output=True)