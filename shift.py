import pandas as pd
df1 = pd.read_csv("/Users/ernestomartinez/Documents/Winter17/Math180/newsudrot.csv")
newsudshift = pd.DataFrame(index = 1000)
for i in range (1, 92):
	link = df1.columns[i] # link
	tempnewsudshift = [] # list of shifts
	for j in range (0, 24):
		tempnewsud = df1.ix[j,i]
		tempnewsudshift.append(tempnewsud)
		n1 = 0 # length of link 1
		n2 = 0 # length of link 2
		for a in range (0, len(tempnewsud)-1):
			if tempnewsud[a].isupper():
				n1 = n1 + 1 # sets length of link 1
			else:
				break
		for b in range (n1, len(tempnewsud)):
			if tempnewsud[b].isupper():
				n2 = n2 + 1 # sets length of link 1
		for k in range (0, n1-1): #shifts link 1
			for l in range (0,n2-1): # shifts link 2
				nmid = 0 # length of middle transition
				for b in range (n1, len(tempnewsud)):
					if tempnewsud[b].islower():
						nmid = nmid + 1
				if tempnewsud[len(tempnewsud) - 1] == 'N':
					tempnewsud = tempnewsud[:n1+nmid] + 'sN' + tempnewsud[n1+nmid:len(tempnewsud)-1]	
					for mid in range (n1, len(tempnewsud)):
						if tempnewsud[mid] == 'n':
							tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]	
							tempnewsud = tempnewsud[:n1+nmid-1] + tempnewsud[n1+nmid:]
							break		
				elif tempnewsud[len(tempnewsud) - 1] == 'E':			
					tempnewsud = tempnewsud[:n1+nmid] + 'wE' + tempnewsud[n1+nmid:len(tempnewsud)-1]	
					for mid in range (n1, len(tempnewsud)):
						if tempnewsud[mid] == 'e':
							tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]	
							tempnewsud = tempnewsud[:n1+nmid-1] + tempnewsud[n1+nmid:]
							break			
				elif tempnewsud[len(tempnewsud) - 1] == 'W':
					tempnewsud = tempnewsud[:n1+nmid] + 'eW' + tempnewsud[n1+nmid:len(tempnewsud)-1]
					for mid in range (n1, len(tempnewsud)):
						if tempnewsud[mid] == 'w':
							tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]	
							tempnewsud = tempnewsud[:n1+nmid-1] + tempnewsud[n1+nmid:]
							break				
				elif tempnewsud[len(tempnewsud) - 1] == 'S':
					tempnewsud = tempnewsud[:n1+nmid] + 'nS' + tempnewsud[n1+nmid:len(tempnewsud)-1]
					for mid in range (n1, len(tempnewsud)):
						if tempnewsud[mid] == 's':
							tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]	
							tempnewsud = tempnewsud[:n1+nmid-1] + tempnewsud[n1+nmid:]
							break				
				elif tempnewsud[len(tempnewsud) - 1] == 'U':
					tempnewsud = tempnewsud[:n1+nmid] + 'dU' + tempnewsud[n1+nmid:len(tempnewsud)-1]
					for mid in range (n1, len(tempnewsud)):
						if tempnewsud[mid] == 'u':
							tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]	
							tempnewsud = tempnewsud[:n1+nmid-1] + tempnewsud[n1+nmid:]
							break				
				elif tempnewsud[len(tempnewsud) - 1] == 'D':
					tempnewsud = tempnewsud[:n1+nmid] + 'uD' + tempnewsud[n1+nmid:len(tempnewsud)-1]
					for mid in range (n1, len(tempnewsud)):
						if tempnewsud[mid] == 'd':
							tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]	
							tempnewsud = tempnewsud[:n1+nmid-1] + tempnewsud[n1+nmid:]
							break
				tempnewsudshift.append(tempnewsud)	
			if tempnewsud[n1-1] == 'N':
				tempnewsud = tempnewsud[n1-1] + tempnewsud[:n1-1] + 'n' + tempnewsud[n1:]
				for mid in range (n1, len(tempnewsud)):
					if tempnewsud[mid] == 's':
						tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]
						tempnewsud = tempnewsud[:n1] + tempnewsud[n1+1:]
						break
			elif tempnewsud[n1-1] == 'E':
				tempnewsud = tempnewsud[n1-1] + tempnewsud[:n1-1] + 'e' + tempnewsud[n1:]
				for mid in range (n1, len(tempnewsud)):
					if tempnewsud[mid] == 'w':
						tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]
						tempnewsud = tempnewsud[:n1] + tempnewsud[n1+1:]
						break
			elif tempnewsud[n1-1] == 'W':		
				tempnewsud = tempnewsud[n1-1] + tempnewsud[:n1-1] + 'w' + tempnewsud[n1:]
				for mid in range (n1, len(tempnewsud)):
					if tempnewsud[mid] == 'e':
						tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]
						tempnewsud = tempnewsud[:n1] + tempnewsud[n1+1:]
						break
			elif tempnewsud[n1-1] == 'S':
				tempnewsud = tempnewsud[n1-1] + tempnewsud[:n1-1] + 's' + tempnewsud[n1:]
				for mid in range (n1, len(tempnewsud)):
					if tempnewsud[mid] == 'n':
						tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]
						tempnewsud = tempnewsud[:n1] + tempnewsud[n1+1:]
						break
			elif tempnewsud[n1-1] == 'U':		
				tempnewsud = tempnewsud[n1-1] + tempnewsud[:n1-1] + 'u' + tempnewsud[n1:]
				for mid in range (n1, len(tempnewsud)):
					if tempnewsud[mid] == 'd':
						tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]
						tempnewsud = tempnewsud[:n1] + tempnewsud[n1+1:]
						break
			elif tempnewsud[n1-1] == 'D':
				tempnewsud = tempnewsud[n1-1] + tempnewsud[:n1-1] + 'd' + tempnewsud[n1:]
				for mid in range (n1, len(tempnewsud)):
					if tempnewsud[mid] == 'u':
						tempnewsud = tempnewsud[:mid] + tempnewsud[mid+1:]
						tempnewsud = tempnewsud[:n1] + tempnewsud[n1+1:]
						break			
			tempnewsudshift.append(tempnewsud)		
	newsudshift[link]= tempnewsudshift #keep getting indexing error with this
newsudshift.to_csv(path_or_buf = '/Users/ernestomartinez/Documents/Winter17/Math180/newsudshift.csv')