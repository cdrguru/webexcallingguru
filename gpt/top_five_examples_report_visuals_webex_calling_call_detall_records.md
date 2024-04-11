# TOP FIVE EXAMPLES OF REPORTS AND VISUALS FOR WEBEX CALLING CALL DETAIL RECORDS

## Unlocking Actionable Insights from Webex Calling Data

These examples leverage the extensive Webex Calling CDR knowledge to provide more targeted and actionable insights. By incorporating key CDR fields, advanced analytics techniques, and role-specific customization, these examples demonstrate how to extract maximum value from Webex Calling data using Power BI and Python.

### 1. Transforming Webex Calling Analytics with Expo XT

**Query Instructions:**

- Extract key CDR fields like Call ID, Correlation ID, Duration, Start Time, End Time, and Call Type for advanced analytics.
- Calculate average call duration, sentiment scores, and frequency of specific keywords mentioned in calls over a selected period, segmented by Call Type.
- Correlate call metrics with user and department data for deeper insights.

**Power BI Steps:**

- Import the transformed CDR dataset and create relationships with user and department data.
- Use Power Query to create calculated columns for sentiment analysis and keyword detection based on call transcriptions, if available.
- Generate a Sankey diagram illustrating the flow of data from Cisco Webex Calling to Expo XT, emphasizing the analytics processing and data relationships.

**Python Script:**

```python
import pandas as pd

# Load the transformed CDR dataset and related data
cdr_data = pd.read_csv('/mnt/data/transformed_webexcallingcdr.csv')
user_data = pd.read_csv('/mnt/data/user_data.csv')
dept_data = pd.read_csv('/mnt/data/department_data.csv')

# Merge datasets for comprehensive analysis
merged_data = pd.merge(cdr_data, user_data, on='User UUID')
merged_data = pd.merge(merged_data, dept_data, on='Department ID')

# Calculate metrics segmented by Call Type
metrics_by_type = merged_data.groupby(['Call type', 'Department'])['Duration'].agg(['mean', 'count'])
metrics_by_type['Sentiment Score'] = merged_data.groupby(['Call type', 'Department'])['SentimentScore'].mean()
metrics_by_type['Top Keywords'] = merged_data.groupby(['Call type', 'Department'])['KeywordsMentioned'].apply(lambda x: x.value_counts().index[0])

print(metrics_by_type)
```

### 2. Mastering Call Metrics for Strategic Insights

**Query Instructions:**

- Aggregate call volumes by time (day, week, month) and Call Type to identify trends.
- Correlate call volumes with sales performance data, segmented by User Type, to assess impact.
- Analyze call disposition statuses and durations to gauge individual and departmental performance metrics.

**Power BI Steps:**

- Create line graphs with multiple series to visualize call volume trends by Call Type.
- Design clustered bar graphs to compare individual and departmental performance metrics.
- Use stacked area charts to display the distribution of call durations over time, reflecting efficiency.
- Incorporate slicers for interactive filtering by time period, department, and user type.

**Python Script:**

```python
import pandas as pd

# Load the transformed CDR dataset
cdr_data = pd.read_csv('/mnt/data/transformed_webexcallingcdr.csv')

# Aggregate call volumes by day and Call Type
cdr_data['Start time'] = pd.to_datetime(cdr_data['Start time'])
cdr_data['Day'] = cdr_data['Start time'].dt.date
call_volumes = cdr_data.groupby(['Day', 'Call type']).size().unstack()

# Prepare call volumes data for visualization
call_volumes.to_csv('/mnt/data/call_volumes_by_day_type.csv')
```

### 3. Elevating Insights with Precision Analytics

**Query Instructions:**

- Filter out calls marked as test or irrelevant based on specific criteria (e.g., short durations, known test numbers).
- Compare key performance metrics like average duration, sentiment scores, and keyword frequencies before and after applying filters to demonstrate the impact of data accuracy.

**Power BI Steps:**

- Utilize Power Query to apply filters excluding test calls based on multiple criteria.
- Create before-and-after KPI visuals showing the difference in key call metrics with accurate data filtering.
- Add illustrative icons and conditional formatting to emphasize improvements in data quality and reliability.

**Python Script:**

