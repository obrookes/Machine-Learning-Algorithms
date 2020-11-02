File descriptions
Train.zip - the training set, unzip this and you will get the csv file for each station.
test.csv - the test set.
sampleSubmission.csv - a sample submission file in the correct format
Models.zip - linear models pre-trained from other stations.
Data fields
The data contain 4 station features, 8 time features, 7 weather features, 1 task-specific feature and 4 profile features plus 1 target variable. The target variable is 'bikes' and it is a non-negative integer representing the median number of available bikes during the respective hour in the respective rental station. There are 4 features regarding the station:

station - integer from 1 to 275, representing the number of the station, also in the file name
latitude - real number representing geographical latitude of the station
longitude - real number representing geographical longitude of the station
numDocks - positive integer representing the maximal number of bikes that can be present in the station

There are 8 features regarding the timepoint:

timestamp - integer representing the Unix timestamp (seconds since Unix Epoch)
year - integer with 4 digits
month - integer from 1 (January) to 12 (December)
day - integer from 1 to 31
hour - integer from 0 to 23
weekday - string (Monday, Tuesday, ..., Sunday)
weekhour - integer from 1 to 168 representing the hour of the week (Monday 0h is weekhour 1, Sunday 23h is weekhour 168)
isHoliday - 1 (a national or local holiday), 0 (not a holiday)

There are 7 features regarding weather, these do not differ across stations:

windMaxSpeed.m.s
windMeanSpeed.m.s
windDirection.grades
temperature.C
relHumidity.HR
airPressure.mb
precipitation.l.m2

There is one feature regarding the number of bikes in the station 3 hours ago:

bikes_3h_ago
The profile variables are calculated from earlier available timepoints on the same station:

The 'full_profile_bikes' feature is the arithmetic average of the target variable 'bikes' during all past timepoints with the same weekhour, in the same station.
The 'full_profile_3h_diff_bikes' feature is the arithmetic average of the calculated feature 'bikes-bikes_3h_ago' during all past timepoints with the same weekhour, in the same station.
The 'short_*' profile s the same as the full profiles except that it only uses past 4 timepoints with the same weekhour. If there are less than 4 such timepoints then all are used. The missing values are ignored in all profile calculations, i.e. only the timepoints with existing values are averaged.
MODELS
All models are presented in the CSV format. 

For each station there are 6 linear models, all built using R function rlm from the package MASS, with missing value imputation using function na.roughfix from package randomForest. The models use the following features (plus an intercept term):

short: bikes_3h_ago, short_profile_3h_diff_bikes, short_profile_bikes
short_temp: bikes_3h_ago, short_profile_3h_diff_bikes, short_profile_bikes, temperature.C
full: bikes_3h_ago, full_profile_3h_diff_bikes, full_profile_bikes
full_temp: bikes_3h_ago, full_profile_3h_diff_bikes, full_profile_bikes, temperature.C
short_full: bikes_3h_ago, short_profile_3h_diff_bikes, short_profile_bikes, full_profile_3h_diff_bikes, full_profile_bikes
short_full_temp: bikes_3h_ago, short_profile_3h_diff_bikes, short_profile_bikes, full_profile_3h_diff_bikes, full_profile_bikes, temperature.C