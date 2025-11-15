# Create by: Izram Khan
# Date created: 15-Nov-25 [Saturday] (6:21 pm)

#__________________________________________________________________________________________
import PyPDF2
import PyPDF2.errors
import os

def merge_pdf():

    print('''
[-----------------]
|---MERGING-PDF---|
[-----------------]
          ''')
    
    current_path = os.getcwd()
    print(f'Current Path: {current_path}')

    # Creating an instance merger
    merger = PyPDF2.PdfMerger()

    # List to store all files
    pdf_files = []

    while True:
        try:
            no_of_files = int(input('\nHow many files you want to merger: '))
            break

        except ValueError:
            print('\n❌ Error: Please enter a vlaid number!')

    i = 1
    while i <= no_of_files:

            file_name = input(f'\nEnter file number {i}: ')

            if file_name.endswith('.pdf'):
                pdf_files.append(file_name)
                i += 1
            elif i == no_of_files:
                break
            else:
                print('\n❌ Error: Not a pdf file!')
                continue

    print('\n----------------------------------------------------------------------')

    for pdf in pdf_files:
        try:
            # Appending all files in pdf_files to merger
            merger.append(pdf)
            print(f'\n✅ [{pdf}] merged successfully!')

        except FileNotFoundError:
            print(f'\n❌ Error: No such file as "{pdf}" in current path!')

        except PyPDF2.errors.EmptyFileError:
            print(f'\n❌ Error: Empty file found "{pdf}" in current path!')

    # Merged files are store in Merged.pdf
    merger.write('Merged.pdf')
    merger.close()
    print('\n✅ Your all PDF files are merged in \"Merged.pdf\"! ✅')

def split_pdf():

    print('''
[-------------------]
|---SPLITTING-PDF---|
[-------------------]
          ''')

    current_path = os.getcwd()
    print(f'Current Path: {current_path}')
    while True:
        try:
            file_name = input('\nEnter the name of file: ')

            print('\n----------------------------------------------------------------------')

            if not file_name.endswith('.pdf'):
                print('\n❌ Error: Not a pdf file!')

            reader = PyPDF2.PdfReader(file_name)

            for i, page in enumerate(reader.pages, start=1):

                writer = PyPDF2.PdfWriter()
                writer.add_page(page)

                output_file = f'page_{i}.pdf'
            
                with open(output_file,'wb') as f:
                    writer.write(f)
            print(f'\n✅ File: \"{file_name}\" splitted successfully!')
            break
        
        except FileNotFoundError:
            print(f'\n❌ Error: No such file as "{file_name}" in current path!')

        except PyPDF2.errors.EmptyFileError:
            print(f'\n❌ Error: Empty file found "{file_name}" in current path!')

def intro():
    message = '''
| *** WELCOME TO PDF MERGER & SPLITTER *** |   
'''
    import sys
    import time
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06)
    print()
    time.sleep(0.5)

def use():
    intro()
    print('\n1. Merge')
    print('2. Split')
    print('3. Exit')

    while True:
        user_choice = input('\nEnter (1/2/3): ')

        if user_choice == '1':
            merge_pdf()
        elif user_choice == '2':
            split_pdf()
        elif user_choice == '3':
            print('\n🛑 PDF MERGER AND SPLITTER WAS EXITED 🛑')
            break
        else:
            print('\n❌ Error: Please enter (1/2/3)!')

if __name__ == '__main__':
    use()

# ____________________________________________________________________________________________________