question=['Ques 1) What is your name : \n 1. Aviansh 2. Nobita 3. Aliya-Avi 4.Gajju \n',
      'Ques 2) Who is pm of india in current:\n 1.Modi 2. Yogi 3. Amit Shah 4. Rahul Gandhi \n',
      'Ques 3) National Bird Of India:\n 1. Pegion 2. Crow 3. Peacock 4. Cock \n',
      'Ques 4) National Animal of India:\n 1. Monkey 2. Bear 3. Horse 4. Tiger \n']
answer=[1,1,3,4]
amt=[10,20,30,40,50]
c_ans=[]
for ques in(question):
    print(ques)
    ans=int(input("Enter your Answer no(1,2,3,4): "))
    c_ans.append(ans)
    i=0
    if(ans==answer[i]):
        print("Correct Answer :)")
        i=i+1
    else:
        print("Wrong Answer")
        break
# if(c_ans[0]!=1):
#     print("Your Winning amt is: 0")
# else:
print(f"Your winning amt is: {amt[i]}")