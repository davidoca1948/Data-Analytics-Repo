name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000" 

print(name_1.lower())
print(name_2.lower()) 
print(name_3.lower()) 

print(name_1.title()) 
print(name_2.title()) 
print(name_3.title()) 

salary_1_cleaned = salary_1.replace('$', '')
print(salary_1_cleaned, type(salary_1_cleaned)) 
salary_2_cleaned = salary_2.replace('$', '')
print(salary_2_cleaned, type(salary_2_cleaned)) 

salary_1_math = int(salary_1.replace('$', '').replace(',', ''))
print(salary_1_math, type(salary_1_math)) 