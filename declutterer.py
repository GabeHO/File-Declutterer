import sys
import os

file_extensions = {
	".pdf": "PDFs",
	".exe": "Executables",
	".png": "Pictures",
	".jpg": "Pictures",
	".jpeg": "Pictures",
	".lnk": "Shortcuts",
	".zip": "Zips",
	".docx": "Word Documents"
}

def declutter(dir):
	directories = os.listdir(dir)
	for file in directories:
		file_name, file_extension = os.path.splitext(file)
		if(not file_extension in file_extensions.keys()):
			print(f"SKIPPING {file}")
			continue
		new_dir = os.path.join(dir, file_extensions[file_extension])
		if(not os.path.isdir(new_dir)):
			print(f"{new_dir} NOT FOUND. CREATING")
			os.mkdir(new_dir)
		
		print(f"MOVING {file} TO {new_dir}")
		os.rename(os.path.join(dir, file), os.path.join(new_dir, file))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Incorrect use of script. Correct usage is: \npython3 declutterer.py <dir>")
	else:
		declutter(sys.argv[1])