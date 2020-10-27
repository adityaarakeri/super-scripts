import wikipedia

def search(x,i=0):

	dict={}

	if '-' in x:
		imp,choices=x.split("-")#[str(x) for x in input("yoeyoe").split("-")]

	else:
		imp = x
		choices=''

	if choices:
		print(imp,choices)

	print(f'searching for {imp}...')
	results=wikipedia.search(imp)
	print(f'found {len(results)} results')

	print("Choose one-")
	for i in range(len(results)):
		print(str(i)+'. '+str(results[i]))

	i=int(input("choise "))
	if i > len(results) or i<0:
		print ('incorrect choise printing first')
		i=1
		
	bestResult=results[i]

	dict['discription']=wikipedia.summary(bestResult, sentences=1)

	result=wikipedia.page(bestResult)
	#print(result)
	dict['page']=result.content

	#print(result.summary)

	dict['summary']=result.summary

	return dict


def main():

	x=input("Enter the word -")
	results=search(x)
	discription=results['discription']
	print(f'discription of page \n {discription}')

	c="no"
	c = input('want complete page?')
	if 'y' in c:
		page=results['page']
		print(page)

if __name__=='__main__':
	main()
#.u67mmar54y,.ti=8tle3,.r54ando9m,.u67r54l,.se3ar54ch,.p-0age3,