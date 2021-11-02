# Final Project - KICKSTARTER

![picture](kickstarter.png)

Kickstarter is a funding platform for creative projects. Everything from film, games, and music to art, design, and technology. Kickstarter is full of ambitious, innovative, and imaginative projects that are brought to life through the direct support of others.

Every project creator sets their project's funding goal and deadline. If people like the project, they can pledge money to make it happen. If the project succeeds in reaching its funding goal, all backers' credit cards are charged when time expires. Funding on Kickstarter is all-or-nothing. If the project falls short of its funding goal, no one is charged.

## Objective

The goal  is to be able to predict whether or not a project will receive it's goal funds.

## Data

describe data etc.

### Data Source

The data has been extracted via apify downloads from kickstarter.

### Shape of the Data

The dataframe consits of xxx rows × 47 columns. Here are some of the most important ones used for this analysis and model:

| Column name | Description |
| ----------- | ----------- |
| backers_count | count of people backing the project |
| blurb | short description of the project |
| categoryId | categoryId |
| categoryName | name of category |
| categroySlug | name of subcategory |
| converted_pledged_amount | amount of money pledged |
| country | country |
| country_displayable_name | country full name |
| created_at | timestamp of when the project was created |
| created_at_formatted | formatted created |
| currency | e |
| currency_symbol | e |
| currency_trailing_code | e |
| current_currency | e |
| deadline | e |
| description | e |
| disable_communication | e |
| fx_rate | e |
| goal | goal amount |
| id | project id |
| is_starrable | e |
| launched_at | timestamp of when the project was launched |
| launched_at_formatted | e |
| link | e |
| locationId | e |
| locationName | e |
| name | e |
| photo | e |
| pledged | e |
| pubDate | e |
| slug | e |
| spotlight | e |
| staff_pick | e |
| state | state of project either live or successful |
| state_changed_at | e |
| static_usd_rate | e |
| title | e |
| url | e |
| usd_exchange_rate | e |
| usd_pledged | e |
| usd_type | e |

### Workflow

#### Load, First Review and Clean


#### Deep Dive Python


#### Deep Dive Tableau


#### EDA


## Python Libraries
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [scipy](https://www.scipy.org/)
- [sklearn](https://scikit-learn.org/stable/)

### Libraries use for NLP
- [textblob](https://textblob.readthedocs.io/en/dev/)
- [yake](https://pypi.org/project/yake/)
