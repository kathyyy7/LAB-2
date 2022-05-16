"""""
# for flowchart
input: the test scores
initiate a iterator (counter) and accumulator (sum) and set it to zero 
loop through the list of test scores
add all the test scores
increment the counter by one
once the loop ends, there are no more scorces to add
divide the accumulator (sum) by counter
display the output to the user
output: print the average of the class scores
"""""

"""""
# pseudocode for the laymen's term interpretation
scores
iterator, accumaltor = 0
loop through scores
    accumaltor = accumulator + scores
    iterator =iterator + 1
output = accumultor / total scores
print output
"""""
# def calculate_average(scores):
#     iterator = 0
#     accumulator = 0
#     student_count = len(scores)
#     print("Length is: ", len(scores))
#     #total = 100 + 80 + 90 + 70 + 50 + 95
#     #print("total: ", total)
#     # while there are more scores:
#     while iterator < len(scores):
#         iterator = iterator + 1
#         # print ("within while loop iterator: ", iterator)
#         print (f"item at index {iterator} is: ", scores[iterator])
#         accumulator = accumulator + scores[iterator]

#     print("sum is: ", accumulator)
#     average = accumulator / student_count
#     print("The average of total scores in the class is: ", average)

# output = calculate_average([50, 0, 100, 80, 90, 70, 50, 95, 60, 90, 50, 100, 70, 90])
# print("The average of total scores in the class is: ", output)



# #do our math


"""""
start
get the numbers of sheets
sheets/ 5
round answer to next number
output the result to the user
end

"""""
import math 
def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer)
    print("sheet is : ", sheet)
    print("the answer is: ", answer)
    print("rounded is: ", math.ceil(rounded))
    print("===================")
    return rounded

output = calculate(16)

print("the return statement is: ", output)



