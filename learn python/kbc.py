
q = ["1. Who is known as the Father of the Nation in India?\n",
    "2. Which is the largest state in India by area?\n",
    "3. Which planet is known as the Red Planet?\n",
    "4. National animal of india?\n",
    "5. In which year did India gain independence from British rule?\n",
    "6. Which scientist formulated the theory of relativity?\n",
    "7. What is the largest mammal in the world?\n",
    "8. who is India's first prime minister?\n",
    "9. Which famous scientist wrote the book 'A Brief History of Time'?\n",
    "10. What is the currency of Japan?\n",
    "11. Which is the tallest mountain in the world?\n",
    "12. Who invented the telephone?\n",
    "13. Which country won the t-20 World Cup in 2024?\n",
    "14. What is the chemical symbol for water?\n",
    "15. which is the oldest university of India?\n"
    "aa"]

option=[["A. Mahatma Gandhi", "B. Jawaharlal Nehru","C. Subhas Chandra Bose","D. Sardar Vallabhbhai Patel\n"],
        ["A. Maharashtra", "B. Uttar Pradesh", "C. Madhya Pradesh", "D. Rajasthan\n"],
        ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn\n"],
        ["A. Lion" ,"B. Tiger", "C. Elephant", "D. Leopard/n"],
        ["A. 1945", "B. 1947", "C. 1950", "D. 1955/n"],
        ["A. Isaac Newton" , "B. Albert Einstein" , "C. Stephen Hawking" , "D. Galileo Galilei\n"],
        ["A. Elephant" ," B. Blue Whale" , "C. Giraffe" , "D. Hippopotamus\n"],
        ["A. Lal Bahadur Shastri" , "B. Indira Gandhi" , "C. Jawaharlal Nehru" , "D. Rajiv Gandhi\n"],
        ["A. Stephen Hawking" , "B. Albert Einstein" , "C. Carl Sagan" , "D. Richard Dawkins\n"],
        ["A. Yuan" , "B. Yen" , "C. Won" , "D. Rupee\n"],
        ["A. K2 ", "B. Mount Everest" , "C. Kangchenjunga" , "D. Makalu\n"],
        ["A. Alexander Graham Bell" , "B. Thomas Edison" , "C. Nikola Tesla" , "D. Guglielmo Marconi\n"],
        ["A. India" , "B. Australia" , "C. Pakistan" , "D. England\n"],
        ["A. Wo" , "B. H2O" , "C. Wa" , "D. H2\n"],
        ["A. University of Mumbai" ," B. Aligarh Muslim University" , "C. University of Calcutta" , "D. Nalanda University"]]
a=[1,4,2,2,2,2,2,3,1,2,2,1,1,2,4]
level=["0","1000","2000","5000","10000","20000","40000","80000","160000","320000","650000","1200000","2500000","5000000","10000000","70000000"]
print("--------------------------------------------------WELCOME TO THE KAUN BANEGA CROREPATI------------------------------------------------------------\n\n")
print("ENTER THE OPTION IN 1,2,3,4 FOR A,B,C,D RESPECTIVELY OR \"0\" TO QUIT THE GAME")
print()
i=0
money=0
for i in range(len(level)):
    print(f"the question is for rs--:{level[i+1]}")
    print()
    print(q[i])
    print()
    for j in option[i]:
        print(j)    
    c=int(input("enter the ans-: "))
    d=int(c)
    print()
    if(d==a[i]):
       print("correct\n")
       money=int(level[i+1])
       print(f"you won the prize of {level[i+1]}")
       print()
    elif(d!=a[i] and q[i]<q[4]):
       print("incorect!!\n")
       print(f"TOTAL PRIZE MONEY WONIS RS.{level[0]}")
       break
    elif(d!=a[i] and q[i]<q[9]):
       print("incorect!!\n")
       print(f"TOTAL PRIZE MONEY WONIS RS.{level[5]}")
       break
    elif(d!=a[i] and q[i]<q[13]):
       print("incorect!!\n")
       print(f"TOTAL PRIZE MONEY WONIS RS.{level[10]}")
       break
    elif(d!=a[i] and q[i]<=q[14]):
       print("incorect!!\n")
       print(f"TOTAL PRIZE MONEY WONIS RS.{level[14]}")
       break
    elif(d==0):
       print(f"TOTAL PRIZE MONEY WONIS RS.{level[i]}")
       print("incorect!!\n")      
       print()
       break
    elif(d==a[i] and q[i]==q[5],q[10],q[14]):
       print(f"TOTALPRIZE MONEY WON AND SAVED IS{level[i]}")
    elif(q[i]==15 and q[i]==a[i]):
       print("YOU HAVE COMPLETED THE K.B.C.\WON THE GRAND PRIZE OF\"7 CRORE\"")    
    