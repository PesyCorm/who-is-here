from Common.OutputFormat import return_output
import time

class SystemWork:

    def __enter__(self):

        self.system_work_time = time.time()
        _output_text = "The system was launched at " + time.ctime()
        print(return_output(_output_text, "-"))


    def __exit__(self, exc_type, exc_val, exc_tb):
    	
        _output_text = "Shutting down the system"
        print(return_output("Shutting down the system", "_"))
        print(return_output(f"Working time: {int(time.time() - self.system_work_time)} sec", "="))
