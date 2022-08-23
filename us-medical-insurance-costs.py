#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# ## What questions will we answer in this project?

# In this project, we will be using a U.S. Medical Insurance dataset to answer the following questions:
# 1. How many patients are there by age group?
# 2. What is the average age of the patients in the dataset?
# 3. Where are a majority of the individuals from?
# 4. How do average costs differ between smokers vs. non-smokers?
# 5. What is the average age for someone who has at least one child in this dataset?

# ## Import csv and pandas

# We begin by importing the modules csv and pandas.

# In[1]:


import csv


# In[2]:


import pandas as pd


# ## Read csv into DataFrame

# Next, we read the csv data into a pandas DataFrame.

# In[3]:


df= pd.read_csv('insurance.csv')


# ## Show the first five rows of data

# Using, df.head(), we can inspect the first five rows of data to get an idea of what we're working with.

# In[37]:


print("The first five rows of data:\n")
print(df.head())


# ## How many patients are there by age group?

# To determine how many patients there are by age group, we begin by creating a list of ages and indices.  
# Then, we organize this data into a dictionary with the indices as keys, and the ages as values.

# In[5]:


ages= df['age'].tolist()


# In[7]:


indices= [i for i in range(len(df))]


# In[8]:


age_by_index= {}
for index in indices:
    age_by_index[index]= ages[index]


# Next, we write a function to iterate through the dict keys and total up the number of patients by age group.

# In[34]:


def get_patients_by_age_group(): 
    zero_to_one= 0
    two_to_four= 0
    five_to_twelve= 0
    thirteen_to_nineteen= 0
    twenty_to_thirtynine= 0
    forty_to_fiftynine= 0
    sixty_plus= 0

    for age in ages:
        if age <= 1:
            zero_to_one+= 1
        elif age <= 4:
            two_to_four+= 1
        elif age <= 12:
            five_to_twelve+= 1
        elif age <= 19:
            thirteen_to_nineteen+= 1
        elif age <= 39:
            twenty_to_thirtynine+= 1
        elif age <= 59:
            forty_to_fiftynine+= 1
        else:
            sixty_plus+= 1
    
    summary_string=\
        "Patients by age group:\n\
        0-1: {zero_to_one}\n\
        2-4: {two_to_four}\n\
        5-12: {five_to_twelve}\n\
        13-19: {thirteen_to_nineteen}\n\
        20-39: {twenty_to_thirtynine}\n\
        40-59: {forty_to_fiftynine}\n\
        60+: {sixty_plus}\
        ".format(zero_to_one=zero_to_one,\
                 two_to_four=two_to_four,\
                 five_to_twelve=five_to_twelve,\
                 thirteen_to_nineteen=thirteen_to_nineteen,\
                 twenty_to_thirtynine=twenty_to_thirtynine,\
                 forty_to_fiftynine=forty_to_fiftynine,\
                 sixty_plus=sixty_plus)
    return summary_string


# ### Patients by age group:

# Finally, we print out the result.

# In[35]:


print(get_patients_by_age_group())


# ## What is the average age of the patients in the dataset?

# To answer this question, we write a function determine the average patient age.

# In[11]:


def find_average_age():
    sum_of_ages= 0
    num_of_ages= len(ages)
    for age in ages:
        sum_of_ages+= age
    average_age= sum_of_ages / num_of_ages
    return "{:.2f}".format(average_age)


# ### The average patient age is:

# In[33]:


average_age= find_average_age()
print("The average patient age is {} years.".format(average_age))


# ## Where are the majority of individuals from?

# First, we create a list of the each region in the dataset, keeping duplicates.

# In[40]:


regions= df['region'].tolist()


# To determine which region has the majority of patients, we first initialize each region to 0.  
# Then we iterate though the list of regions and total up the number of times each region appears.

# In[41]:


