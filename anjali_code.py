def validate(data, template, path=""):
    if type(template) == dict:
        for key, template_value in template.items():
            full_path = path + "." + key if path != "" else key
            
            if key not in data:
                return False, f"mismatched keys: {full_path}"
            
            result, error = validate(data[key], template_value, full_path)
            if result == False:
                return result, error
        
        for key in data:
            if key not in template:
                full_path = path + "." + key if path != "" else key
                return False, f"mismatched keys: {full_path}"
    
    elif not isinstance(data, template):
        return False, f"bad type: {path}"
    
    return True, "" 
