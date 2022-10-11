from distutils.command.upload import upload
import funcs
import os
import ast
import tabulate

def main():
    while True:
        input("take the photo: (press enter)")
        cont = 1
        while (cont == 1):
            funcs.takePhoto(1)
            if (input("want to continue YES (0) (1) \n") != 1):
                cont = 0
        fileName = os.path.join("./static/IMG/", "image.jpg")


        with open('./tables/listTable.txt', 'r') as f:
            file_contents = f.read()
            lista = ast.literal_eval(file_contents)


        user = [lista[len(lista)-1][0] + 1, "name", "SEX", "hair", "accessories", 'pic'+ str(lista[len(lista)-1][0] + 1) +'.jpg', "email"]

        uploaded = funcs.uploadToS3(fileName, 'avataring-img', 'pic'+ str(lista[len(lista)-1][0] + 1) +'.jpg')

        # Add the user
        lista.append(user)

        # Write the user in the more table like file
        with open('./tables/table.txt', 'w') as fi:
            fi.write(tabulate(lista, headers='firstrow', tablefmt='fancy_grid'))

        # Write the list for the next user
        with open('./tables/listTable.txt', 'w') as fil:
            fil.write(str(lista))

        
        print(uploaded)


if __name__ == "__main__":
    main()