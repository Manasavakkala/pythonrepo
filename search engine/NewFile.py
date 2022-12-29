import win32api
availableDrives=win32api.GetLogicalDriveStrings()
print(availableDrives)
drives=[drivestr for drivestr in availableDrives.split('\ooo') if drivestr]
#drives=drives.split('\ooo)[:-1]
print(drives)