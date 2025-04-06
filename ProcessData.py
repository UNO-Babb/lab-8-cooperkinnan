#ProcessData.py
#Name:Cooper Kinnan
#Date:4/6/2025
#Assignment:Lab 8


def main():
    # Open the files we will be using
    inFile = open("names.dat", 'r')
    outFile = open("StudentList.csv", 'w')
    
    
    outFile.write("Last Name,First Name,UserID,Major-Year\n")
    
    
    for line in inFile:
        data = line.strip().split()  
        first_name = data[0]
        last_name = data[1]
        student_id = data[3][-3:]  
        major = data[6][:3].upper()  
        year_mapping = {"Freshman": "FR", "Sophomore": "SO", "Junior": "JR", "Senior": "SR"}
        year_abbr = year_mapping.get(data[5], "Unknown")  

     
        if len(last_name) < 5:
            user_id = f"{first_name[0]}{last_name}X{student_id}"
        else:
            user_id = f"{first_name[0]}{last_name}{student_id}"

        
        major_year = f"{major}-{year_abbr}"

       
        outFile.write(f"{last_name},{first_name},{user_id},{major_year}\n")
    
    
    inFile.close()
    outFile.close()

if __name__ == '__main__':
    main()

