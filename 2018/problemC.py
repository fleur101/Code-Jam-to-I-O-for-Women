f = open('C-large-practice.in', 'r')
T = int(f.readline())
out = open("output.txt", "w");

for j in range (T):
    N=int(f.readline())
    names = f.readline().split(" ");
    name1 = names[0];
    name2 = names[1];
    name3 = names[2];
    i = 0;
    while i < N:
        if (name1[i] == name2[i] and name2[i] == name3[i] and name1[i] == name3[i]):
            i+=1;
            continue;
        else:
            break;
    if i == N or (name1[i] != name2[i] and name2[i] != name3[i] and name1[i] != name3[i]):
        ans1 = "YES";
        ans2 = "YES";
        ans3 = "YES";
    else:
        print(name1[i] + name2[i]+name3[i])
        if (name1[i] == name2[i]):
            letter1 = name3[i];
            letter2 = name1[i];
            ans3 = "NO";
            i = i+1;
            while i<N:
                if (name1[i] == name2[i]):
                    i = i+1;
                    continue;
                else:
                    break;
            if i == N:
                ans1 = "YES";
                ans2 = "YES";
            elif (name1[i] == letter1 and name2[i]==letter2):
                ans1 = "YES";
                ans2 = "NO";
            elif (name1[i] == letter2 and name2[i]==letter1):
                ans1 = "NO";
                ans2 = "YES";
            else:
                ans1 = "YES";
                ans2 = "YES";
        elif (name1[i] == name3[i]):
            letter1 = name2[i];
            letter2 = name1[i];
            ans2 = "NO";
            print("letter1 "+letter1);
            print("letter2 "+letter2);
            i = i+1;
            while i<N:
                if (name1[i] == name3[i]):
                    i = i+1;
                    continue;
                else:
                    break;
            if i == N:
                ans1 = "YES";
                ans3 = "YES";
            elif (name1[i] == letter1 and name3[i]==letter2):
                ans1 = "YES";
                ans3 = "NO";
            elif (name1[i] == letter2 and name3[i]==letter1):
                ans1 = "NO";
                ans3 = "YES";
            else:
                ans1 = "YES";
                ans3 = "YES";  
        elif (name2[i] == name3[i]):
            letter1 = name1[i];
            letter2 = name2[i];
            ans1 = "NO";
            i = i+1;
            while i<N:
                if (name2[i] == name3[i]):
                    i = i+1;
                    continue;
                else:
                    break;
            if i == N:
                ans2 = "YES";
                ans3 = "YES";
            elif (name2[i] == letter1 and name3[i]==letter2):
                ans2 = "YES";
                ans3 = "NO";
            elif (name2[i] == letter2 and name3[i]==letter1):
                ans2 = "NO";
                ans3 = "YES";
            else:
                ans2 = "YES";
                ans3 = "YES";
    ans = ans1 + " " + ans2 + " " + ans3;
    out.write("Case #"+str(j+1)+": "+str(ans)+"\n")
out.close();

