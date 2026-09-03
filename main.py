
tasks_list=input("Enter your tasks for today separated by a comma: ").lower()
tasks_list=tasks_list.split(",")
done_Tasks=[]
ongoing_Tasks=[]
for task in tasks_list:
        print(f"\n{task}\n") 
        done =input(f"Did you finish {task} alredy?").lower()
        if done=="yes":
            print("Nice Job")
            print("---------------")
            done_Tasks.append(task)
        else:
            print("Try not to put it off ")
            print("---------------")
            ongoing_Tasks.append(task)
        
progress=input("Do you want to see your today's progress?(yes, no)").lower()
        
if progress=="no":
            input("please hit enter to exit")
        
else:
            print("""
                     ******** Done Tasks ******
            """)
            print(done_Tasks)
            print("""
                     ******* Ongoing Tasks *****
            """)
            print(ongoing_Tasks)
            
            
            
            