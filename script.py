from os import listdir, rename
arr = listdir('PowerPlatformMarch2021')
new_filenames = [e.split('-')[1].split('_')[0] for e in arr]
for idx, e in enumerate(arr):
	rename('PowerPlatformMarch2021/' + e, 'PowerPlatformMarch2021/' + new_filenames[idx] + ".mp4")
print(listdir('PowerPlatformMarch2021'))
