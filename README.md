# surfs_up
SQLite, SQLAlchemy

## Overview of the analysis: Explain the purpose of this analysis.
SQLite, SQLAlchemy, Pandas, and Python were used to conduct a weather analysis to determine whether a year-round surf shop and ice cream business will be sustainable in Oahu, HI.
Temperature data was pulled for the months of June and December and summary statistics were retrieved to compare.


## Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.
### Deliverable 1 : The Summary Statistics for month June is as follows:

June_df fig: <img width="896" alt="June_temp_df" src="https://user-images.githubusercontent.com/106944351/183472932-7abbca03-6eda-402c-acc4-c36b5af1bd9c.png">

### Deliverable 2 : The Summary Statistics for month December is as follows:

December_df fig: <img width="909" alt="Demeber_temp_df" src="https://user-images.githubusercontent.com/106944351/183472966-1f0864f5-ae20-48c3-8f36-323ec9cb6eb6.png">

- The mean temp of June and December also does not hav much difference.(difference = 3)

- The range of temperatures for December is 27 degrees compared to 21 degrees for June temperatures.

- The maximum temperature of June is 85 and December id 83 degrees. The difference between maximum temperature is 2 degrees. The The difference between minimum temperature of June and December is 
8 degrees.

## Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
According to the temperature analysis, we could say that it would be be favorable to keep the surf and ice cream shop open for complete year.
Just like temperature, we can also find out temperature of other months or we could find out precipitation of June and December as follows:


### Query 1 : 
June_prcp = []
June_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6)
print(June_prcp.all())
June_prcp_df = pd.DataFrame(June_prcp, columns=['date','Precipitation'])
June_prcp_df.describe()

June_prcp_df fig : <img width="198" alt="June_prcp_df" src="https://user-images.githubusercontent.com/106944351/183473027-3612ec09-3192-4926-9425-7467ed06bb97.png">

### Query 2 :  
december_prcp = []
december_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12)
print(december_prcp.all())
december_prcp_df = pd.DataFrame(december_prcp, columns=['date','Precipitation'])
december_prcp_df.describe()

december_prcp_df fig : <img width="322" alt="December_prcp_df" src="https://user-images.githubusercontent.com/106944351/183473058-3d3c44fc-3f2d-4b06-ac00-ffe9c0841f5a.png">