```python
import pandas as pd

# Load the transformed CDR dataset
cdr_data = pd.read_csv('/mnt/data/transformed_webexcallingcdr.csv')

# Filter out irrelevant data based on multiple criteria
relevant_data = cdr_data[(cdr_data['Call type'] != 'Test') & (cdr_data['Duration'] > 10) & (~cdr_data['Calling number'].isin(['1234567890', '9876543210']))]

# Calculate performance metrics before and after filtering
metrics_before = cdr_data.agg({'Duration': 'mean', 'SentimentScore': 'mean', 'KeywordsMentioned': lambda x: x.value_counts().index[0]})
metrics_after = relevant_data.agg({'Duration': 'mean', 'SentimentScore': 'mean', 'KeywordsMentioned': lambda x: x.value_counts().index[0]})

# Prepare data for visualization
filtered_metrics = pd.DataFrame({'Before Filtering': metrics_before, 'After Filtering': metrics_after})

print(filtered_metrics)
```

### 4. Custom Analytics for Varied Team Roles

**Query Instructions:**

- Segment data analysis based on role-specific criteria, leveraging CDR fields like User Type, Department ID, and Call Type.
- Develop customized metrics and KPIs relevant to each role using the CDR dataset and related user/department data.

**Power BI Steps:**

- Design distinct dashboards tailored to sales managers, sales reps, IT personnel, and executives within Power BI.
- Use role-relevant visuals, KPIs, and filters to provide targeted analytics for each dashboard.
- Implement row-level security to ensure users only access data pertinent to their roles.

**Python Script:**

```python
import pandas as pd

# Load the transformed CDR dataset and related data
cdr_data = pd.read_csv('/mnt/data/transformed_webexcallingcdr.csv')
user_data = pd.read_csv('/mnt/data/user_data.csv')
dept_data = pd.read_csv('/mnt/data/department_data.csv')

# Merge datasets for comprehensive analysis
merged_data = pd.merge(cdr_data, user_data, on='User UUID')
merged_data = pd.merge(merged_data, dept_data, on='Department ID')

# Segment analytics based on User Type and Department
role_analytics = merged_data.groupby(['User type', 'Department']).agg({
    'Duration': 'mean',
    'SentimentScore': 'mean',
    'Call type': lambda x: x.value_counts().index[0]
})

# Prepare segmented data for visualization
role_analytics.to_csv('/mnt/data/analytics_by_role.csv')
```

### 5. Transforming Challenges into Growth Opportunities

**Query Instructions:**

- Identify patterns in call abandonment such as time of day, duration before hang-up, caller demographics, and Call Type.
- Link abandonment patterns to potential interventions like staffing optimization, IVR improvements, and targeted callbacks.

**Power BI Steps:**

- Implement a query to analyze call abandonment trends and correlate them with CDR fields for a comprehensive view.
- Design an interactive dashboard with slicers and drill-through to investigate abandonment patterns across various dimensions.
- Create a decision tree visual to map abandonment patterns to recommended interventions and track outcomes.

**Python Script:**

```python
import pandas as pd

# Load the transformed CDR dataset
cdr_data = pd.read_csv('/mnt/data/transformed_webexcallingcdr.csv')

# Identify call abandonment patterns
abandoned_calls = cdr_data[(cdr_data['Call outcome'] == 'Failure') & (cdr_data['Duration'] < 30)]
abandonment_patterns = abandoned_calls.groupby(['Hour', 'Call type']).agg({
    'Duration': 'mean',
    'Calling number': pd.Series.nunique
})

# Prepare abandonment pattern data for visualization
abandonment_patterns.to_csv('/mnt/data/call_abandonment_patterns.csv')
```

## Conclusion

The top five examples presented in this document showcase the immense potential of Webex Calling CDR data for driving business value. By harnessing the power of key data fields, advanced analytics, and customized reporting, organizations can gain deep insights into their communication patterns, customer interactions, and operational efficiency.

Leveraging tools like Power BI and Python, these examples demonstrate how to transform raw CDR data into visually compelling and actionable intelligence. From identifying call abandonment patterns to optimizing staffing based on call volume predictions, the possibilities are endless.

As businesses continue to rely on Webex Calling for their critical communication needs, mastering CDR data analysis will become increasingly essential. By following the best practices and techniques outlined in these examples, organizations can stay ahead of the curve and make data-driven decisions to improve their bottom line.

The future of Webex Calling analytics is bright, and those who embrace the power of CDR data will be well-positioned to succeed in the digital age. By continuously refining and expanding upon these examples, businesses can unlock the full potential of their communication data and drive meaningful results.
