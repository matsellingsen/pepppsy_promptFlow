from promptflow import tool
import pandas as pd
import azureml.fsspec


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


#for e in examples_pd:
 #    print(e)
#First 8 labeled notes are provided here, as examples for the LLM.

@tool
def prepare_examples(example_size):
    columns = ["English US revised (deepl translator)", "English US"]
    examples_pd = pd.read_excel("azureml://subscriptions/4a40333d-da0e-4cdb-8711-92dc11a1d1bd/resourcegroups/matsel-rg/workspaces/pepppsy/datastores/workspaceblobstore/paths/UI/2024-08-29_124003_UTC/Translated_Comments.xls", usecols=columns)
    prepared_examples = []
    for row in examples_pd.index[:example_size]:
        prepared_examples.append({"text_converted": examples_pd["English US revised (deepl translator)"][row],
                                    "text": examples_pd["English US"][row]     
        })
    return prepared_examples


