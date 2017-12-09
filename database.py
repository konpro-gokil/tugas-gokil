# function action
def action(kondisi):
	if (kondisi=="lapar"):
		result = "harus makan"
	else:
		result = "jangan makan"
	return result
		
# function program
result = action ("lapar")
print(result)