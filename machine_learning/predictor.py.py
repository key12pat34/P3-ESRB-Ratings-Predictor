#!/usr/bin/env python
# coding: utf-8

# # Loading Trained Model

# In[1]:


# import sklearn.externals.joblib as extjoblib
import joblib


# In[5]:


# Load the model
loaded_model = joblib.load("joblib_model.pk1")


# # Manual Predictor

# In[6]:


#Game: Same_and_Max:_Save_The_World (Nintendo Switch)
#Result Value should be "T"
print(loaded_model.predict([[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]]))

