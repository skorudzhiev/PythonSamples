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

for engagement_record in daily_engagement:
    # For each row we create an account key and set it to the existing value
    engagement_record['account_key'] = engagement_record['acct']
    # Once the value has been copied we delete the acct from the dictionary
    del[engagement_record['acct']]
