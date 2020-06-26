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

print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])