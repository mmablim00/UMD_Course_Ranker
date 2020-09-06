import PlanetTerp
import requests
import json


#written by Murat Ablimit



#param: json_object is the PlanetTerp API grade data that is expressed as json
#return value: a deserialized json object that has been turned into a list of dicts

def json_handler(json_object, indentation = 2):
    #encoded_json is a json formatted python string
    encoded_json = json.dumps(json_object, indent=indentation)

    return json.loads(encoded_json)



# param: data_dict is a dictionary that contains grade data for a single section of a class
# keys in data_dict are letter grades and the associated value is an integer that represents frequency of the letter grade

# return value: an array where the first element is a float that represents an accumulator(sum) of the section's grades
# the second element is the number of students who received a letter grade that can be factored in the overall GPA calculation

# Note: "Other" grades not factored into calculation, "W" grades hold same weight as an "F"
def grade_section(data_dict):
    acc = 0.0
    counter = 0

    #in this for loop, each letter grade is converted to its corresponding GPA quality points out of the 4.0 scale
    for key in data_dict:
        if key == "A+" or key == "A":
            acc += (4.0 * data_dict[key])
            counter += data_dict[key]
        elif key == "A-":
            acc += (3.7 * data_dict[key])
            counter += data_dict[key]
        elif key == "B+":
            acc += (3.3 * data_dict[key])
            counter += data_dict[key]
        elif key == "B":
            acc += (3.0 * data_dict[key])
            counter += data_dict[key]
        elif key == "B-":
            acc += (2.7 * data_dict[key])
            counter += data_dict[key]
        elif key == "C+":
            acc += (2.3 * data_dict[key])
            counter += data_dict[key]
        elif key == "C":
            acc += (2.0 * data_dict[key])
            counter += data_dict[key]
        elif key == "C-":
            acc += (1.7 * data_dict[key])
            counter += data_dict[key]
        elif key == "D+":
            acc += (1.3 * data_dict[key])
            counter += data_dict[key]
        elif key == "D":
            acc += (1.0 * data_dict[key])
            counter += data_dict[key]
        elif key == "D-":
            acc += (0.7 * data_dict[key])
            counter += data_dict[key]
        elif key == "F" or key == "W":
            counter += data_dict[key]
    

    return [acc, counter]


#param: data_list is the deserialized json object that is returned by json_handler
#return value: a float rounded to decimal places that represents the average GPA for the course
# returns -1.0 if the course represented in data_list cannot have its average gpa calculated
def grade_course(data_list):
    acc = 0.0
    num_students = 0
    for section in data_list:
        arr = grade_section(section)
        acc += arr[0]
        num_students += arr[1]
    
    #if either acc is 0.0 or num_students is 0
    #that means the above for loop never ran
    #therefore data_list is invalid
    if acc == 0.0 or num_students == 0:
        return -1.0
    
    return round(acc / num_students, 2)

#param: courses is a list of lists, with each list element containing data for a specific course
#list elements in courses has the following structure: [average gpa, course name, professor name]
def rank_courses(courses):

    courses.sort(reverse = True)

    print("Your courses are ranked as follows:")

    for index, course in enumerate(courses):
        rank = index + 1
        print(f"{rank}.",course[1],"with",course[2],"has an average GPA of",course[0])
    
        



pt = PlanetTerp.PlanetTerp() #see PlanetTerp wrapper class
continue_loop = True
course_db = [] #list used to contain all the courses needed to be ranked

print('\n')
print("This is CourseRanker! CourseRanker is a tool that ranks UMD courses you are taking by their average GPA.")
print("Enter course names and professor names with proper spelling, capitalization, and spacing.\n")


while(continue_loop):

    course_name = input("Enter a course: ")
    prof_name = input("Enter a professor: ")

    average_gpa = grade_course(json_handler(pt.grades(course=course_name, professor=prof_name)))

    #a nonexistent course or professor at UMD will have a -1.0 gpa
    if average_gpa == -1.0:
        print("The course and/or the professor you entered does not exist at UMD, please try again.")
    else:
        course_db.append([average_gpa, course_name, prof_name]) 
    
    prompt = input("Enter \"add\" to add another course or \"rank\" to rank your courses: ")
    print('\n')

    if prompt == "rank":
        continue_loop = False
    else:
        continue


rank_courses(course_db)
