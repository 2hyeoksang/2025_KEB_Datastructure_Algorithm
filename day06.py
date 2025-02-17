try :
    fn = input("Enter the File Name : ")
    fp = open(fn,'r')
    readme_list = fp.readlines()
    rls = readme_list[0].split('_')
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err:
    print(f'{fn} does not exist. {err}')