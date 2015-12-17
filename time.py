from datetime import datetime

class Employee(object):
	

	def __init__(self, name, emp_id):
		self.name = name
		self.emp_id = emp_id
		self.signed_in = False
		
		f = open ("time_sheet.csv", "r")
		for line in f.readlines():
			line_list = line.split(',')
			if line_list[0] == str(self.emp_id):
				self.signed_in = (line_list[1] == 'signed-in at: ')
		if not self.signed_in:
			self.signed_in = False

	def action (self):
		
		time_sheet = []

		time_inp = raw_input("Please type 1 to sign-in or 2 to sign-out ")
		if time_inp == '1' and self.signed_in == False:
			sign_in_time = str(datetime.now()) [:-7]
			self.signed_in == True
			print "You have signed-in at ", sign_in_time

			if not sign_in_time in time_sheet:
				time_sheet.append(str(self.emp_id))
				time_sheet.append("signed-in at: ")
				time_sheet.append(str(sign_in_time))

			
		elif time_inp == '2' and self.signed_in == True:
			sign_out_time = str(datetime.now()) [:-7]
			self.signed_in == False
			print "You have signed-out at ", sign_out_time

			if not sign_out_time in time_sheet:
				time_sheet.append(str(self.emp_id))
				time_sheet.append("signed-out at: ")
				time_sheet.append(str(sign_out_time))

		else:
			print "Wrong input. Please select a correct action"

		f = open ("time_sheet.csv", "a")
		f.write(",".join(time_sheet) + '\n')
		f.close()


def verify(emp_id):
	emp_list = open("emp_list.csv") #look up the id in the file
	emp_list = emp_list.readlines()
	new_list = []
	for entry in emp_list[1:]:
		new_list.append(int(entry.split(',')[1].strip()))
	return emp_id in new_list



def get_name(emp_id):
	f = open("emp_list.csv", 'r')
	for line in f.readlines():
		line_list = line.split(',')
		if str(emp_id) in line_list[1]:
			name = line_list[0]
			return name


while True:
	emp_id = raw_input("Please enter your id or type exit: ")
	if emp_id == 'exit':
		print "Good bye"
		break
	emp_id = int(emp_id)
	if verify(emp_id):
		print "Your id has been confirmed ", get_name(emp_id)
		
		employee = Employee(get_name(emp_id), emp_id)
		employee.action()
		















