import subprocess

print("This will override a previous output file named in a similar convention - see code for more details")#go to where output string is concatinated into big_string or look for ':D'

big_string = "pdfunite"
prefix = input("prefix:")
first = int(input("first number(inclusive):"))
second = int(input("second number(inclusive):"))#we add one to this in the for loop

for i in range(first, second+1):
	big_string += " "+prefix+str(i)+".pdf"
big_string += " output"+prefix+str(first)+"-"+prefix+str(second)+".pdf"# :D
process = subprocess.Popen(big_string.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
