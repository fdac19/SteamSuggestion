#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame


# In[2]:



def load_data():
    data=pd.read_csv("steam.csv", names=['appid', 'name', 'release_date', 'english', 'developer', 'publisher', 'platforms', 'required_age', 'categories', 'genres', 'steamspy_tags', 'achievements', 'positive_ratings', 'negative_ratings', 'average_playtime', 'median_playtime', 'owners', 'price'])
    data=data.drop(columns=['appid', 'english'])
    data=data.drop(data.index[0])
    #data['release_date'] = data['release_date'].str[:4]
    #print(data['release_date'])
    return data


# In[3]:


def u_input():
    return


# In[4]:


def filter_plat(data, key):

    plat_filter= data[data['platforms'].str.contains(key)]
    return plat_filter
    


# In[5]:


def publish(data, key):
    #print(plat['publisher'].value_counts()[:5].index.tolist())
    publish_filter= data[data['publisher'].str.contains(key)]

    
    return publish_filter


# In[6]:


def genre(data,key):
    #print(data.genres.unique())
    cat_filter= data[data['genres'].str.contains(key)]
    
    return cat_filter


# In[7]:


def req_age(data, key): #[0,3,7,12,16, 18]
    #print(data.required_age.unique())
    age_filter= data[data['required_age'].str.contains(key)]

    return age_filter


# In[8]:


def year_filter(data,key):
    #print(data.release_date.unique())
    year= data[data['release_date'].str.contains(key)]

    return year


# In[9]:


'''def tag_filter(data,key):
    #print(data.steamspy_tags.unique())
    tag= data[data['steamspy_tags'].str.contains(key)]
    return tag
'''
    


# In[31]:


def sorting(data, key):
    if(key==0):
        final=data.sort_values(by='positive_ratings', ascending=False)
        #print(data)
        print(final['positive_ratings'])
    
    if(key==1):
        final=data.sort_values(by='average_playtime', ascending=False)
        print(final['average_playtime'])
    if(key==2):
        final=data.sort_values(by='price', ascending=False)
        print(final['price'])
    return final
    


# In[33]:


def run(key):
    data=load_data()
    #print(data.head())
    #key= u_input()
    #key=['windows','','','',2]
    plat=data
    if(key[0]!=''):
        plat=filter_plat(data, key[0])
    cat=plat
    if(key[1]!=''):
        cat= genre(plat, key[1])
    #print(cat['name'])
    year=cat
    if(key[2]!=''):
        year= year_filter(cat,key[2] ) 
    #print(year['name'])
    
    r_age=year
    if(key[3]!=''):
        r_age=req_age(year, key[3])
    
    #print(r_age['name'])
    sort=sorting(r_age, key[4])
    
        
    final=sort['name'].head(20).tolist()
    #print(final)
        
    return final


# In[ ]:





# In[ ]:





# In[ ]:




