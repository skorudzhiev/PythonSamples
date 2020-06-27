import unicodecsv

enrollments_filename = 'C:\Temp\PythonSamples\csv\\resources\enrollments.csv'
daily_engagement_filename = 'C:\Temp\PythonSamples\csv\\resources\daily_engagement.csv'
project_submissions_filename = 'C:\Temp\PythonSamples\csv\\resources\project_submissions.csv'

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv(enrollments_filename)
daily_engagement = read_csv(daily_engagement_filename)
project_submissions = read_csv(project_submissions_filename)

## Find the total number of rows and the number of unique students (account keys)
## in each table.

enrollment_num_rows = sum(1 for row in enrollments_filename)
daily_engagement_num_rows = sum(1 for row in daily_engagement_filename)
project_submissions_num_rows = sum(1 for row in project_submissions_filename)

len(enrollments)
len(daily_engagement)
len(project_submissions)

# The number of students enrolled
unique_enrolled_students = set()
for enrolled in enrollments:
    unique_enrolled_students.add(enrolled['account_key'])
len(unique_enrolled_students)

# The number of unique students engagement 
unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct'])
len(unique_engagement_students)

# The number of unique project submissions
unique_project_submissions = set()
for submission in project_submissions:
    unique_project_submissions.add(submission['account_key'])
len(unique_project_submissions)

print(len(unique_engagement_students))