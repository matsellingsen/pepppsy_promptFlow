from promptflow import tool
import pandas as pd

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def prepare_text_for_conversion(num, tekst):
    columns = ["English US"]
    examples_pd = pd.read_excel("azureml://subscriptions/4a40333d-da0e-4cdb-8711-92dc11a1d1bd/resourcegroups/matsel-rg/workspaces/pepppsy/datastores/workspaceblobstore/paths/UI/2024-08-29_124003_UTC/Translated_Comments.xls", usecols=columns)
    text = examples_pd.iloc[num][0]
   # return text 
    return tekst 