def find_majority_region():
    patients_by_region= {
        'northwest': 0,
        'northeast': 0,
        'southeast': 0,
        'southwest': 0
    }
    for region in regions:
        if region == 'northwest':
            patients_by_region['northwest']+= 1
        elif region == 'northeast':
            patients_by_region['northeast']+= 1
        elif region == 'southeast':
            patients_by_region['southeast']+= 1
        else:
            patients_by_region['southwest']+= 1
    
    majority_region= 'northwest'
    for key in patients_by_region.keys():
        if patients_by_region[key] > patients_by_region[majority_region]:
            majority_region= key
    return majority_region, patients_by_region[majority_region]
    


# ### The majority of patients are from:

# In[38]:


majority_region, num_patients= find_majority_region()
print("The majority of patients ({num_patients}) are from the {majority_region}."\
      .format(num_patients=num_patients, majority_region=majority_region))


# ## How do costs differ between smokers vs. non-smokers?

# First, we create two lists, one of the smoker data, and another of the patient charges.

# In[15]:


smokers= df['smoker'].tolist()
charges= df['charges'].tolist()
smoker_and_charges_by_index= {}
for index in indices:
    smoker_and_charges_by_index[index]= {'smoker': smokers[index], 
                                      'charges': charges[index]}


# Next, we find the total number of smokers and non-smokers.

# In[16]:


# find the average cost for smokers vs. non-smokers
# first, find the total number of smokers and non-smokers
num_smokers= 0
num_nonsmokers= 0
for patient in smokers:
    if patient == 'yes':
        num_smokers+= 1
    elif patient == 'no':
        num_nonsmokers+= 1


# We then find the total charges for smokers and for non-smokers.

# In[17]:


smokers_charges= 0
nonsmokers_charges= 0

for key in smoker_and_charges_by_index.keys():
    if smoker_and_charges_by_index[key]['smoker'] == 'yes':
        smokers_charges+= smoker_and_charges_by_index[key]['charges']
    elif smoker_and_charges_by_index[key]['smoker'] == 'no':
        nonsmokers_charges+= smoker_and_charges_by_index[key]['charges']


# To find the average charges, we divide the smokers' charges by the number of smokers, and similarly for the non-smokers.

# In[18]:


# divide total smokers' charges by number of smokers
average_charge_smoker= "{:.2f}".format(smokers_charges / num_smokers)
# divide total non-smokers' charges by number of non-smokers
average_charge_nonsmoker= "{:.2f}".format(nonsmokers_charges / num_nonsmokers)


# ### Average charges for smokers vs. non-smokers:

# In[27]:


print("The average charge for a smoker is ${}".format(average_charge_smoker))


# In[26]:


print("The average charge for a non-smoker is ${}".format(average_charge_nonsmoker))


# ### How many times more are smokers charged than non-smokers?

# In[39]:


how_many_times_more= "{:.2f}".format(float(average_charge_smoker) / float(average_charge_nonsmoker))
print("The average smoker is charged {} times more than the average non-smoker.".format(how_many_times_more))


# ## What is the average age for someone who has at least one child in this dataset?

# In a similar approach to answering the previous questions, we start off by creating a list of the children column data.  
# Then, we create a dictionary that stores age and children by index.

# In[22]:


num_children= df['children'].tolist()

age_and_children_by_index= {}
for index in indices:
    age_and_children_by_index[index]= {
        'age': ages[index],
        'children': num_children[index]
    }


# We now determine the total number of patients with children, as well as the sum of their ages.

# In[23]:


num_childhavers= 0
childhaver_ages= 0
for key in age_and_children_by_index.keys():
    if age_and_children_by_index[key]['children'] >= 1:
        num_childhavers+= 1
        childhaver_ages+= age_and_children_by_index[key]['age']


# Lastly, we determine the average age.

# In[24]:


# divide sum of ages of patients with children by the total number of patients with children
average_age_of_childhaver= "{:.2f}".format(childhaver_ages / num_childhavers)


# ### The average age of a person with at least one child is:

# In[25]:


print("The average age of a person with at least one child in the dataset is {} years.".format(average_age_of_childhaver))

