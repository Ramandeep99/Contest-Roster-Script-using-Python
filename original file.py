import datetime
import sys
# import os


def return_starting_date(n):
	if n < 10:
		print('ENTER WEEK STARTING FROM 10')
		return
	n-=9
	start_date = datetime.datetime(2021,2,20)

	new_date = start_date + datetime.timedelta(days = n*7)
	return (new_date.strftime('%d/%m')[:5])

# print(return_starting_date(10))


def return_ending_date(n):
	if n < 10:
		print('ENTER WEEK STARTING FROM 10')
		return
	n-=9
	start_date = datetime.datetime(2021,2,20)

	new_date = start_date + datetime.timedelta(days = n*7+6)
	return (new_date.strftime('%d/%m')[:5])

# print(return_ending_date(10))


def contest_date(n):
	if n < 10:
		print('ENTER WEEK STARTING FROM 10')
		return
	n-=9
	start_date = datetime.datetime(2021,2,20)
	new_date = new_date = start_date + datetime.timedelta(days = n*7+2)
	return (new_date.strftime('%d-%m-%y'))
# print(contest_date(10))


def upsolving_date(n):
	if n < 10:
		print('ENTER WEEK STARTING FROM 10')
		return
	n-=9
	start_date = datetime.datetime(2021,2,20)

	new_date = new_date = start_date + datetime.timedelta(days = n*7+6)
	return (new_date.strftime('%d-%m-%y'))
# print(upsolving_date(10))

import csv

def Team_data():
	rows = [['Ankit Riya'],
			['Shubham Ritika'],
			['Chiranjeev Deepak'],
			['Chirag Ramandeep'],
			['Harsh Kanchi'],
			['Chanchal Abhishek'],
			['Tanu Ashish'],
			['Abhay Sukhmanjot'],
			['Arnav Lalit']]

	filename  = 'contest_roster.csv'
	with open(filename , 'w') as f:
		tw = csv.writer(f)

		# tw.writerow(fields)
		tw.writerows(rows)
Team_data()

def first_row():
	fields = ['WEEK' , 'DUTY' , 'DAYS(SAT-FRI)','CONTEST_DATE','UPSOLVING_DATE']
	filename  = 'contest__.csv'
	with open(filename , 'w') as f:
		tw = csv.writer(f)

		tw.writerow(fields)
first_row()


def print_(filename):
	with open (filename , 'r') as f:

		cc = csv.reader(f)
		for i in cc:
			for j in i:
				print(j.ljust(18),end=' ')
			print()
# print_('contest_roster.csv')
# print_('contest__.csv')


def return_team_name(filename):
	rows = [] 

	with open(filename,'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if row: 
				rows.append(row)
		return rows
# print(return_team_name('contest_roster.csv')[0])


def add_team(WEEKno,l ,start_date,contest_date,upsolving_date, filename = 'contest__.csv'):
	row = [WEEKno, *l , start_date,contest_date,upsolving_date]

	with open(filename , 'a+' ) as f:
		tw = csv.writer(f)

		tw.writerow(row)


def main_function(start_week , end_week):

	i,j = start_week,end_week
	k = (i-10)%9
	while i <= j:
		add_team('WEEK ' + str(i) , (return_team_name('contest_roster.csv')[k]) ,  str(return_starting_date(i)) + '-' + str(return_ending_date(i)), str(contest_date(i)) , str(upsolving_date(i)))
		k+=1
		k = k%9
		i+=1

print()
start_week = int(input('Enter_starting_week :'))
print()
end_week = int(input('Enter_ending_week :'))
print()

if start_week <10:
	print('ENTER WEEK STARTING FROM 10')
	quit()
elif end_week < start_week:
	print('ENTER END WEEK GREATER THAN EQUAL TO STARTING WEEK')
	quit()
else:	
	main_function(start_week,end_week)
	print_('contest__.csv')