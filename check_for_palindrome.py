'''
Daily Interview Pro
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, determine if there is a way to arrange the string such that the string is a palindrome. 
If such arrangement exists, return a palindrome (There could be many arrangements).
Otherwise return None.
'''



def find_palindrome(s):
	return True if s == s[::-1] else False

print(find_palindrome('momom'))
# momom
	
	
	

