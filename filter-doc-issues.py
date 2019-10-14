import pandas as pd
import csv

zendesk_df = pd.read_csv('zendesk_data.csv', index_col='URL')
read_filtered_df = pd.read_csv('filtered_issues.csv', names =['Url','Description'])

filtered_df = pd.DataFrame(read_filtered_df)
filtered_url = filtered_df['Url']

##################################################

#Create the keyword list.
keywords = ['api-sandbox', 'docs', 'documentation', 'api', 'crud']
#Create a dictionary to store the data that is filtered using the keywords.
keyword_dict = {}

#pass the data in your csv to a panda datafram, and only get the Description and URl columns.
df = pd.DataFrame(zendesk_df, columns = ['DESCRIPTION','URL'])
#It is easier to filter out content when all the test are in lowercase. Therefore, make sure the description column is in lowercase.
df_lower = df['DESCRIPTION'].str.lower()

#Filter out the rows where the description has any of the keywords.
for index, desc in df_lower.items():
    for keyword in keywords:
        if keyword in desc:
            if index not in filtered_url:
                #Write the data to the dictionary you created above.
                keyword_dict[index] = desc
                # Pass the dictionary data to a datafram so you can write into a new CSV file.
                filtered_list = pd.DataFrame.from_dict(keyword_dict, orient='index', columns=['Description'])
                filtered_list.to_csv(path_or_buf="filtered_issues.csv")
            break
