# count of words

def word_count() :
    my_input = input("Please , enter a sentence!")
    marks = [":", ";" , "," , "-" , "!" , "." , "'" , '"' , "(" , ")"]
    m = my_input
    for mark in marks: 
        m = m.replace(mark , " ")
    m = m.lower()
    m = m.split()
    word_dict = {}
    for item in m :
        if item not in word_dict.keys() :
            word_dict[item] = 1
        else :
            word_dict[item] += 1
    sorted_dict = sorted(word_dict.items())
    

    for word, count in sorted_dict:
        print(f"\nword: " , word)
        print(f"count:" , count)


word_count()





        

    


            










  
    
