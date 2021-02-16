class Desktop:

	def dir_01(self):
		return "files in dir_01"

	def dir_02(self):
		return "files in dir_02"

	def dir_03(self):
		return "files in dir_03"

desktop_directory = {"dir_01": Desktop().dir_01(), "dir_02": Desktop().dir_02(), "dir_03": Desktop().dir_03()}

while True:
	
	request = input("--")

	if "cd" in request:
		try:
			split_request = request.split(" ")
			if len(split_request) == 2:
				try:
					response = desktop_directory[split_request[1]]
					print("\n>>", response, "\n")

				except:
					print("directory not found. try again or enter 'help'")

			else:
				print("directory not found. try again or enter 'help'")
		except:
			print("directory not found. try again or enter 'help'")

		

	elif "help" in request:
		print("""
>>help - enter "help" to see tips
>>cd [requested directory] - to view directory contents
			""")
	elif "quit" in request:
		break
	else:
		print("unexpected request. try again or enter 'help'")