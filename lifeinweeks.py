#this script is use to calculate total weeks left in one's life if they live up to 90 years

age = input()

#converting input into integer and calculation of age left below
age_left = 90 - int(age)

age_in_weeks = age_left * 52

print(f"You have {age_in_weeks} weeks left.")