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

## Find any one student enrollments where the student is missing from the daily engagement table.
## Output that enrollment.

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        print(enrollment) 
        break


## Find the number of surprising data points (enrollments missing from
## the engagement table) that remain, if any.

num_problem_students = 0

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students \
        and enrollment['join_date'] != enrollment['cancel_date']:
        num_problem_students += 1

num_problem_students


# Create a set of the account keys for all Udacity test accounts
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)

# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

# Remove Udacity test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print(len(non_udacity_enrollments))
print(len(non_udacity_engagement))
print(len(non_udacity_submissions))