import json 
def main(input_data,role,region): 
    try: 
        #json_payload = json.loads(json_payload) 
        input_from_user = input_data.get("query") 
        print(input_from_user) 
        return {"message": "Processed query", "user query from main function": input_from_user} 
    except Exception as e: print(e)