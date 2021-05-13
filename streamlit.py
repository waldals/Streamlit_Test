import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

"""
# Hello!
You did it :)
"""
def recommend_similar(prodid):
    similarprods = sortedcoocurrences[prodid]
    top5 = similarprods[:5]
    top5 = [(id, idtoname[id][0]) for id, _ in top5]
    print("You may also like:")
    for id, name in top5:
        print(name,id)
    return top5
  
  prodid = input("Enter product_id:")
  
  print(prodid)
