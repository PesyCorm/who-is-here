import shutil

def return_output(text, fill_sep):

	columns,lines = shutil.get_terminal_size()
	string = "{:{fill}{align}{width}}"
	return string.format(f' {text} ', fill=fill_sep, align='^', width=columns)