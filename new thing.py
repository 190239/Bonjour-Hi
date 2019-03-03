import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yinanjohn1",
    database="database1",
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

print("\nThe following people have the highest science averages out of everybody: \n") 


sciQuery = ("SELECT name, Personal_Science_Average FROM students "
            "WHERE Personal_Science_Average BETWEEN %s and %s")

Personal_Science_Average_start = 95
Personal_Science_Average_end = 100

cursor.execute(sciQuery, (Personal_Science_Average_start, Personal_Science_Average_end))

for (name, Personal_Science_Average) in cursor:
  print("{}, has one of the highest Science Averages with a score of {}". format(name,Personal_Science_Average))

print("\nThe following people have the highest math averages out of everybody: \n") 


mathQuery = ("SELECT name, Personal_Math_Average FROM students "
            "WHERE Personal_Math_Average BETWEEN %s and %s")

Personal_Math_Average_start = 95
Personal_Math_Average_end = 100

cursor.execute(mathQuery, (Personal_Math_Average_start, Personal_Math_Average_end))

for (name, Personal_Math_Average) in cursor:
  print("{}, has one of the highest Math Averages with a score of {}". format(name,Personal_Math_Average))

print("\nThe following people have the highest English averages out of everybody: \n") 


englishQuery = ("SELECT name, Personal_English_Average FROM students "
            "WHERE Personal_English_Average BETWEEN %s and %s")

Personal_English_Average_start = 95
Personal_English_Average_end = 100

cursor.execute(englishQuery, (Personal_English_Average_start, Personal_English_Average_end))

for (name, Personal_English_Average) in cursor:
  print("{}, has one of the highest English Averages with a score of {}". format(name,Personal_English_Average))

print("\nThe following people have the highest History averages out of everybody: \n") 


historyQuery = ("SELECT name, Personal_History_Average FROM students "
            "WHERE Personal_History_Average BETWEEN %s and %s")

Personal_History_Average_start = 95
Personal_History_Average_end = 100

cursor.execute(historyQuery, (Personal_History_Average_start, Personal_History_Average_end))

for (name, Personal_History_Average) in cursor:
  print("{}, has one of the highest History Averages with a score of {}". format(name,Personal_History_Average))


print("\nThe following people have the highest total averages out of everybody: \n") 

totQuery = ("SELECT name, Personal_Cumulative_Grade_Average FROM students "
            "WHERE Personal_History_Average BETWEEN %s and %s")

Personal_Cumulative_Grade_Average_start = 95
Personal_Cumulative_Grade_Average_end = 100

cursor.execute(totQuery, (Personal_Cumulative_Grade_Average_start, Personal_Cumulative_Grade_Average_end))

for (name, Personal_Cumulative_Grade_Average) in cursor:
  print("{}, has one of the highest Total Averages with a score of {}". format(name,Personal_Cumulative_Grade_Average))

print("\n These People are the best students: \n")

bestQuery = ("SELECT Personal_Cumulative_Grade_Average, Class_Cumulative_Grade_Average, School_Cumulative_Grade_Average, Region_Cumulative_Grade_Average, Provincial_Cumulative_Grade_Average"
             " FROM students")

cursor.execute(bestQuery)



best = Personal_Cumulative_Grade_Average * Class_Cumulative_Grade_Average * School_Cumulative_Grade_Average * Region_Cumulative_Grade_Average * Provincial_Cumulative_Grade_Average

ratingQuery = ("SELECT name, best FROM students WHERE best BETWEEN %s and %s")

best_start = best/700000010
best_end = best/700000000

cursor.execute(ratingQuery, (best_start, best_end))

for (name, best) in cursor:
    print("{} has one of the highest student ratings with {}". format(name,best))

cursor.close()
db.close()
