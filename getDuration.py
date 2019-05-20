
def getDuration(num, two_digits=False):
	"""
	num = duration in seconds\n
	two_digits = True, 01hr 03min 09sec\n
	Returns dictionary 
	{
		dur: provided duration,
		hr: hours,
		min: minutes,
		sec: seconds,
		short_msg: 2min 30sec
		long_msg: 0hr 2min 30sec
	}
	"""
	my_dict = None
	if (str(int(num)).isdigit() and num >= 0):
		num = int(num)
		my_dict = {
			'dur': num,
			'hr': 0,
			'min': 0,
			'sec': 0,
			'long_msg': "",
			'short_msg': ""
		}
		
		my_dict['hr'] = num // 3600
		my_dict['min'] = (num % 3600) // 60
		my_dict['sec'] = num % 3600 % 60
		
		for key, val in my_dict.items():
			if(key != 'dur' and str(val).isdigit()):
				if (val < 10 and two_digits):
					val = "0" + str(val)
				if(int(val) > 0):
					my_dict['short_msg'] += f"{val} {key} "
				my_dict['long_msg'] += f"{val} {key} "
		my_dict['short_msg'] = my_dict['short_msg'].strip()
		my_dict['long_msg'] = my_dict['long_msg'].strip()
		my_dict['dur'] = num
		return my_dict
	else:
		print("Please provide a positive number of seconds.")

		
if __name__ == "__main__":
	import sys
	argv_len = len(sys.argv)
	if (argv_len == 2):
		my_dict = getDuration(float(sys.argv[1]))
		print(my_dict)
		
	if (argv_len == 3):
		my_dict = getDuration(float(sys.argv[1]), sys.argv[2])
		print(my_dict)
