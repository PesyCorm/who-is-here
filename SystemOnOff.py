from Common.OutputFormat import return_output
from Common.ConsoleColor import out_back_blue
import time

class SystemWork:

    def __enter__(self):

        self.system_work_time = time.time()
        _output_text = "The system was launched at " + time.ctime()
        print(out_back_blue(return_output(_output_text, "-")))


    def __exit__(self, exc_type, exc_val, exc_tb):
    	
        _output_text = "Shutting down the system"
        print(out_back_blue(return_output("Shutting down the system", "-")))
        print(out_back_blue(return_output(f"Working time: {int(time.time() - self.system_work_time)} sec", "~")))
