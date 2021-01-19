# IA626FinalProject
Isabella Grasso

## Motivation

There are over 500,000 Floridians who are eligible for SNAP benefits but do not use them. A random sample of 20,000 Floridians receiving SNAP benefits where information on ethnicity, county, age, household size, employment status, primary language, education, and gender was collected is explored and compared to trends in the Florida general population. The overarching goal is to understand why eligible Floridians are not taking advantage of these benefits, as well as identify if there are any populations in particular that are underrepresented. For the purpose of this project, race and primary language spoken were explored. 

## Racial Distribution Among Florida SNAP Recipients

First the ethnicity data was visualized in a histogram, showing the frequency of the unique answers for ethnicity on the form. Because this is filled out by hand by recipients, redundant answers such as "caucasion," "caucasian," and "white," for example, needed to be cleaned. This was true of other race/ethnicity responses as well. Answers of “white,” “caucasion,” “Hispanic-white,” and “caucasian” were all categorized as “White.” Answers of “black,” “Hispanic-black,” and “African American” were categorized as “Black/African American”. “Asian” and “asian” were categorized as “Asian.” “Native American” and “Native American and Native Alaskan” were categorized as “Native American/Native Alaskan.” Assumptions were made to match the categories provided in US census data https://www.infoplease.com/us/census/florida/demographic-statistics

## Racial Distribution Among Greater Population of Florida

The US Census API was used to gather data from 2018. They utilized the following code system:
      "11": "Native Hawaiian and Other Pacific Islander alone or in combination",
      "10": "Asian alone or in combination",
      "9": "American Indian and Alaska Native alone or in combination",
      "8": "Black alone or in combination",
      "7": "White alone or in combination",
      "6": "Two or more races",
      "5": "Native Hawaiian and Other Pacific Islander alone",
      "4": "Asian alone",
      "3": "American Indian and Alaska Native alone",
      "2": "Black alone",
      "1": "White alone",
      "0": "All races"
Codes 0 and 6 were recoded as "Other". Codes 2 and 8 were recoded as "Black/African American". Codes 1 and 7 were recoded as "White". Codes 3 and 9 were recoded as "Native American/Alaskan Native". Codes 4 and 10 were recoded as "Asian". Codes 5 and 11 were recoded as "Native Hawaiian/Pacific Islander". 

|Race|Percent of SNAP Pop| Percent of FL Pop|
|----|---------|-----------|
|White| 58.2% | 51.8%|
|Black/African American|19.9%|11.6%|
|Asian|5.84%|2.2%|
|Native American/Alaskan Native|10.1%|0.5%|
|Native Hawaiian/Pacific Islander|3.09%|0.13%|
|Other|2.85%|33.8%|

## Primary Language Spoken Among Florida SNAP Recipients
The three options for primary language among Florida SNAP recipients were English, Spanish, and Other. The website is offered in both English and Spanish. 

## Primary Language Spoken Among Greater Population of Florida
To access this information wikipedia was scraped from this URL: https://en.wikipedia.org/wiki/Demographics_of_Florida#Languages. The page contained a mixture of tables, text, and images, and first all of the contents of the page were scraped. This was saved into a text file to avoid multiple requests which was then loaded by another script. First the table containing the relevant information was isolated using the title of the table, "Top Languages in Florida." The data was further divided to scrap unnecessary information after the end of the table. Beautiful soup was then utilized to extract the information from the table. Any languages other than English or Spanish were aggregated into the category Other. 

|Primary Language|Percent of SNAP Pop|Percent of FL Pop|
|----------------|---------|------|
|English|85%|73.4%|
|Spanish|11.9%|19.5%|
|Other|3.1%|4.41%|


## Visualization & Analysis

All of the above data was stored into CSV files which were then loaded into R for visualization. GGPlot was utilized. To prepare the data for visualization any data that represented frequency was transformed to represent percentage of the total data. Then the distribution of the SNAP data was compared to the distribution of the census/wikipedia data of the greater Florida population to see if there are any over or under populated groups.


![alt text](https://github.com/igrasso/IA626FinalProject/blob/main/rep_by_race.png)
*Figure 1: Representation by Race of FL SNAP recipients. The vertical black line lies at x = 1. This would indicate a proportionate representation of SNAP recipients to the greater population of Floridians.* 

**Add in analysis here** Most likely Chi quared goodness of fit test with post hoc analysis using bonferroni adjustment. 

![alt text](https://github.com/igrasso/IA626FinalProject/blob/main/rep_by_lang.png)
*Figure 2: Representation by Language of FL SNAP recipients. The vertical black line lies at x = 1. This would indicate a proportionate representation of SNAP recipients to the greater population of FLoridians.*

**Add in analysis here** Most likely test for proportion for each language as frequency data is unavailable from wikipedia. 
