#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""
To calculate if the student has completed the target he has set earlier by using input function
and then use the input data to compare it with the actual studied time in total for a week
We assume that the student invetsed time on all seven days of week
"""

print('Hi There!!! Learner\n')
hrs_target_week_total = input('Please enter the target you have set for your self in total for the whole week: ')
print('\n')
hrs_sun = input('Please enter the hours you studied on Sunday: ')
hrs_mon = input('Please enter the hours you studied on Monday: ')
hrs_tue = input('Please enter the hours you studied on Tuesday: ')
hrs_wed = input('Please enter the hours you studied on Wednesday: ')
hrs_thu = input('Please enter the hours you studied on Thursday: ')
hrs_fri = input('Please enter the hours you studied on Friday: ')
hrs_sat = input('Please enter the hours you studied on Saturday: ')
hrs_target_week_total = float(hrs_target_week_total)
hrs_sun = float(hrs_sun)
hrs_mon = float(hrs_mon)
hrs_tue = float(hrs_tue)
hrs_wed = float(hrs_wed)
hrs_thu = float(hrs_thu)
hrs_fri = float(hrs_fri)
hrs_sat = float(hrs_sat)
print('\n')
hrs_day = [hrs_sun, hrs_mon, hrs_tue, hrs_wed, hrs_thu, hrs_fri, hrs_sat]
hrs_studied_total = hrs_sun + hrs_mon + hrs_tue + hrs_wed + hrs_thu + hrs_fri + hrs_sat
hrs_studied_total = float(hrs_studied_total)
avg_target = hrs_target_week_total/7

if hrs_studied_total >= hrs_target_week_total:
    print('Kudos to you! you have already blown away the limit you have set for yourself')
else:
    for i in range(len(hrs_day)):
        if hrs_day[i] < avg_target:
            print('Little more effort can be made next week on '+ str(i+1) +'th day')
        else:
            continue

