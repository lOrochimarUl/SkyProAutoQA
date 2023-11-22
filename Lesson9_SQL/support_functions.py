

class Support:
        
    def clear_id(id: str):
        f = filter(str.isdecimal, id)
        s1 = "".join(f)
        return s1
                